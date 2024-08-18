import random

def tas_kagit_makas_BERRU_ERDOGAN():
  
  print("Taş, kağıt, makas oyununa hoş geldiniz.\nBu oyun iki kişilik bir oyundur.\nBu oyunu bilgisayara karşı oynayacaksın.\nTaş makası, makas kağıdı, kağıt da taşı yener.\nAynı seceneği seçerseniz beraberlik olur.")

  secenekler = ["taş", "kağıt", "makas"]
  oyun_devam_ediyor = True
  oynanan_oyun_sayısı = 1
  oyuncu_galibiyeti = 0
  pc_galibiyeti = 0
  
  while oyun_devam_ediyor:
    tur = 1
    pc_skor = 0
    kullanici_skor = 0
    
    print("OYUN - ", oynanan_oyun_sayısı)
      
    while True:
        pc_secimi = random.choice(secenekler)
        print("TUR - ", tur)
        print("Bilgisayar seçimini yaptı. Sıra sende!")
        secim = input("Taş, kağıt veya makas seç: ").lower()
        if secim not in secenekler:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            continue
        
        tur += 1

        print(f"Bilgisayar: {pc_secimi}")
        print(f"Sen: {secim}")
        if pc_secimi == secim:
            print("Berabere!")
        elif (pc_secimi == "taş" and secim == "makas") or \
            (pc_secimi == "kağıt" and secim == "taş") or \
            (pc_secimi == "makas" and secim == "kağıt"):
            print("Bilgisayar kazandı!")
            pc_skor +=1
        else:
            print("Sen kazandın!")
            kullanici_skor +=1

        print("Kullanıcı skoru: ",kullanici_skor)
        print("Bilgisayar skoru : ", pc_skor)
        
        if pc_skor == 2 or kullanici_skor == 2:
            if pc_skor == 2:
                pc_galibiyeti += 1
                print("OYUNU BİLGİSAYAR KAZANDI")
            if (kullanici_skor == 2):
                oyuncu_galibiyeti += 1
                print("OYUNU SEN KAZANDIN")
            print("OYUNCU GALİBİYETİ: ", oyuncu_galibiyeti)
            print("BİLGİSAYAR GALİBİYETİ: ", pc_galibiyeti)
            break
    
    pc_devam = random.choice([True,False])  
    kullanici_devam = input("Yeni bir oyun oynamak istiyor musunuz? Evet is e, hayır ise h yazınız: ").lower()
    while kullanici_devam != "e" and kullanici_devam != "h":
        print("Geçersiz cevap yazdınız!")
        kullanici_devam = input("Yeni bir oyun oynamak istiyor musunuz? Evet is e, hayır ise h yazınız: ").lower()

    if pc_devam == False or kullanici_devam == "h":
        if pc_devam == False:
            print("bilgisayar oyuna devam etmek istemiyor :(")
        if kullanici_devam == "h":
            print("Oynadığınız için teşekkürler :)")
        print("OYUN BİTTİ")
        oyun_devam_ediyor = False
        
    if pc_devam== True and kullanici_devam == "e":
        oynanan_oyun_sayısı += 1
        print("Bilgisayar da devam etmek istiyor. Haydi oynayalım :)")
        
       

tas_kagit_makas_BERRU_ERDOGAN()

