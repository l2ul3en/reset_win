import os

class TestData:

    try:
        W_URL = os.environ["W_URL"]
        W_USER = os.environ["W_USER"]
        W_PASS = os.environ["W_PASS"]
    except KeyError as e:
        raise RuntimeError("Could not find a W_USER or W_PASS in environment") from e
    
    H1_LOGIN = 'Inside ADManager Plus'
    CHANGE_SUCCESS = 'Successfully'