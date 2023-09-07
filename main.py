import random

kitaplar = {
    "Klasik Edebiyat": ["Madame Bovary", "Savaş ve Barış", "Suç ve Ceza", "Gönülçelen"],
    "Bilim Kurgu": ["Dune", "Yıldız Gemisi Askerleri", "Vakıf", "Yaban", "Doktor Uyku"],
    "Polisiye": ["Sherlock Holmes", "Agatha Christie Kitapları", "Kızıl Dosya", "Sherlock Holmes'un Dönüşü"],
    "Bilim": ["Einstein'ın Rüyaları", "Evrenin Kısa Tarihi", "Büyük Tasarım"],
    "Tarih": ["Sapiens", "İkinci Dünya Savaşı", "Ottoman Empire", "Tarihte İlginç Olaylar"],
    "Romantik": ["Aşk ve Gurur", "Gone with the Wind", "Aşk Romanları"],
    "Korku": ["Dracula", "Frankenstein", "Kırmızı Odanın Gizemi"],
    "Fantastik": ["Harry Potter", "Yüzüklerin Efendisi", "Percy Jackson Serisi"],
    "Felsefe": ["Sokrates'in Savunması", "Varlık ve Zaman", "Ahlakın Eleştirisi"]
}

print("Lütfen aşağıdakileri büyük harflere dikkat ederek ve sadece 1 tane giriniz:")
for ilgi_alani in kitaplar.keys():
    print(ilgi_alani)

secilen_ilgi_alan = input("Hangi ilgi alanını seçmek istersiniz?: ")

# Kullanıcının birden fazla ilgi alanı seçmesini engelleyin
secilen_ilgi_alanlar = secilen_ilgi_alan.strip().split(",")
if len(secilen_ilgi_alanlar) != 1:
    print("Lütfen yalnızca bir ilgi alanı seçin!")
else:
    secilen_ilgi_alani = secilen_ilgi_alanlar[0]
    if secilen_ilgi_alani in kitaplar:
        kitap_listesi = kitaplar[secilen_ilgi_alani]
        onerilen_kitap = random.choice(kitap_listesi)
        print(f"{secilen_ilgi_alani} kategorisinden size önerilen kitap: {onerilen_kitap}")
    else:
        print("Geçerli bir ilgi alanı seçmediniz!!!")
