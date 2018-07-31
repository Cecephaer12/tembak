# -*- coding: utf-8 -*-
import os
import sys
import platform
import time
from xlpy import *
import base64

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[1;32m'
O = '\x1b[33m'
B = '\x1b[34m'
P = '\x1b[35m'
C = '\x1b[36m'
GR = '\x1b[37m'



def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)
def lodprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7.0/90)
        
        def main_menu():
       clear()
       slowprint(W + '#'*45)
       slowprint(W + '     -== '+gt+'Tembak Paket XL'+W+' ==-')
       slowprint(W + '#'*45)
       print(W + '# ' + str(time.strftime('%a, %d %B %Y')))
       print(W + '# Provider gsm Operator ' + C + str(os.popen('getprop gsm.operator.alpha').read().split('\n')[0]))
       print(W + '# Python ' + C + str(pv) + W + ', ' + C + str(os.popen('getprop ro.product.device').read().split('\n')[0]) + ' ' + str(os.popen('getprop ro.build.version.release').read().split('\n')[0]) + ' Build SDK ' + str(os.popen('getprop ro.build.version.sdk').read().split('\n')[0]))
       print(W + '#'*45)

chr=(gt+"""
 #######  #     #  # ##### 
#  C      # H   #  # U   #     
#   E     #   A #  #   D #   
#  C      #######  # I N # 
#   E     #  E  #  #  #
#  P      # R   #  #   #
 ######## #     #  #     #
 =================================
""")
l="Harap tunggu.."

def main_menu():
    clear()
    slowprints(chr)
    print(p+
        "   Tembak Xl Mode Otp" +
        "\nPilih Salah Satu:"
        "\n  [1] Menu Beli Paket" + 
        "\n  [2] Minta Otp Code" +
        "\n  [3] Menu utama"+
        "\n  [0] Keluar"
    )
    choice = str(input(" Enter here Example : 1 >>"))
    exec_menu(choice)
    return

def exec_menu(choice):
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

def menu_1():
    lodprint(l)
    clear()
    print(chr)
    print(p+"Menu Beli Paket Xl")
    msisdn = str(input("Masukan No Ex : 62xx >>"))
    clear()
    print(chr)
    po = str(input(p+"Masukan Kode Otp "))
    clear()
    print(chr)
    print (p+" 1.Xtra Kuota 30GB Rp. 10.000")
    print (p+" 2.Xtra 10GB 30day 59k")
    print (p+" 3.Manual service id")
    pkt = str(input("Pilih Sesuai Keinginan >> "))
    
    if pkt == '1':
        i = '8110577'
    elif pkt == '2':
        i ='8211183'
    elif pkt == '3':
        i = str(input("Masukan Service ID Paket >>"))
    else:
        print("Pilihan gak tercantum")
    lodprint(l)
    serviceid = i
    xl = XL(msisdn)
    r = xl.loginWithOTP(po)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
        decision = str(input(p+"Ulangi Proses [Y/N]? "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
        
def menu_2():
    lodprint(l)
    clear()
    print(chr)
    print(p+"Meminta Kode Otp Baru")
    msisdn = str(input("Masukan Nomor Ex: 62xx  >>"))
    lodprint(l)
    xl = XL(msisdn)
    print(xl.reqOTP()['message'])
    decision = str(input(p+"Ulangi Proses[Y/N]? "))
    menu_actions['main']() if(decision in ['N','n']) else menu_2()

def menu_4():
    clear()
    print(".::Password Menu::.")
    msisdn = str(input("Input your MSISDN >> "))
    xl = XL(msisdn)
    print(xl.reqPassword()['message'])
    decision = str(input("Want to repeat the process [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['3']()
    return

def menu_3():
     lodprint(l)
     os.system('cd ..;python chr.py')


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
