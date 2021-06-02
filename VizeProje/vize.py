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
while satinAl == 0:
    listeSec = int(input("Lutfen incelemek istegidiniz listeyi seciniz...0 = Aksiyon 1 = Spor 2 = Simulasyon"))

    if listeSec == 0:
        print(aksiyonListesi.items())
        oyunNo = int(input("Lutfen sepete eklemek istediginiz urun numarasini giriniz..."))

        if oyunNo == 1:
            print("Maneater oyunu sepete eklendi...")
            sepeteEkle += 61
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("fonkyiyon")

        elif oyunNo == 2:
            print("Biomutant oyunu sepete eklendi...")
            sepeteEkle += 300
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("fonkyiyon")

        elif oyunNo == 3:
            print("Soulworker oyunu sepete eklendi...")
            sepeteEkle += 10
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("fonkyiyon")


        elif oyunNo == 4:
            print("Sea of Thieves oyunu sepete eklendi... ")
            sepeteEkle += 60
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("fonkyiyon")

        elif oyunNo == 5:
            ("RONIN Two Souls oyunu sepete eklendi... ")
            sepeteEkle += 20
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("fonkyiyon")

        elif oyunNo == 6:
            ("Yakuza oyunu sepete eklendi... ")
            sepeteEkle += 60
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("fonkyiyon")

        elif oyunNo == 7:
            ("Graven oyunu sepete eklendi... ")
            sepeteEkle += 60
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("fonkyiyon")

        elif oyunNo == 8:
            ("Riftdrifter oyunu sepete eklendi... ")
            sepeteEkle += 10
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("fonkyiyon")

        elif oyunNo == 9:
            ("The Black Hole oyunu sepete eklendi... ")
            sepeteEkle += 32
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("fonkyiyon")
            else:
                print("Liste bolumune yonlendiriliyor...")

        elif oyunNo == 10:
            ("Lost Souls oyunu sepete eklendi... ")
            sepeteEkle += 14
            devam = int(input("Farkli oyun incelemek istiyorsaniz 1 e, istemiyorsaniz farkli bir tusa basiniz..."))
            if devam == 1:
                print("Liste bolumune yonlendiriliyor...")
            else:
                print("fonkyiyon")







    else:
        print("Program kapatiliyor. Gecerli bir liste secmediniz..!")
        satinAl = 1


def odemeYap():
    satisDosyasi = open("C:/Users/user/Desktop/sayisDosyasi.txt", "w")
