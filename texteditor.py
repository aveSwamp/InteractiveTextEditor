def texteditor(arg_line):
    import os
    def help_editor():
        print("This is text editor")
        print("You can use this commands:")
        print("1)append <string> - add <string> to the end of file")
        print("2)count - prints count of strings in your file; press [ENTER] to return to your text")
        print("3)remove <fil> <sil> - removes strings from your file from <fil> to <sil>")
        print("4)assign <index> <string> - changes value of <index> string in file to <string>")
        print("5)scroll <dir>[ <number>]:\n5.1)<dir> = up - scrolls up your file on 1 string\n5.2)<dir> = down - scrolls down your file on 1 string\n5.3)<number> - changes count of scrolling strings to <number>")
        print("6)help - prints this message")
        print("7)exit - exit from text editor")
        #print("P.S. All commands works in choosen fragment of text")

    def isWorking(module_name):
        return module_name

    def askForECmd(ecmdl):
        _f_arg_line = list(input("text_editor> ").split())
        if _f_arg_line != []:    
            if _f_arg_line[0] not in ecmdl:
                print("Wrong command!")
                help_editor()
                return []
            else:
                return _f_arg_line
        else:
            return []
    
    def print_text_fragment(args):
        print(args)
        termSize = tuple(os.get_terminal_size())# W x H

        file_path,fline,eline = None, 0, termSize[1]-2
        filename = None

        if len(args) == 3:
            file_path,fline = args[1:3]

        elif len(args) == 2:
            file_path = args[1]

        elif len(args) == 1:
            file_path = input("Please input full path where you want to save your file: ")    

        filename = list(file_path.split('\\'))[len(list(file_path.split('\\')))-1]

        text_buffer = ['~' + ' ' * (termSize[0] - 1)] * (termSize[1] - 3)#height = termH-3 width = termW-1
        screen_buffer = []

        file_stream = None
        fline = int(fline)
        eline = fline + termSize[1]-4

        #opening or creating file
        if file_path != None:
            if os.path.exists(file_path) == True:
                file_stream = open(file_path,"r+")
            else:
                file_stream = open(file_path,"x+")
        else:
            file_stream = open(file_path,"x+")

        read_buffer = []
        readflag = False
        for i, line in enumerate(file_stream):
            if i == fline:
                readflag = True

            if readflag == True:
                if len(line) > termSize[0]:
                    read_buffer.append(line[:termSize[0]])
                else:
                    read_buffer.append(line[:len(line)])

            if i == eline:
                readflag = False

        file_stream.close()

        for i in range(len(read_buffer)):
            text_buffer[i] = read_buffer[i]


        #generating output string
        title = filename
    
        for i in range(termSize[1] - 1):
            if i == 0:
                screen_buffer.append("#" + title + ("#" * (termSize[0] - len(title) - 1)) + "\n")
            elif i == termSize[1] - 2:
                screen_buffer.append("#" * termSize[0])
            else:
                if text_buffer[i-1][len(text_buffer[i-1])-1] == "\n":
                    screen_buffer.append(text_buffer[i-1])
                else:
                    screen_buffer.append(text_buffer[i-1] + "\n")

        out_string = screen_buffer[0]
        for i in screen_buffer[1:]:
            out_string += i
        print(out_string)
        return (file_path,filename,fline,eline)



    editor_cmds = ["append", "count", "remove", "assign", "scroll", "help", "exit"]
    text_editor = True
    path = arg_line[1]
    count = sum(1 for i,line in enumerate(open(path,"r")))
    help_editor()
    input()
    while isWorking(text_editor):
        abrakadabra = print_text_fragment(arg_line)
        editor_arg_line = askForECmd(editor_cmds)
        os.system("cls")
        #print(manager_arg_line)
        if editor_arg_line != []:
            if editor_arg_line[0] == "help":
                help_editor()
                input()
                os.system("cls")
            elif editor_arg_line[0] == "append":
                fs = open(abrakadabra[0],"a")
                fs.write(" ".join(editor_arg_line[1:]) + "\n")
                fs.close()
            elif editor_arg_line[0] == "count":
                print("count of strings in your file: "+ str(count))
                input()
            elif editor_arg_line[0] == "remove":
                fs = open(abrakadabra[0],"r")
                fb = [line for i,line in enumerate(fs) if i < int(editor_arg_line[1]) or i > int(editor_arg_line[2])]
                fs.close()
                fs = open(abrakadabra[0],"w")
                [fs.write(i) for i in fb]
                fs.close()
            elif editor_arg_line[0] == "assign":
                fs = open(abrakadabra[0],"r")
                fb = fs.readlines()
                fs.close()
                fb[int(editor_arg_line[1])] = editor_arg_line[2]+"\n"
                fs = open(abrakadabra[0],"w")
                [fs.write(i) for i in fb]
                fs.close()
            elif editor_arg_line[0] == "scroll":
                if editor_arg_line[1] == "up" and abrakadabra[2] != 0:
                    if abrakadabra[2] != 0:
                        arg_line = ["edit", abrakadabra[0], str(abrakadabra[2]-(1 if len(editor_arg_line) == 2 else int(editor_arg_line[2])))]
                if editor_arg_line[1] == "down":
                    if abrakadabra[3] != count - 1:
                        arg_line = ["edit", abrakadabra[0], str(abrakadabra[2]+(1 if len(editor_arg_line) == 2 else int(editor_arg_line[2])))]
            elif editor_arg_line[0] == "exit":
                text_editor = False