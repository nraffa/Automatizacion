import pyautogui
import time
import subprocess
import os 
import win32clipboard
from spontit import SpontitResource
#from spontit import Expiration


#configuracion notificaciones al celular
resource = SpontitResource("nicolas_raffa5828", "AWUC4HVUGE22LBE4Q4H1EACX6KBHG3NJCL0EYJFGBRNCMBK634JR52ZG0REXD7ZXABYUUPMY6QJNF4VY495P85D236QV69NOGY34")

# set clipboard data
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
#win32clipboard.SetClipboardText('testing 123')
win32clipboard.CloseClipboard()


#print(pyautogui.position())
filename = "EstadoTorrent.txt"


booleano = True


def update():
    #time.sleep(60*5)

    #limpio text file
    f1 = open(filename , "r+")
    f1.truncate(0)     
    f1.close()

    #Abro qTorrent
    subprocess.Popen('C:\Program Files\qBittorrent\\qbittorrent.exe')
    time.sleep(5)
  
    #Me desplazo hacia donde esta el estado
    pyautogui.moveTo(75, 159, duration = 1) 
    pyautogui.click(75, 159) 
   
    #Copio Estado
    pyautogui.hotkey("ctrlleft", "c")

    #Cierro ventana del qTorrent
    pyautogui.click(1348, 16) 
    time.sleep(2)
    #deposito texto copiado en una variable
    
    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()

    f2 = open(filename , "a+")
    f2.write(data)
    f2.close()
    

def evaluate_update():
    #Abro txt file para su lectura (sin abrir el archivo en si)
    f3 = open(filename , "r")
    f3_content = f3.read()
    f3.close()

    if f3_content == "Descargando (1)":
        response_true = resource.push("Descarga en curso!", push_title = "qTorrent")#, expirationStamp = 5 )
        #print("Descarga en curso")
    elif f3_content == "Descargando (0)":
        booleano = False
        print(booleano)
        response_false = resource.push("Descarga terminada!", push_title = "qTorrent" )
        subprocess.Popen('C:\Program Files\qBittorrent\\qbittorrent.exe').terminate()
        
        #print("Descarga terminada")
        
    

while booleano == True :
    update()
    evaluate_update()
    print(booleano)
    if booleano == False:
        break
    


