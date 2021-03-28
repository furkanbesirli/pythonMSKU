#Hafta 3 Ornek 1

username = input('Kullanici adi giriniz: ')
password = input('Sifre giriniz: ')

uzunluk = len(username) + len(password)
print('Bilgileriniziz toplam karakter sayisi: {}'.format(uzunluk))

if uzunluk > 40:
    print("Kullanici adi ve parola toplam karakter sayisi 40'i gecmemelidir")
else:
    print('Sisteme girisiniz basariyla gerceklestirildi')