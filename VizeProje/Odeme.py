def odemeYap():
    satisDosyasi = open("C:/Users/user/Desktop/sayisDosyasi.txt", "w")
    print("Odeme bolumune hosgeldiniz!")
    name = input("Isim : ")
    surname = input("Soyisim : ")
    address = input("Adress : ")
    tel = input("Telefon No : ")
    kart = input("Kart No :")

    satisDosyasi.write(name)
    satisDosyasi.write("\n")
    satisDosyasi.write(surname)
    satisDosyasi.write("\n")
    satisDosyasi.write(address)
    satisDosyasi.write("\n")
    satisDosyasi.write(tel)
    satisDosyasi.write("\n")
    satisDosyasi.write(kart)
    satisDosyasi.write("\n")
    satisDosyasi.write("Odeme isleminiz tamamlandi. Tesekkur ederiz.")



