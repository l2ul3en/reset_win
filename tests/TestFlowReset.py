from tests.TestBase import TestBase
from utils.TestData import TestData
from time import sleep
from random import randint
from faker import Faker

class TestFlowReset(TestBase):

    def _read_file(self, filename: str) -> list:
        with open(filename, 'r') as fn:
            lista = [i.strip() for i in fn if i.strip() != '']
        return lista
    
    def _check_info(self, list1: list , list2: list, list3: list) -> bool:
        return len(list1) == len(list2) == len(list3)
    
    def _procesar_data(self,tname: list , tuser: list, touname: list, user: str, clave: str) -> None:
        for i in range(len(tname)):
            if tuser[i].text.strip().lower() == user.lower():
                print(tname[i].text, tuser[i].text, touname[i].text)
                self.managementpage.do_click_apply_reset(int(i+1))
                sleep(2)
                self.managementpage.do_change_password(clave)
                sleep(2)
                print(f"la clave del usuario {user} es {clave}")

    def _get_password(self) -> str:
        faker = Faker()
        word = faker.word()
        num_random = randint(0,9999)
        return word.capitalize() + str(num_random).zfill(TestData.MIN_LENGTH_PASSWORD - len(word))
    
    def _is_valid_password(self, password: str) -> bool:
        return len(password) >= TestData.MIN_LENGTH_PASSWORD
    
    def _do_reset(self, lista: list) -> None:
        for i in lista:
            if TestData.SEP_FIELDS in i:
                username, password = i.split(TestData.SEP_FIELDS)
                self.managementpage.do_send_username(username)
            else:
                password = self._get_password()
                username = i
                self.managementpage.do_send_username(username)
            
            sleep(1)
            tname = self.managementpage.get_table_name()
            tuser = self.managementpage.get_table_user()
            touname = self.managementpage.get_table_ouname()

            #Si la cantidad de filas es la misma
            if self._check_info(tname,tuser,touname):
                if self._is_valid_password(password):
                    self._procesar_data(tname, tuser, touname, username, password)
                else:
                    print(f"La cantidad de caracteres de la contraseña '{password}' del usuario {username} no es valida")
                    raise Exception
            else:
                print("la cantidad de elementos no es la misma")
                raise Exception
            
            #Limpiar caja de texto
            self.managementpage.clear_textbox()

    def test_flow_reset_windows_password(self):
        try:
            self.loginpage.signIn(TestData.W_USER, TestData.W_PASS)
            self.homepage.do_click_reset_password_console()
            self.managementpage.do_click_lupa()
            list_data = self._read_file(TestData.FILE_INPUT_DATA)
            if len(list_data) > 0:
                self._do_reset(list_data)
            else:
                print(f"No se encontraron datos de entrada en {TestData.FILE_INPUT_DATA}")
                raise Exception
        except FileNotFoundError:
            print(f"No se encontro el archivo de datos {TestData.FILE_INPUT_DATA} en el directorio del proyecto")
        except:
            print("Opss!! ocurrio un error")
        finally:
            print("logouttt")
            self.managementpage.do_logout()