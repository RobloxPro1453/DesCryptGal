# -*- coding: utf-8 -*-
import re
from funcandvar import *
from time import sleep
from des import *
import questionary as qa
from rich import print as rprint
from ayardosyasi import Dosyalar
import tkinter as tk
import os
from rich.progress import wrap_file


""" 
-kod çorba gibi
- class kullanılabilir
- encode decode fonksiyonlarıında da questionary modulu ile input alınabilir (+1)
"""


def converttobyte(strin):
    bytes_str = eval("b'" + strin + "'")
    return bytes_str

def bytetostring(bytes_str):
    string_str = repr(bytes_str)[2:-1]
    return string_str

def ozel_karakter_sil(string):
    temiz_string = re.sub(r'[^\w\s]', '', string)
    return temiz_string



def Encode():
    clear()
    dosya = Dosyalar()
    rprint("[yellow]Sadece unicode karakterler kullanınız.[/yellow]")
    key = input("Anahtar: ")
    if len(key) != 8:
        clear()
        rprint("[red][strong]Anahtar 8 karakter uzunluğunda olmalı.[/strong][/red]")
    else:
        if dosya.ayarlar.get("txtyeyaz"):

            def tkinterverial():
                global text
                text = entry.get('1.0', 'end-1c')
                root.destroy()

                
            root = tk.Tk()
            root.title("Metin Girin")
            root.attributes("-topmost", True)
            
            entry_frame = tk.Frame(root)
            entry_frame.pack(pady=10)

            global entry, text
            entry = tk.Text(entry_frame, width=50, height=30)
            entry.pack()
            
            oku_button = tk.Button(root, text="Metni gir", command=tkinterverial)
            oku_button.pack()
            
            root.mainloop()
        else:
            text = input("Şifrelenecek metin: ")
            clear()
        if text.strip() == "":
            clear()
            rprint("[red][strong]Geçerli bir metin giriniz..[/strong][/red]")
        else:

            # sifrekat = dosya.ayarlar.get("sifrelemesayisi")

            with CliStatus("İşleniyor..."):
                clear()
                dodes = des(key, CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

                sifrelenmis = bytetostring(dodes.encrypt(text))

                # x = 0
                # while x == sifrekat:
                #     sifrelenmis = dodes.encrypt(sifrelenmis)
                #     x+=1

                # rprint(f"Şifrelenmiş metin (Şifreleme sayısı {str(sifrekat)}):")
            
                rprint("[blue]Şifrelenmiş metin:[/blue]")            

                rprint("[green][strong]BAŞLANGIÇ[/strong][/green]".center(70,"▬"))
                rprint("[yellow]{sf}[/yellow]".format(sf=sifrelenmis))
                rprint("[green][strong]BİTİŞ[/strong][/green]".center(70,"▬"))

                # rprint(Panel("[yellow]{sf}[/yellow]".format(sf=sifrelenmis), title="BAŞLANGIÇ", subtitle="BİTİŞ"))
    os.system('pause') 


def Decode():
    clear()
    dosya = Dosyalar()
    rprint("[yellow]Sadece unicode karakterler kullanınız.[/yellow]")
    key = input("Anahtar: ")
    if len(key) != 8:
        clear()
        rprint("[red][strong]Anahtar 8 karakter uzunluğunda olmalı.[/strong][/red]")
    else:
        if dosya.ayarlar.get("txtyeyaz"):

            def tkinterverial():
                global text
                text = entry.get('1.0', 'end-1c')
                root.destroy()
                
            root = tk.Tk()
            root.title("Metin Girin")
            root.attributes("-topmost", True)
            
            entry_frame = tk.Frame(root)
            entry_frame.pack(pady=10)

            global entry, text
            entry = tk.Text(entry_frame, width=50, height=30)
            entry.pack()
            
            oku_button = tk.Button(root, text="Metni gir", command=tkinterverial)
            oku_button.pack()
            
            root.mainloop()
        else:
            text = input("Çözülecek metin: ")
            clear()
        if text.strip() == "":
            clear()
            rprint("[red][strong]Geçerli bir metin giriniz..[/strong][/red]")
        else:
            # sifrekat = int(input("Şifrelenme sayısı: "))
            with CliStatus("İşleniyor..."):
                clear()
                dosya = Dosyalar()
                dodes = des(key, CBC, b"\0\0\0\0\0\0\0\0",pad=None)

                cozulmus = ozel_karakter_sil(dodes.decrypt(converttobyte(text)).decode())
                    
                # if sifrekat == 1:
                #     cozulmus = ozel_karakter_sil(dodes.decrypt(converttobyte(text)).decode())
                # else:
                #     cozulmus = dodes.decrypt(converttobyte(text))
                #     x = 0
                #     while x == sifrekat:
                #         cozulmus = dodes.decrypt(converttobyte(cozulmus))
                #         x+=1
                #         if (x+1) == sifrekat:
                #             cozulmus = ozel_karakter_sil(dodes.decrypt(converttobyte(cozulmus)).decode())
                #             break


                rprint("[blue]Çözülmüş metin:[/blue]")
                rprint("[green][strong]BAŞLANGIÇ[/strong][/green]".center(70,"▬"))
                rprint("[yellow]{sf}[/yellow]".format(sf=cozulmus))
                rprint("[green][strong]BİTİŞ[/strong][/green]".center(70,"▬"))

                # rprint(Panel("[yellow]{sf}[/yellow]".format(sf=cozulmus), title="BAŞLANGIÇ", subtitle="BİTİŞ"))
            os.system('pause')

def Ayarlar():
    while True:
        clear()
        dosya = Dosyalar()
        ayarlar = dosya.ayarlar
        tr = lambda opt: "AÇIK" if opt else "KAPALI"

        ayarlar_options = [
            'Şifrelenecek ve çözülecek metni bir tkinter penceresine yaz. (uzun metinler için önerilir): '+tr(ayarlar['txtyeyaz']),
            'Şifreleme sayısı (CPU kullanımını arttırır) (inaktif)'+": "+str(ayarlar["sifrelemesayisi"]),
            'Geri dön'
        ]

        ayar_islem = qa.select(
            'İşlemi seç',
            ayarlar_options,
            style=prompt_tema,
            instruction=" "
            ).ask()
        
        if ayar_islem == ayarlar_options[0]:
            dosya.set_ayar("txtyeyaz", not ayarlar['txtyeyaz'])


        if ayar_islem == ayarlar_options[1]:
            max_dl = qa.text(
                message = 'Kaç defa şifreleme yapılsın?',
                default = str(ayarlar["sifrelemesayisi"]),
                style = prompt_tema
            ).ask(kbi_msg="")
            if isinstance(max_dl,str) and max_dl.isdigit():
                dosya.set_ayar("sifrelemesayisi", int(max_dl))


        elif ayar_islem == ayarlar_options[2]:
            break
    

def menu_loop():
    while True:
        clear()
        islem = qa.select(
            "İşlemi seç",
            choices=['Encode',
                    'Decode',
                    'Ayarlar',
                    'Kapat'],
            style=prompt_tema,
            instruction=" "
        ).ask()
        
        if islem == "Encode":
            Encode()
        elif islem == "Decode":
            Decode()
        elif islem == "Ayarlar":
            Ayarlar()
        else:
            with CliStatus("Kapatılıyor..."):
                sleep(1)
                clear()
                exit()


if __name__ == '__main__':
    menu_loop()


