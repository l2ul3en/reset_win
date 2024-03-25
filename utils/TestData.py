from os import environ
import tomllib

class TestData:

    try:
        W_URL = environ["W_URL"]
        W_USER = environ["W_USER"]
        W_PASS = environ["W_PASS"]
    except KeyError as e:
        raise RuntimeError("Could not find a W_USER or W_PASS in environment") from e
    
    FILE_CONFIG = 'config.toml' 
    try:
        with open(FILE_CONFIG, 'rb') as conf:
            REPORT = tomllib.load(conf)
    except tomllib.TOMLDecodeError as e:
        raise RuntimeError(f"Invalid TOML document {FILE_CONFIG}") from e
    
    H1_LOGIN = 'Inside ADManager Plus'
    FILE_INPUT_DATA = 'win_users.txt'
    SEP_FIELDS = ';' # Separador de campos en archivo de entrada de datos
    MIN_LENGTH_PASSWORD = 12 #Numero minimo de caracteres para contraseña
    CSV_FILE = 'procesado.csv'
    CSV_HEADERS = ['Fecha Solicitud', 'Hora Solicitud', 'Ticket', 'Solicitante',
                    'Nombre', 'Usuario', 'Grupo','Encargado', 'Medio de la Solicitud',
                    'Respuesta al Usuario', 'Acciones Realizadas']