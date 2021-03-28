#Hafta 3 Ornek 4


gun = input("Lutfen 1 ile 7 arasindan sayi giriniz: ")
gun = int(gun)

if gun == 1:
    print('Bugun gunlerden Pazartesi.')
elif gun == 2:
    print('Bugun gunlerden Sali')
elif gun == 3:
    print('Bugun gunlerden Carsamba')
elif gun == 4:
    print('Bugun gunlerden Persembe')
elif gun == 5:
    print('Bugun gunlerden Cuma')
elif gun == 6:
    print('Bugun gunlerden Cumartesi')
elif gun == 7:
    print('Bugun gunlerden Pazar')
else:
    print('Hatali sayi girisi yaptiniz.')
