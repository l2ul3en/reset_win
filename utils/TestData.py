from os import environ

class TestData:

    try:
        W_URL = environ["W_URL"]
        W_USER = environ["W_USER"]
        W_PASS = environ["W_PASS"]
    except KeyError as e:
        raise RuntimeError("Could not find a W_USER or W_PASS in environment") from e
    
    H1_LOGIN = 'Inside ADManager Plus'
    FILE_INPUT_DATA = 'win_users.txt'
    SEP_FIELDS = ';' # Separador de campos en archivo de entrada de datos
    MIN_LENGTH_PASSWORD = 12 #Numero minimo de caracteres para contraseña