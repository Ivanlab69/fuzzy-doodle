import os
import shutil
import subprocess
import sys

def print_banner():
    banner = """
  __                         _____                   _             _ 
 / _|_   _ _________   _    |_   _|__ _ __ _ __ ___ (_)_ __   __ _| |
| |_| | | |_  /_  / | | |_____| |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
|  _| |_| |/ / / /| |_| |_____| |  __/ |  | | | | | | | | | | (_| | |
|_|  \__,_/___/___|\__, |     |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                   |___/                                             
    """
    print(banner)

if __name__ == "__main__":
    print_banner()
    # Your existing code here 

def run_shell():
    while True:
        command = input("$~ ")

        # Exit condition
        if command == "exit":
            print("Exiting...")
            break

        # File system commands (Bash-like)
        elif command.startswith("ls"):
            path = command[3:].strip() or "."
            try:
                print("\n".join(os.listdir(path)))
            except FileNotFoundError:
                print(f"ls: {path}: No such file or directory")
        
        elif command.startswith("cd"):
            path = command[3:].strip() or os.path.expanduser("~")
            try:
                os.chdir(path)
            except FileNotFoundError:
                print(f"cd: {path}: No such file or directory")

        elif command == "pwd":
            print(os.getcwd())

        elif command.startswith("mkdir"):
            path = command[6:].strip()
            try:
                os.mkdir(path)
            except FileExistsError:
                print(f"mkdir: {path}: File exists")
            except FileNotFoundError:
                print(f"mkdir: {path}: No such file or directory")

        elif command.startswith("rm"):
            path = command[3:].strip()
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
            except FileNotFoundError:
                print(f"rm: {path}: No such file or directory")
            except IsADirectoryError:
                print(f"rm: {path}: Is a directory")

        # Networking commands (Windows-like)
        elif command == "ipconfig":
            subprocess.run(["ipconfig"], check=True)
        
        elif command.startswith("ping"):
            target = command[5:].strip() or "localhost"
            subprocess.run(["ping", target], check=True)
        
        elif command == "netstat":
            subprocess.run(["netstat"], check=True)
        
        elif command.startswith("tracert"):
            target = command[8:].strip() or "google.com"
            subprocess.run(["tracert", target], check=True)
        
        elif command.startswith("nslookup"):
            domain = command[9:].strip() or "google.com"
            subprocess.run(["nslookup", domain], check=True)

        # Command to open Echoflux (2).py
        elif command == "echoflux":
            subprocess.run(["python", "Echoflux (2).py"], check=True)

        # For other system commands (like `ls`, `ping`, etc.)
        else:
            os.system(command)

if __name__ == "__main__":
    run_shell()
