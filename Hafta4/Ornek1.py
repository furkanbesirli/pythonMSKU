#Hafta 4 Ornek 1


sayi1 = int(input('1. sayiyi giriniz: '))
sayi2 = int(input('2. sayiyi giriniz: '))
toplam = 0
if sayi1 > sayi2:
    for i in range(sayi1-1,sayi2,-1):
        toplam += i
    print('Sayilarin toplami: ',toplam)
elif sayi2 > sayi1:
    for i in range(sayi2-1,sayi1,-1):
        toplam += i
    print('Aradaki sayilarin toplami: ',toplam)
else:
    print('Sayilar esit.')