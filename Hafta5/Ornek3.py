#Ad Soyad girisi al. Hafleri ayirip alfabetik sirala

name = input('Ad Giriniz: ')
surname = input('Soyad Giriniz: ')

sesliHarfler = "aeiou"
sessizHarfler = "bcdfghjklmnprstvyzx"
sesli = ""
sessiz = ""

for harf in name:
    if harf in sesliHarfler:
        if harf not in sesli:
            sesli += harf
    elif harf in sessizHarfler:
        if harf not in sessiz:
            sessiz += harf
for harf2 in surname:
    if harf2 in sesliHarfler:
        if harf2 not in sesli:
            sesli += harf2
    elif harf2 in sessizHarfler:
        if harf2 not in sessiz:
            sessiz += harf2

print(sorted(sesli))
print(sorted(sessiz))