# coding:cp1254
import sys
from getpass import fallback_getpass
"""
Bu program kullan�c�dan komut sat�r�nda kullan�c� ad� ve �ifreyi ister
Bilgilerin kontrol�n� sa�lar. Gerekli bilgiler bir s�zl�k i�inden �ekilir.
Konsol ortam�nda �al���r.
"""

Login = {
"erkan":{"sifre":"erkan123","yetkisi":1,"email":"erkan9unlu@gmail.com"},
"serkan":{"sifre":"123456Seven","yetkisi":2,"email":"serkan@gmail.com"},
"ozkan":{"sifre":"bjk1903.","yetkisi":3,"email":"ozkan@yahoo.com"},
"hazal": dict(sifre="hazal123", yetkisi=3, email="hazal@hotmail.com")
}
hak = 3
girisBasariliMi = False
user = paswd = ""

def win_getpass(prompt='Password: ', stream=None):
    """Prompt for password with echo off, using Windows getch()."""
    if sys.stdin is not sys.__stdin__:
        return fallback_getpass(prompt, stream)
    import msvcrt
    for c in prompt:
        msvcrt.putch(c)     #msvcrt.putwch(c)
    pw = ""
    while 1:
        c = msvcrt.getch() #msvcrt.getwch()
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            if pw == '':
                pass
            else:
                pw = pw[:-1]
                msvcrt.putch('\b')  #msvcrt.putwch('\b')
                msvcrt.putch(" ")   #msvcrt.putwch(" ")
                msvcrt.putch('\b')  #msvcrt.putwch('\b')
        else:
            pw = pw + c
            msvcrt.putch("*")  #msvcrt.putwch("*")
    msvcrt.putch('\r')         #msvcrt.putwch('\r')
    msvcrt.putch('\n')         #msvcrt.putwch('\n')
    return pw

while hak:
    user = input("Kullanici adi".ljust(15)+": ")   # python 3 i�in buras�
    #user = raw_input("Kullanici adi".ljust(15)+": ")
    paswdM = "Sifre".ljust(15)+": "
    #paswd = getpass.getpass("Please enter your password:")
    paswd = win_getpass(prompt=paswdM)

    if user in Login:
        if Login[user]["sifre"] == paswd:
            girisBasariliMi = True
            break
        else:
            print(u"Yanl�� �ifre girdiniz. Tekrar deneyin.")
    else:
        print(u"Bu kullan�c� sistemde yok.")
    hak -= 1

if girisBasariliMi:
    if Login[user]["yetkisi"] == 1:
        print(u"Sisteme admin olarak giri� yapt�n�z")
    elif Login[user]["yetkisi"] == 2:
        print(u"Sisteme superuser olarak giri� yapt�n�z")
    elif Login[user]["yetkisi"] == 3:
        print(u"Sisteme normal kullan�c� olarak giri� yapt�n�z")
    else:
        print(u"Sisteme bilinmeyen bir yetkiyle giri� yapt�n�z.")
else:
    print(u"Sisteme giri� yetkiniz yok.")