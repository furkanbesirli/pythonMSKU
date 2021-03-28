#Hafta 3 Ornek 6


sayi = input('Bir sayi girisi yapiniz: ')
sayi = int(sayi)

if sayi % 2 == 0:
    print('Girilen sayi cifttir.')
elif sayi % 2 == 1:
    print('Girilen sayi tektir.')
else:
    print('Yanlis giris yapildi.')