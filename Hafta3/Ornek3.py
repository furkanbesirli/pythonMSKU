
#Hafta 3 Ornek 3


ogrenciNot1 = input("Lutfen 1. ders notunu giriniz: ")
ogrenciNot2 = input("Lutfen 2. ders notunu giriniz: ")
ortalama = (float(ogrenciNot1) + float(ogrenciNot2))/2

if ortalama >= 85 and ortalama <= 100:
    beslikNot = 5
    print("Ogrenci 5'lik sistem notu: {} ".format(beslikNot))
elif ortalama >= 70 and ortalama <= 84:
    beslikNot = 4
    print("Ogrenci 5'lik sistem notu: {} ".format(beslikNot))
elif ortalama >= 55 and ortalama <= 69:
    beslikNot = 3
    print("Ogrenci 5'lik sistem notu: {} ".format(beslikNot))
elif ortalama >= 45 and ortalama <= 54:
    beslikNot = 2
    print("Ogrenci 5'lik sistem notu: {} ".format(beslikNot))
elif ortalama >= 25 and ortalama <= 44:
    beslikNot = 1
    print("Ogrenci 5'lik sistem notu: {} ".format(beslikNot))
else:
    beslikNot = 0
    print("Ogrenci 5'lik sistem notu: {} ".format(beslikNot))

