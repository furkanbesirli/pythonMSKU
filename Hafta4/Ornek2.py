#Hafta 4 Ornek 2

dongu = 0
while dongu == 0:
    sayi = int(input('Sayi girisi yapiniz: '))
    if sayi > 9 and sayi < 16:
        dongu += 1
    else:
        print(sayi)