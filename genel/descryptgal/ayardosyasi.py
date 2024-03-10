from os import path,mkdir
import json

class Dosyalar:
    # Defaults to C:/User/xxx/DESbyRobloxpro veya ~/DESbyRobloxpro dizini.

    def __init__(self):
        self.ta_path = path.join(path.expanduser("~"), "DESbyRobloxpro" )
        self.ayar_path = path.join(self.ta_path, "ayarlar.json")
        default_ayarlar = {
            "txtyeyaz" : False,
            "sifrelemesayisi":1
        }

        if not path.isdir(self.ta_path):
            mkdir(self.ta_path)

        if path.isfile(self.ayar_path):
            ayarlar = self.ayarlar
            for ayar,value in default_ayarlar.items():
                if not ayar in ayarlar:
                    self.set_ayar(ayar,value)
        else:
            with open(self.ayar_path,"w",encoding="utf-8") as fp:
                fp.write('{}')
            self.set_ayar(ayar_list=default_ayarlar)


    def set_ayar(self, ayar = None, deger = None, ayar_list = None):
        assert (ayar != None and deger != None) or ayar_list != None
        ayarlar = self.ayarlar
        if ayar_list:
            for n,v in ayar_list.items():
                ayarlar[n] = v
        else:
            ayarlar[ayar] = deger
        with open(self.ayar_path,"w",encoding="utf-8") as fp:
            json.dump(ayarlar,fp,indent=2)

    @property
    def ayarlar(self):
        with open(self.ayar_path,encoding="utf-8") as fp:
            return json.load(fp)