import os

while True:
    print("what can i do for you:" ,end=" ")

    a=input()

    if ("run" in a or "execute" in a or "open" in a) and ("cmd" in a or "command" in a):
        os.system("start cmd.exe")
    elif ("run" in a or "execute" in a or "play" in a or "open" in a) and ("vlc" in a):
        os.system("vlc")
    elif ("run" in a or "execute" in a or "open" in a) and ("chrome" in a):
        os.system("chrome www.google.com")
        
    elif ("run" in a or "execute" in a or "start" in a or "open" in a) and ("word" in a and ( "office" in a or "microsoft" in a)):
        os.system("start winword")
    elif ("run" in a or "execute" in a or "start" in a or "open" in a) and ("sublime" in a):
        os.system("start sublime_text")
    elif ("run" in a or "execute" in a or "start" in a or "open" in a) and ("calculator" in a):
        os.system("calc.exe")
    elif ("run" in a or "execute" in a or "start" in a or "open" in a) and ("paint" in a):
        os.system("mspaint.exe")

    elif ("shutdown" in a):
        os.system("shutdown /s")
    elif ("restart" in a):
        os.system("shutdown /r")
    elif "exit" in a or "close" in a or "quit" in a:
        break
    else:
        print("don't support")
    
