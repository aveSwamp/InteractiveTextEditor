from texteditor import texteditor
import os
def help_manager():
    print("Hello, You've started text editor manager.\nYou can use some commands to act with manager:\n1) help - prints this help message\n2) edit [<file_path>[ <start>]] - opens choosen file to edit\n3) exit - ends work of this manager")

def start_state():
    help_manager()
    return True

def askForMCmd(mcmdl):
    _f_arg_line = list(input("text_manager> ").split())
    if _f_arg_line != []:    
        if _f_arg_line[0] not in mcmdl:
            print("Wrong command!")
            help_manager()
            return []
        else:
            return _f_arg_line
    else:
        return []

def isWorking(module_name):
    return module_name

os.system("cls")
manager = start_state()

manager_cmds = ["help","edit","exit"]

while isWorking(manager):
    manager_arg_line = askForMCmd(manager_cmds)
    os.system("cls")
    #print(manager_arg_line)
    if manager_arg_line != []:
        if manager_arg_line[0] == "help":
            help_manager()

        elif manager_arg_line[0] == "edit":
            texteditor(manager_arg_line)

        elif manager_arg_line[0] == "exit":
            manager = False
    
    