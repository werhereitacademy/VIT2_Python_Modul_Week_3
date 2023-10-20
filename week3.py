gorevler = []
import os
sira_numarasi=1

def gorev_ekle():
    global sira_numarasi
    #Gorevler listesinin 1 den fazla elemani oldugunda sira numarasini belirleyecek algoritma
    if len(gorevler):# Eger gorevler listesi bos degil ise demek
        for i in range(1,max(gorev["Sıra Numarası"] for gorev in gorevler) + 2): # 1 den max gorev sirasina kadar bakacak . 
            # Arada silinmis numara varsa yeni sira numarasini o siraya atayacak . 
            # silinmis sira numarasi yoksa max sira numarasinin 1 ustunu sira numarasi olarak atayacak
            if i not in (gorev["Sıra Numarası"] for gorev in gorevler):
                sira_numarasi = i 
                break  
    gorev_adi = input("Yeni görev adını girin: ")
    yeni_gorev = {"Sıra Numarası": sira_numarasi, "Görev Adı": gorev_adi, "Durumu": "Beklemede"}
    gorevler.append(yeni_gorev)
    print(f"'{gorev_adi}' başlıklı görev (sıra {sira_numarasi}) eklendi.")
    sira_numarasi = max(gorev["Sıra Numarası"] for gorev in gorevler) + 1



def gorev_tamamla():
    tamamlanmamis_gorevleri_listele()
    sira_numarasi = int(input("Tamamlanan görevin sıra numarasını girin: "))
    for gorev in gorevler:
        if gorev["Sıra Numarası"] == sira_numarasi:
            gorev["Durumu"] = "Başarılı"
            print(f"'{gorev['Görev Adı']}' başlıklı görev (sıra {sira_numarasi}) başarıyla tamamlandı.")
            break
    else:
        print("Belirtilen sıra numarasına sahip görev bulunamadı.")

def gorev_sil():
    global sira_numarasi
    tamamlanmamis_gorevleri_listele()
    tamamlanmis_gorevleri_listele()
    sira_numarasi = int(input("Silinecek görevin sıra numarasını girin: "))
    for gorev in gorevler:
        if gorev["Sıra Numarası"] == sira_numarasi:
            gorevler.remove(gorev)
            print(f"'{gorev['Görev Adı']}' başlıklı görev (sıra {sira_numarasi}) silindi.")
            break
    else:
        print("Belirtilen sıra numarasına sahip görev bulunamadı.")

def tamamlanmis_gorevleri_listele():
    print("\nTamamlanmış Görevler:")
    sirali_gorevler = sorted(gorevler, key=lambda x: x["Sıra Numarası"])
    for gorev in sirali_gorevler:
        if gorev["Durumu"] == "Başarılı":
            print(f"{gorev['Sıra Numarası']}. {gorev['Görev Adı']}")

def tamamlanmamis_gorevleri_listele():
    print("\nTamamlanmamış Görevler:")
    sirali_gorevler = sorted(gorevler, key=lambda x: x["Sıra Numarası"])
    for gorev in sirali_gorevler:
        if gorev["Durumu"] == "Beklemede":
            print(f"{gorev['Sıra Numarası']}. {gorev['Görev Adı']} {gorev['Durumu']}")


while True:
    print("\nGörev Yöneticisi")
    print("1. Görev Ekle")
    print("2. Görev Tamamla")
    print("3. Görev Sil")
    print("4. Tamamlanmış Görevleri Listele")
    print("5. Tamamlanmamış Görevleri Listele")
    print("6. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5/6): ")
    os.system('cls')

    if secim == '1':
        gorev_ekle()
    elif secim == '2':
        gorev_tamamla()
    elif secim == '3':
        gorev_sil()
    elif secim == '4':
        tamamlanmis_gorevleri_listele()
    elif secim == '5':
        tamamlanmamis_gorevleri_listele()
    elif secim == '6':
        print("Görev yöneticisi uygulamasından çıkılıyor.")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
