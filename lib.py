import os,sys

from colorama import Fore
from time import sleep

class installs:

    def pip_update():
        print(Fore.RED+'>>> please wait checked pip update')
        os.system('pip install --upgrade pip')

    def install_sqlmap():
        print(Fore.RED+'>>> please wait install SQLMAP')
        os.system('pip install sqlmap')
    def exiting():
        print('\n>>> Exit.... [Telegram @Gaget]')
        sleep(0.5)
        sys.exit()