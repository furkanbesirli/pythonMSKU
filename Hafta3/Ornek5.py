#Hafta 3 Ornek 5


ortalama = input('Lutfen ortalamanizi giriniz: ')
ortalama = float(ortalama)
if ortalama >= 50 and ortalama <= 100:
    print('GECTI')
elif ortalama > 0 and ortalama <= 49:
    print('KALDI')
else:
    print('Sayi yanlis girildi.')