### Soru 1_cozumu ###

gorevler= []
gorev_numarasi_artir = 1
gorev_durum= ["Başarili", "Beklemede", "Silindi"]

def gorev_liste():
    print("\nTüm Görevler:")
    if not gorevler:
        print("Henüz hiç görev eklenmemiş.")
    else:
        for gorev in gorevler:
            print(f"{gorev['Sira Numarasi']}: {gorev['Görevin Adi']} ({gorev_durum[gorev['Durumu']]})")

def gorev_tamamlanan_liste():
    gorev_liste()
    tamamlan_gorev = [gorev for gorev in gorevler if gorev["Durumu"] == 0]
    print("\nTamamlanmiş Görevler:")
    for gorev in tamamlan_gorev:
        print(f"{gorev['Sira Numarasi']}: {gorev['Görevin Adi']} ({gorev_durum[gorev['Durumu']]})")

def gorev_ekle():
    global gorev_numarasi_artir
    gorev_adi = input("Yeni görevin adini girin: ")
    gorev = {
        "Sira Numarasi": gorev_numarasi_artir,
        "Görevin Adi": gorev_adi,
        "Durumu": 1  
    }
    gorevler.append(gorev)
    gorev_numarasi_artir += 1
    print("Yeni görev eklendi: ", gorev_adi)


def gorev_tamamla():
    gorev_liste()
    gorev_numarasi = int(input("Tamamlanan görevin sira numarasini girin: "))
    for gorev in gorevler:
        if gorev["Sira Numarasi"] == gorev_numarasi:
            gorev["Durumu"] = 0  
            print("Görev tamamlandi.")
            return
    print("Sira numarasi bulunamadi.")


def gorev_sil():
    gorev_liste()
    global gorev_numarasi_artir   
    gorev_numarasi= int(input("Silinecek görevin numarasini girin: "))
    for gorev in gorevler:
        if gorev["Sira Numarasi"] == gorev_numarasi:
            gorevler.remove(gorev)

            for i, gorev in enumerate(gorevler):
                gorev['Sira Numarasi'] = i + 1
            print(gorev_numarasi , " numarali  Görev silindi. ")
    gorev_numarasi_artir = gorev_numarasi_artir - 1 
  
while True:
    print("\nGörev Yöneticisi Uygulamasi")
    print("1. Yeni Görev Ekle")
    print("2. Görevi Tamamla")
    print("3. Görevi Sil")
    print("4. Tamamlanan Görevleri Listele")
    print("5. Tüm Görevleri Listele")
    print("6. Cikiş")
    secim = input("Seciminizi girin: ")

    if secim == "1":
        gorev_ekle()
    elif secim == "2":
        gorev_tamamla()
    elif secim == "3":
        gorev_sil()
    elif secim == "4":
        gorev_tamamlanan_liste()
    elif secim== "5":
        gorev_liste()
    elif secim == "6":
        print("Uygulamadan cikiliyor")
        break
    else:
        print("Geçersiz seçenek, tekrar deneyin.")






###Hackerrank_Find_Digits ###
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def findDigits(n):
    count = 0
    for i in str(n):
        if int(i) != 0 and n%int(i) == 0:
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)
        fptr.write(str(result) + '\n')
    fptr.close()



###Hackerrank_capitalize###

#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    a = ' '.join([i.capitalize() for i in s.split(' ')])
    return a   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()




