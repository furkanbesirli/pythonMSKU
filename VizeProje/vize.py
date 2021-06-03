print("Magazamiza Hos Geldiniz...")


aksiyonListesi = {
    "Maneater": 61,
    "Biomutant": 300,
    "Soulworker": 10,
    "Sea of Thieves": 60,
    "RONIN Two Souls": 20,
    "Yakuza": 60,
    "Graven": 60,
    "Riftdrifter": 10,
    "The Black Hole": 32,
    "Lost Souls": 14,

}
sporListesi = {
    "CryoFall": 18,
    "Ranch": 40,
    "Torque Drift": 0,
    "SlappyBall": 0,
    "F1 2020": 50,
    "Dirt 5": 92,
    "NBA 2K2021": 400,
    "Skate City": 25,
    "Descenders": 25,
    "FIFA 21": 400,
}
simulasyonListesi = {
    "Powerwash Simulator": 50,
    "SnowRunner": 150,
    "Al Drone Simulator": 45,
    "Vivid Knight": 25,
    "Farm Manager 2021": 32,
    "Imagine Earth": 40,
    "Tennis Manager 2021": 69,
    "MotoGp21": 53,
    "Jetborne Racing": 18,
    "Operator": 2,
}

satinAl = 0
sepeteEkle = 0

def odemeYap():
    satisDosyasi = open("C:/Users/user/Desktop/sayisDosyasi.txt", "w")
    print("Odeme bolumune hosgeldiniz!")
    name = input("Isim : ")
    surname = input("Soyisim : ")
    address = input("Adress : ")
    tel = input("Telefon No : ")
    kart = input("Kart No :")

    satisDosyasi.write(name)
    satisDosyasi.write(surname)
    satisDosyasi.write(address)
    satisDosyasi.write(tel)
    satisDosyasi.write(kart)
    satisDosyasi.write(str(sepeteEkle))
    print("Odeme isleminiz tamamlandi. Tesekkur ederiz.")


while satinAl == 0:
    listeSec = int(input("Lutfen incelemek istegidiniz listeyi seciniz...0 = Aksiyon 1 = Spor 2 = Simulasyon"))

    if listeSec == 0:
        print(aksiyonListesi.items())
        oyunNo = int(input("Lutfen sepete eklemek istediginiz urun numarasini giriniz..."))

        if oyunNo == 1:
            print("Maneater oyunu sepete eklendi...")
            sepeteEkle += 61
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1

        elif oyunNo == 2:
            print("Biomutant oyunu sepete eklendi...")
            sepeteEkle += 300
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1

        elif oyunNo == 3:
            print("Soulworker oyunu sepete eklendi...")
            sepeteEkle += 10
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1

        elif oyunNo == 4:
            print("Sea of Thieves oyunu sepete eklendi... ")
            sepeteEkle += 60
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1

        elif oyunNo == 5:
            ("RONIN Two Souls oyunu sepete eklendi... ")
            sepeteEkle += 20
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1

        elif oyunNo == 6:
            ("Yakuza oyunu sepete eklendi... ")
            sepeteEkle += 60
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1

        elif oyunNo == 7:
            ("Graven oyunu sepete eklendi... ")
            sepeteEkle += 60
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1

        elif oyunNo == 8:
            ("Riftdrifter oyunu sepete eklendi... ")
            sepeteEkle += 10
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1

        elif oyunNo == 9:
            ("The Black Hole oyunu sepete eklendi... ")
            sepeteEkle += 32
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1

        elif oyunNo == 10:
            ("Lost Souls oyunu sepete eklendi... ")
            sepeteEkle += 14
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz 2 tusuna basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            elif devam == 2:
                print("Sepet tutarinizi onayliyor musunuz? : " + str(sepeteEkle))
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeYap()
                    satinAl = 1
                else:
                    satinAl = 1
            else:
                print("Yanlis giris yapildi.")
                satinAl = 1
        else:
            print("Gecersiz giris yaptiniz...!")
"""
    elif listeSec == 1:
        print(sporListesi.items())
        oyunNo = int(input("Lutfen sepete eklemek istediginiz urun numarasini giriniz..."))

        if oyunNo == 1:
            print("CryoFall oyunu sepete eklendi...")
            sepeteEkle += 18
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 2:
            print("Ranch oyunu sepete eklendi...")
            sepeteEkle += 40
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 3:
            print("Torque Drift oyunu sepete eklendi...")
            sepeteEkle += 0
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1


        elif oyunNo == 4:
            print("SlappyBall oyunu sepete eklendi... ")
            sepeteEkle += 0
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 5:
            ("F1 2020 oyunu sepete eklendi... ")
            sepeteEkle += 50
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 6:
            ("Dirt 5 oyunu sepete eklendi... ")
            sepeteEkle += 60
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 92:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 7:
            ("NBA 2K21 oyunu sepete eklendi... ")
            sepeteEkle += 400
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 8:
            ("Skate City oyunu sepete eklendi... ")
            sepeteEkle += 25
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1


        elif oyunNo == 9:
            ("Descenders oyunu sepete eklendi... ")
            sepeteEkle += 25
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1


        elif oyunNo == 10:
            ("FIFA 21 oyunu sepete eklendi... ")
            sepeteEkle += 400
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1
        else:
            print("Gecersiz giris yaptiniz...!")

    elif listeSec == 2:
        print(simulasyonListesi.items())
        oyunNo = int(input("Lutfen sepete eklemek istediginiz urun numarasini giriniz..."))
        if oyunNo == 1:
            print("Powerwash Simulator oyunu sepete eklendi...")
            sepeteEkle += 50
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 2:
            print("SnowRunner oyunu sepete eklendi...")
            sepeteEkle += 150
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 3:
            print("Al Drone Simulator oyunu sepete eklendi...")
            sepeteEkle += 45
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1


        elif oyunNo == 4:
            print("Vivid Knight oyunu sepete eklendi... ")
            sepeteEkle += 25
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 5:
            ("Farm Manager 2021 oyunu sepete eklendi... ")
            sepeteEkle += 32
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 6:
            ("Imagine Earth oyunu sepete eklendi... ")
            sepeteEkle += 40
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 92:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 7:
            ("Tennis Manager 2021 oyunu sepete eklendi... ")
            sepeteEkle += 69
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        elif oyunNo == 8:
            ("MotoGp21 oyunu sepete eklendi... ")
            sepeteEkle += 53
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1


        elif oyunNo == 9:
            ("Jetborne Racing oyunu sepete eklendi... ")
            sepeteEkle += 18
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1


        elif oyunNo == 10:
            ("Operator oyunu sepete eklendi... ")
            sepeteEkle += 2
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("Sepet tutarinizi onayliyor musunuz? : " + sepeteEkle)
                onay = int(input("Onaylamak icin 1 e basiniz..."))
                if onay == 1:
                    odemeler.odemeYap()
                else:
                    satinAl = 1

        else:
            print("Gecersiz giris yaptiniz...!")

    else:
        print("Program kapatiliyor. Gecerli bir liste secmediniz..!")
        satinAl = 1
"""
