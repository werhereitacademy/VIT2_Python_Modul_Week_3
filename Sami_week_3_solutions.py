gorev_sozlugu = {}
gorev_no = 1

def gorev_ekle():
    global gorev_no  # Fonksiyon içindeki değişikliklerin global değişkeni etkilemesini sağlar.
    gorev_adi = input("Gorev Adini girin: ")
    gorev_durumu = input("Gorev Durumu girin: ")
    gorev_bilgileri = {
        'Gorev Adi': gorev_adi,
        'Gorev Durumu': gorev_durumu
    }
    gorev_sozlugu[gorev_no] = gorev_bilgileri
    print(f"{gorev_no} {gorev_adi} adlı gorev başarıyla eklenmiştir.")
    gorev_no += 1
# Müşteri bilgilerini güncellemek için bir fonksiyon tanımlayın
def gorev_guncelle():
    gorev_no = int(input("Güncellemek istediğiniz gorevin numarasini girin: "))
    if gorev_no in gorev_sozlugu:
        print(f"Mevcut Gorev Bilgileri:")
        for bilgi, deger in gorev_sozlugu[gorev_no].items():
            print(f"{bilgi}: {deger}")

        yeni_ad = input("Yeni gorev Adı (Değiştirmek istemiyorsanız boş bırakın): ")
        yeni_gorev_durumu = input("Yeni gorev durumu (Değiştirmek istemiyorsanız boş bırakın): ")

        if yeni_ad:
            gorev_sozlugu[gorev_no]['Gorev Adi'] = yeni_ad
        if yeni_gorev_durumu:
            gorev_sozlugu[gorev_no]['Gorev Durumu'] = yeni_gorev_durumu

        print("Gorev bilgileri başarıyla güncellendi.")
    else:
        print(f"{gorev_no} gorevi bulunamadı.")


# Gorev silmek için bir fonksiyon tanımlayın
def gorev_sil():
    gorev_no = int(input("Silmek istediğiniz gorevin nosunu girin: "))
    if gorev_no in gorev_sozlugu:
        del gorev_sozlugu[gorev_no]
        print(f"{gorev_no} gorevi başarıyla silindi.")
    else:
        print(f"{gorev_no} gorevi bulunamadı.")


# Tüm gorevleri listeleme işlemi
def gorevleri_listele():
    print("\nTüm Gorevler:")
    for gorev_no, gorev_bilgileri in gorev_sozlugu.items():
        print(f"Gorev No: {gorev_no}")
        for bilgi, deger in gorev_bilgileri.items():
            print(f"{bilgi}: {deger}")
        print("\n")
#gorevleri_listele = lambda: [print(f"Gorev No: {gorev_no}\n{bilgi}: {deger}\n") for gorev_no, gorev_bilgileri in gorev_sozlugu.items() for bilgi, deger in gorev_bilgileri.items()]

# Kullanım
gorevleri_listele()


# Ana döngü
while True:
    print("\nGorev Yönetim Sistemi")
    print("1. Gorev Ekle")
    print("2. Gorev Güncelle")
    print("3. Gorev Sil")
    print("4. Tüm Gorevleri Listele")
    print("5. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == '1':
        gorev_ekle()
    elif secim == '2':
        gorev_guncelle()
    elif secim == '3':
        gorev_sil()
    elif secim == '4':
        gorevleri_listele()
    elif secim == '5':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")


Soru1:Görev Yöneticisi Uygulaması
Proje Açıklaması: Bu ödevde, Python programlama dilini kullanarak bir görev yöneticisi uygulaması oluşturacaksınız.
Bu uygulama, kullanıcılara görevlerini eklemelerine, tamamlamalarına, silmelerine ve listelemelerine olanak tanır.

Gereksinimler:
1- Görevler, bir Python listesi içinde saklanacak ve her görev bir sözlük olarak temsil edilecektir.
Her görev aşağıdaki özelliklere sahip olmalıdır:
Sıra Numarası (Otomatik olarak atanmalıdır)
Görevin Adı
Durumu (Başarılı, Beklemede veya Silindi)
2- Kullanıcının yapabileceği işlemler:
Yeni bir görev ekle
Bir görevi tamamla???
Bir görevi sil
Tamamlanmış görevleri listele????????????????????????????????????????????????
Tüm görevleri durumları ile birlikte listele++++
Çıkış
3-Görevler, eklenme sırasına göre otomatik olarak sıra numarası almalıdır.
4-Yeni eklenecek görevler silinen görev numaralarının yerine kaydedilmelidir.???????????????????????????
5-Görevler listelenirken sıra numarasına göre sıralanmalıdır.+++++++
6-Kullanıcıya her işlem sonrasında uygun geri bildirimler verilmelidir.
Örneğin, yeni bir görev eklediğinde, görev eklenmiş olduğuna dair bir mesaj görmelidir.+++++
