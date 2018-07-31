# -*- coding: utf-8 -*-
import os
import sys
import time
import base64

g = "\033[32;1m" #hijau
gt = "\033[0;32m" #hijau terang
bt = "\033[34;1m" #biru terang
b = "\033[36;1m" #biru
m = "\033[31;1m" #merah
c = "\033[0m" #putih
p = "\033[37;1m" #putih
u = "\033[35;1m" #ungu
M = "\033[3;1m" #miring
k = "\033[33;1m" #kuning
kt = "\033[0;33m" #kuning terang
a = "\033[30;1m" #abu abu

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0 / 90)

#harus ini dulu
try:
    import platform
    from xlpy import *
except Exception as err:
    os.system('pip install --upgrade pip')
    os.system('pip install requests')
    os.system('pip install -r requirements.txt')
    os.system('python app.py')()
except KeyboardInterrupt:
	  print (m+"[" + p + "Fail To Import" + m + "]")
	  sys.exit()

#menu
def main_menu():
    try:
        clear()
        slowprint (bt+"------------Tembak Xl Password---------")
        print (b+"\nPilihan Menu Sbb:")
        slowprint (b+"  ["+p+"1"+b+"] "+p+"Beli Paket")
        slowprint (b+"  ["+p+"2"+b+"] "+p+"Minta Password")
        slowprint (b+"  ["+p+"3"+b+"] "+p+"Menu Utama")
        choice = str(input(b+"Pilih >> "+p))
        exec_menu(choice)
        return
    except(KeyboardInterrupt):
        print (m+"     ["+p+"!"+m+"] "+m+"(Ctrl + C ) Detected, "+p+"Trying To Back ...")
        print (m+"     ["+p+"*"+m+"] "+g+"Thank For Using my Pentest Tools ^~^")
        time.sleep(1)
        main_menu()

def exec_menu(choice):
    try:
        clear()
        if(choice == ''):
            menu_actions['main']()
        else:
            try:
                menu_actions[choice]()
            except KeyError:
                print("Invalid selection, please try again.\n")
                menu_actions['main']()
        return
    except(KeyboardInterrupt):
        print (m+"     ["+p+"!"+m+"] "+m+"(Ctrl + C ) Detected, "+p+"Trying To Back ...")
        print (m+"     ["+p+"*"+m+"] "+g+"Thank For Using my Pentest Tools ^~^")
        time.sleep(1)
        exec_menu(choice)

def menu_1():
    try:
        slowprint(b+"Tembak Mode Password")
        print ("")
        msisdn = str(input(b+"Masukan Nomor 62xx >> "+bt))
        passwd = str(input(b+"Masukan Password >> "+bt))
        print ("")
        slowprint (b+"Pilihan Paket")
        print ("")
        slowprint (p+" 01"+b+") "+a+"Xtra Kuota 30GB Rp. 10.000 30day")
        slowprint (p+" 02"+b+") "+a+"Paket Xtra Go Izi | coid")
        slowprint (p+" 03"+b+") "+a+"Paket 3G Rp.22.900 30day")
        slowprint (p+" 04"+b+") "+a+"Paket 5GB Rp.32.900 30day")
        slowprint (p+" 05"+b+") "+a+"Paket 9GB Rp.52.900 30day")
        slowprint (p+" 06"+b+") "+a+"Paket 17GB Rp.82.900 30day")
        print ("")
        lihat = str(input(b+"Pilih Paket >> "+p))
        if lihat == '1' or lihat == '01':
            c = b'\xff\xfe8\x001\x001\x000\x005\x007\x007\x00'
        if lihat == '2' or lihat == '02':
            c = b'\xff\xfe8\x002\x001\x001\x002\x003\x001\x00'
        if lihat == '3' or lihat == '03':
            c = b'\xff\xfe8\x002\x001\x001\x000\x001\x000\x00'
        if lihat == '4' or lihat == '04':
            c = b'\xff\xfe8\x002\x001\x001\x000\x001\x001\x00'
        if lihat == '5' or lihat == '05':
            c = b'\xff\xfe8\x002\x001\x001\x000\x001\x002\x00'
        if lihat == '6' or lihat == '06':
            c = b'\xff\xfe8\x002\x001\x001\x000\x001\x003\x00'
        slowprint("Loading")
        serviceid = c.decode('utf-16')
        xl = XL(msisdn)
        r = xl.loginWithPassword(passwd)
        if(r != False):
            print(xl.purchasePackage(serviceid)['message'])
            print (b+"___________________________________________________________")
            decision = str(input("Want to repeat the process [Y/N]? >> "))
            decision = decision.lower()
            if decision == 'y':
                me(msisdn, passwd)
            else:
                main_menu()
        else:
            print(kt+"["+p+"!"+kt+"] "+m+"Login failed try again")
            print (b+"___________________________________________________________")
            decision = str(input("Want to repeat the process [Y/N]? >> "))
            decision = decision.lower()
            if decision == 'y':
                menu_1()
            else:
                main_menu()
        return

    except(KeyboardInterrupt):
        print (m+"     ["+p+"!"+m+"] "+m+"(Ctrl + C ) Detected, "+p+"Trying To Back ...")
        print (m+"     ["+p+"*"+m+"] "+g+"Thank For Using my Pentest Tools ^~^")
        time.sleep(1)
        menu_1()
        
def menu_2():
    slowprint("Loading")
    try:
        clear()
        print ("")
        msisdn = str(input(b+"Masukan Nomor 62xx>> "+bt))
        slowprint("Loading")
        xl = XL(msisdn)
        print(xl.reqPassword()['message'])
        print (b+"___________________________________________________________")
        decision = str(input("Want to repeat the process [Y/N]? >> "))
        menu_actions['main']() if(decision in ['N','n']) else menu_2()
        return
    except(KeyboardInterrupt):
        print (m+"     ["+p+"!"+m+"] "+m+"(Ctrl + C ) Detected, "+p+"Trying To Back ...")
        print (m+"     ["+p+"*"+m+"] "+g+"Thank For Using my Pentest Tools ^~^")
        time.sleep(1)
        menu_2()
def menu_3(): 
         slowprint("Loading")
         os.system('cd ..;python dor.py')
def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
