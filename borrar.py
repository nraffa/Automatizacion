'''
import os

filename = "EstadoTorrent.txt"
#os. startfile(filename)
file = open( filename , "r+")

print(file.read())
file.close()

'''
'''
from spontit import SpontitResource

#configuracion notificaciones al celular
resource = SpontitResource("nicolas_raffa5828", "AWUC4HVUGE22LBE4Q4H1EACX6KBHG3NJCL0EYJFGBRNCMBK634JR52ZG0REXD7ZXABYUUPMY6QJNF4VY495P85D236QV69NOGY34")
response = resource.push("Hola Guillermo!")
'''
'''
import win32clipboard

# set clipboard data
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText('testing 123')
win32clipboard.CloseClipboard()

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print (data)
'''
import win32clipboard

filename = "EstadoTorrent.txt"
f1 = open(filename , "r+")
f1.truncate(0)     
f1.close()

booleano = True

while booleano == True:
    # get clipboard data
    win32clipboard.OpenClipboard()
    data = str(win32clipboard.GetClipboardData())
    #win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()

    f2 = open(filename , "a+")
    f2.write(data)
    f2.close()

    f3 = open(filename , "r")
    f3_content = f3.read()
    f3.close()

    print(f3_content)
    if f3_content == "Descargando (0)":
        #response_true = resource.push("Descarga en curso!", push_title = "qTorrent", expiration = 20 )
        print("Descarga en curso")
    elif f3_content == "Descargando (1)":
        #response_false = resource.push("Descarga terminada!", push_title = "qTorrent" )
        booleano = False
        print("Descarga terminada")
    else:
        print("no funciona")