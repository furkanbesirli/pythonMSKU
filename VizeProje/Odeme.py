def odemeYap():
    satisDosyasi = open("C:/Users/user/Desktop/sayisDosyasi.txt", "w")
    print("Odeme bolumune hosgeldiniz!")
    name = input("Isim : ")
    surname = input("Soyisim : ")
    address = input("Adress : ")
    tel = input("Telefon No : ")
    kart = input("Kart No :")

    satisDosyasi.write(name)
    print("\n")
    satisDosyasi.write(surname)
    print("\n")
    satisDosyasi.write(address)
    print("\n")
    satisDosyasi.write(tel)
    print("\n")
    satisDosyasi.write(kart)
    print("\n")
    satisDosyasi.write("Odeme isleminiz tamamlandi. Tesekkur ederiz.")



