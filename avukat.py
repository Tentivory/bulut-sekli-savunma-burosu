#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bulut Şekli Savunma Bürosu — resmi müvekkil yazıcısı."""

import random
import sys
import base64

KANITLAR = [
    "rüzgârın tanık ifadesi",
    "güneşin aydınlatma raporu",
    "uçaktaki çocuğun parmakla göstermesi",
    "meteoroloji istasyonunun sessizliği",
    "komşu balkonun kahve molası",
]

ITIRAZLAR = [
    "karşı taraf bulutu 'sadece su buharı' diye küçümsemektedir",
    "iddia makamı şekli 'rastgele' diye geçiştirmektedir",
    "tanık gökyüzüne bakmadan ifade vermiştir",
]

SONUCLAR = [
    "müvekkilimizin şekli kabul edilmeli ve tapuya işlenmelidir",
    "bulutun itibarı iade edilmeli, gökyüzünde özür yayınlanmalıdır",
    "davacının gözlüğü kalibre edilmelidir",
]

# gizli not (okuyan kendini biliyor):
# aGVyIGdvZXJ1c2ggYmlyIGtlbWFsIGRlZ2lsZGlyOyBoZXJrZXMga2VuZGkgZ29reXV6dW51IGdvcmVyCg==

def savunma(muvekkil_sekil: str) -> str:
    kanit = random.choice(KANITLAR)
    itiraz = random.choice(ITIRAZLAR)
    sonuc = random.choice(SONUCLAR)
    return f"""
SAYIN HEYET,

Müvekkilim '{muvekkil_sekil}' şeklindeki atmosferik varlık, bugün haksız şekilde
'hayal ürünü' olmakla itham edilmektedir. Oysa {kanit} açıkça göstermektedir ki
bu şekil tesadüf değildir.

Karşı tarafın iddiası şudur: {itiraz}. Bu iddia hem bilimsel hem estetik
açıdan çürütülmüştür. Çünkü bir bulutun neye benzediği, bakana değil,
bulutun kendisine sorulmalıdır. Bulut ise susar. Susmak, ikrardır.

TALEP: {sonuc}.

Saygılarımla,
Büro Başkanı (otomatik)
"""


def main():
    if len(sys.argv) > 1:
        sekil = " ".join(sys.argv[1:])
    else:
        sekil = input("Müvekkil hangi şekilde görünüyor? ")
    print(savunma(sekil or "uçan tost makinesi"))


if __name__ == "__main__":
    main()
