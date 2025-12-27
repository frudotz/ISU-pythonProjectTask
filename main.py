# ISTINYE UNIVERSITESI - BILISIM GUVENLIGI TEKNOLOJISI
# PROGRAMLAMA TEMELLERI PROJESI - ADISYON UYGULAMASI
# 
# - @frudotz
# - @RFKaya
# 
# Bu programda:
# - Musteri siparis verebilir ve siparislerini gorebilir,
# - Isletme tum siparisleri gorebilir, iptal edebilir,
# - Gun sonu alinabilir.
#
# Bu program bir simulasyon olarak yazilmistir,

# Menü Verileri (Ürün ve Fiyat Grupları)
cigKofteMenusu = [
    ["Çiğ Köfte Dürüm", 80],
    ["Mega Çiğ Köfte Dürüm", 115],
    ["Porsiyon Çiğ Köfte", 200],
    ["Büyük Porsiyon Çiğ Köfte", 350],
    ["Ayran", 30],
    ["Kola", 50]
]

# Sipariş Veri Tabanı
tumSiparisler = []

# --- ANA SAYFA ---
def anaSayfa():
    while True:
        print("\n--- ARSAMİEA ÇİĞ KÖFTE OTOMASYONU ---")
        print("1. Müşteri Girişi")
        print("2. İşletme Girişi")
        print("3. Çıkış Yap")
        
        secim = input("Seçim: ")

        if secim == "1":
            musteriPaneli()
        elif secim == "2":
            isletmePaneli()
        elif secim == "3":
            break
        else:
            print("\nHatalı giriş yaptınız.")

# --- MÜŞTERİ PANELİ ---
def musteriPaneli():
    musteriAdi = input("Lütfen adınızı giriniz: ")
    
    while True:
        print(f"\n--- Hoş Geldin, {musteriAdi} ---")
        print("1. Sipariş Ver")
        print("2. Siparişlerimi Listele")
        print("3. Üst Menüye Dön")
        
        musteriSecimi = input("İşlem seçiniz: ")

        # Sipariş Verme İşlemi
        if musteriSecimi == "1":
            print("\n--- MENÜ ---")
            
            siraNo = 1
            for urun in cigKofteMenusu:
                print(f"{siraNo}. {urun[0]} - {urun[1]} TL")
                siraNo = siraNo + 1
            
            urunNo = input("\nAlmak istediğiniz ürünün numarası: ")
            
            # Menüde olmayan bir ürün tuşlanmaması için kontrol
            if 0 <= (int(urunNo) - 1) < len(cigKofteMenusu):
                # Seçilen ürünü listeden alıp siparişlere ekliyoruz
                secilen = cigKofteMenusu[int(urunNo) - 1]
                tumSiparisler.append([musteriAdi, secilen[0], secilen[1]])
                print(f"{secilen[0]} siparişiniz eklendi.")
            else:
                print("Hatalı seçim!")

        # Müşteri siparişleri listeleme
        elif musteriSecimi == "2":
            print(f"\n--- {musteriAdi} Siparişleri ---")
            for siparis in tumSiparisler:
                # Müşteriye ait siparişleri filtreler, başka müşterilerin siparişleri görüntülenmez
                if siparis[0] == musteriAdi:
                    print(f"- {siparis[1]}: {siparis[2]} TL")
        
        elif musteriSecimi == "3":
            break

# --- İŞLETME PANELİ ---
def isletmePaneli():
    while True:
        print("\n--- İŞLETME PANELİ ---")
        print("1. Tüm Siparişleri Görüntüle")
        print("2. Sipariş Sil")
        print("3. Gün Sonu Al")
        print("4. Üst Menüye Dön")
        
        isletmeSecimi = input("İşlem seçiniz: ")

        def siparisleriListele():
            print("\n--- TÜM SİPARİŞLER ---")

            # Siparişler varsa listele, yoksa uyarı ver
            if len(tumSiparisler):
                listeSira = 1
                for s in tumSiparisler:
                    print(f"{listeSira}. {s[0]} -> {s[1]}")
                    listeSira = listeSira + 1
            else:  
                print("Hiç sipariş yok.")

        # Tüm Siparişleri Görüntüle
        if isletmeSecimi == "1":
            siparisleriListele()
                

        # Sipariş Sil
        elif isletmeSecimi == "2":
            siparisleriListele()

            if len(tumSiparisler): 
                silNo = input("Silinecek sıra no: ")
                # Menüde olmayan bir siparişi silmeye çalışmasın diye kontrol
                if 0 <= (int(silNo) - 1) < len(tumSiparisler):
                    tumSiparisler.pop(int(silNo) - 1)
                    print("\nSipariş silindi.")
                else:
                    print("\nSipariş bulunamadı.")

        # Gün Sonu AL
        elif isletmeSecimi == "3":
            toplamCiro = 0
            for siparis in tumSiparisler:
                toplamCiro = toplamCiro + siparis[2]
            
            print(f"\nKasadaki Toplam: {toplamCiro} TL")

        elif isletmeSecimi == "4":
            break

# Programı Çalıştır
anaSayfa()