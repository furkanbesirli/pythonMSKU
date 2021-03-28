#Hafta 4 Ornek 3

import math

dongu = 0
sayac = 2
toplam = 0
enBuyuk = 0
enKucuk = 0
carpim = 0

sayi = float(input('Sayi giriniz: '))
sayi2 = float(input('Tekrar Sayi giriniz: '))
if sayi > sayi2:
    enBuyuk = sayi
    enKucuk = sayi2
else:
    enBuyuk = sayi2
    enKucuk = sayi
toplam = sayi + sayi2
carpim = sayi * sayi2

while dongu == 0:
    devam = int(input("Devam etmek icin 1'e basiniz: "))
    if devam == 1:
        sayi3 = float(input('Sayi girisi yapiniz: '))
        sayac += 1
        toplam += sayi3
        carpim = carpim * sayi3
        if sayi3 > enBuyuk:
            enBuyuk = sayi3
        elif sayi3 < enKucuk:
            enKucuk = sayi3
        aritmetik = toplam / sayac
        geometrik = carpim ** 0.5
    else:
        print('En buyuk sayi: ', enBuyuk)
        print('En kucuk sayi: ', enKucuk)
        print('Aritmetik ortalamalari: ', aritmetik)
        print('Geometrik ortalamalari: ', geometrik)

        print('Program kapatiliyor...')
        dongu += 1



















