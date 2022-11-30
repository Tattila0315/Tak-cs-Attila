import random
import time
from tkinter import *

global nyeresegek
global vesztesegek
global dontetlenek

def nyertesValaszt(generalt,mienk):
    #1 - ko
    #2 - papir
    #3 - ollo
    nyertes = ""
    if generalt == 1 and mienk == 1:
        nyertes = "dontetlen"
    if generalt == 1 and mienk == 2:
        nyertes = "nyertes"
    if generalt == 1 and mienk == 3:
        nyertes = "vesztes"

    if generalt == 2 and mienk == 1:
        nyertes = "vesztes"
    if generalt == 2 and mienk == 2:
        nyertes = "dontetlen"
    if generalt == 2 and mienk == 3:
        nyertes = "nyertes"

    if generalt == 3 and mienk == 1:
        nyertes = "nyertes"
    if generalt == 3 and mienk == 2:
        nyertes = "vesztes"
    if generalt == 3 and mienk == 3:
        nyertes = "dontetlen"
    return nyertes
def randomGeneral():
    eredmeny = random.randint(1,3)
    if eredmeny == 1:
        generaltGombja["text"] = "Kő"
    if eredmeny == 2:
        generaltGombja["text"] = "Papír"
    if eredmeny == 3:
        generaltGombja["text"] = "Olló"

    return eredmeny
def nyertesSzoveg(nyertes):
    global nyeresegek,vesztesegek,dontetlenek
    szoveg.place(x=110, y=80, width=273, height=32)
    if nyertes == "nyertes":
        szoveg["text"] = "<\n Nyertél!"
        nyeresegek = nyeresegek + 1
        allas["text"] = 'Nyereségek: ' + str(nyeresegek) + '\nVesztések: ' + str(vesztesegek) + '\nDöntetlenek: ' + str(dontetlenek)
    if nyertes == "vesztes":
        szoveg["text"] = ">\n Vesztettél.."
        vesztesegek = vesztesegek +1
        allas["text"] = 'Nyereségek: ' + str(nyeresegek) + '\nVesztések: ' + str(vesztesegek) + '\nDöntetlenek: ' + str(dontetlenek)
    if nyertes == "dontetlen":
        szoveg["text"] = "=\n Döntetlen"
        dontetlenek = dontetlenek+1
        allas["text"] = 'Nyereségek: '+str(nyeresegek)+'\nVesztések: '+str(vesztesegek)+'\nDöntetlenek: '+str(dontetlenek)
def idozito(masodperc):
    Masodperc = masodperc
    while masodperc >-1:
        szoveg["text"] = str(masodperc+1)
        szoveg.place(x=110, y=80, width=273, height=30)
        ablak.update()
        time.sleep(1)
        masodperc-=1
        print(masodperc)
def jatek(valasztott):
    idozito(2)
    rnd = randomGeneral()
    nyertes = nyertesValaszt(rnd,valasztott)
    generaltGombja.place(x=50, y=50, width=135, height=110)
    nyertesSzoveg(nyertes)
    ujrainditasGomb.place(x=180, y=210, width=130, height=50)
def Valasztott(valasztas):
    szoveg.place_forget()
    valasztott = 0
    if valasztas == "ko":
        ko.place(x=310, y=50, width=135, height=110)
        ko["state"] = "disabled"
        papir.place_forget()
        ollo.place_forget()
        valasztott = 1
        jatek(valasztott)
    elif valasztas == "papir":
        papir.place(x=310, y=50, width=135, height=110)
        papir["state"] = "disabled"
        ko.place_forget()
        ollo.place_forget()
        valasztott = 2
        jatek(valasztott)
    else:
        ollo.place(x=310, y=50, width=135, height=110)
        ollo["state"] = "disabled"
        ko.place_forget()
        papir.place_forget()
        valasztott = 3
        jatek(valasztott)
def restart():
    ko["state"] = "active"
    papir["state"] = "active"
    ollo["state"] = "active"

    ko.place(x=20, y=250, width=135, height=110)
    papir.place(x=180, y=250, width=135, height=110)
    ollo.place(x=340, y=250, width=135, height=110)
    generaltGombja.place_forget()
    ujrainditasGomb.place_forget()
    szoveg.place_forget()

if __name__ == '__main__':
    ablak = Tk()
    global nyeresegek, vesztesegek, dontetlenek
    nyeresegek = 0
    vesztesegek = 0
    dontetlenek = 0
    ablak.configure(background="#FFFFFF")
    ablak.title("Kő Papír Olló")
    ablak.geometry("500x385")

    szoveg = Label(ablak, text='Válasszon egyet', bg='white', fg='black', font=("Verdana", 10))
    szoveg.place(x=110, y=80, width=273, height=30)

    allas = Label(ablak, text='Nyereségek: '+str(nyeresegek)+'\nVesztések: '+str(vesztesegek)+'\nDöntetlenek: '+str(dontetlenek), bg='white', fg='black', font=("Verdana", 7), justify="right")
    allas.place(x=270, y=170, width=273, height=50)

    nyertes = Label(ablak, text='', bg='white', fg='black', font=("Verdana", 20))
    nyertes.place(x=110, y=80, width=273, height=32)
    nyertes.place_forget()

    ko = Button(ablak, text='Kő', fg='black', bg='white', height=1, width=5, command=lambda:Valasztott('ko'))
    ko.place(x=20, y=250, width=135, height=110)

    papir = Button(ablak, text='Papír', fg='black', bg='white', height=1, width=5, command=lambda:Valasztott('papir'))
    papir.place(x=180, y=250, width=135, height=110)

    ollo = Button(ablak, text='Olló', fg='black', bg='white', height=1, width=5, command=lambda:Valasztott('ollo'))
    ollo.place(x=340, y=250, width=135, height=110)

    generaltGombja = Button(ablak, text='', fg='black', bg='white', height=1, width=5, state="disabled")
    generaltGombja.place(x=50, y=30, width=135, height=110)
    generaltGombja.place_forget()

    ujrainditasGomb = Button(ablak, text='Újraindítás', fg='black', bg='white', height=1, width=5, command=lambda:restart())
    ujrainditasGomb.place(x=50, y=310, width=130, height=50)
    ujrainditasGomb.place_forget()

    ablak.update()
    ablak.mainloop()
