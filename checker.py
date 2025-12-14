import re
import sys
from colorama import Fore, Style, init

init()

def banner():
    print(Fore.GREEN + r"""
  ____                                   _ 
 |  _ \ __ _ ___ _____      _____  _ __ | |
 | |_) / _` / __/ __\ \ /\ / / _ \| '_ \| |
 |  __/ (_| \__ \__ \\ V  V / (_) | | | |_|
 |_|   \__,_|___/___/ \_/\_/ \___/|_| |_(_)

      PASSWORD STRENGTH CHECKER TOOL v1.0
          Developed by Jas Nisha
================================================
""" + Style.RESET_ALL)

def check_password(password):
    if len(password) < 12:
        print(Fore.RED + "❌ Password should have at least 12 characters" + Style.RESET_ALL)

    elif re.search("[!@#$%^&*]", password) is None:
        print(Fore.RED + "❌ Password must contain at least 1 special character" + Style.RESET_ALL)

    elif re.search("[a-z]", password) is None:
        print(Fore.RED + "❌ Password must contain at least 1 lowercase letter" + Style.RESET_ALL)

    elif re.search("[A-Z]", password) is None:
        print(Fore.RED + "❌ Password must contain at least 1 uppercase letter" + Style.RESET_ALL)
        
    elif re.search("[0-9]", password) is None:
        print(Fore.RED + "❌ Password must contain at least 1 number" + Style.RESET_ALL)    

    else:
        print(Fore.GREEN + "✅ Valid & Strong Password" + Style.RESET_ALL)

def main():
    banner()

    # CLI argument support
    if len(sys.argv) == 2:
        password = sys.argv[1]
    else:
        password = input("Enter password : ")

    check_password(password)

if __name__ == "__main__":
    main()
