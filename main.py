from interface.app import App
from interface.login import Login

if __name__ == '__main__':
    Login = Login()

    if Login.logado:
        App()
