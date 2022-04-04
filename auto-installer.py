import os, sys

from colorama import Fore
from lib import installs
from time import sleep

os.system('@echo off')

print(Fore.BLUE+"\n     |    (@@@@@@@@@)    (@@@@@@@@)  (@@@@@@@@@@)  (@@@@@@@)    (@@@@@)     (@@@@@   @@@@@) | \n     |  (@@@@    @@@@)  (@@@   @@@)     (@@@)     (@@@)        (@@@ @@@)    (@@@@@  @@@@@@) |\n     | (@@@@     @@@@)  (@@@@@@)       (@@@)     (@@@@@@@@)  (@@@@  @@@)   (@@@  @@@@  @@)  |\n     |  (@@@    @@@@)  (@@@  @@@@)     (@@@)     (@@@)      (@@@@@@@@@@)   (@@@       @@@)  |\n     |   (@@@@@@@@)    (@@@   @@@)    (@@@)     (@@@@@@@@) (@@@      @@@) (@@@       @@@)   |\n     |                                                                    Telegram @Gaget   |\n     |_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-| \n")

def auto_installer():
    print(Fore.RED+" \n    Telegram @Gaget\n    \n    1)update pip\n    2)install sqlmap\n    00)Exit\n")
    op = input(Fore.GREEN+">>> Enter OPTIONS Number: ")
    if op =='':
        print(Fore.GREEN+"please select number")
    elif op == '1':
        installs.pip_update()
    elif op == '2':
        installs.install_sqlmap()
    elif op == '00':
        installs.exiting()
    

while True:
    try:
        sleep(1)
        auto_installer()
    except KeyboardInterrupt:
        print("\n____________________________________________________________")
        print("\n>>> Exit.... [Telegram @Gaget]")
        sys.exit()