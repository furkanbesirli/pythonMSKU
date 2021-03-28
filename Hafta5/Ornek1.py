#Metnin a harflerini buyuk yap ve * 'lari virgule cevir

metin = 'Manavdan elma* greyfurt* kavun* marul* biber* mantar almis.'
metin = metin.replace("a","A")
print(metin)
metin = metin.split("*")
print(metin)