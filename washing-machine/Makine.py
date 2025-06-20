import time
import platform
import sys
import pygame 

programlar = {
    "Karişik 30°C": {"tişört", "şort", "çorap", "bluz", "iç çamaşirlar", "polar", "kazak", "pijama", "pantolon", "kaban", "eşofman", "mont"},
    "Yünlü 30°C": {"kazak", "hirka", "polar", "yorgan", "kaban"},
    "Pamuklu 60°C": {"gömlek", "tişört", "iç çamaşirlar", "çorap", "pantolon", "pijama", "pamuklu eşofman", "havlu"},
    "Sentetik 40°C": {"sweatshirt", "şort", "bluz", "gömlek"},
    "Diş Giyim 30°C": {"mont", "yağmurluk"},
    "Hizli 30dk 30°C": {"tişört", "şort", "çorap", "polar", "kazak", "pantolon", "pijama", "eşofman"},
    "Eco 40°C": {"gömlek", "tişört", "polar", "hirka", "polar", "çorap", "kazak", "pijama", "pantolon"}
}

tum_kiyafetler = set()
for kiyafet_seti in programlar.values():
    tum_kiyafetler.update(kiyafet_seti)

def tik_sesi_dosyadan():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("mardin.mp3")  
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            time.sleep(0.1)
        print(" TIK, Kapak açildi.")
    except:
        print(" Ses dosyasi çalinamadi. (mardin.mp3 bulundu mu?)")

def yikama_baslat_kullanicidan_sure():
    try:
        dakika = int(input("Program süresi kaç dakika sürecek?: "))
        if dakika <= 0:
            print("Süre pozitif bir sayi olmali.")
            return
    except ValueError:
        print("Geçersiz giriş. Lütfen sayi girin.")
        return

    print("Makine çalişiyor, kapak kilitlendi.")
    toplam_saniye = dakika * 60
    for kalan in range(toplam_saniye, 0, -1):
        dakika_goster = kalan // 60
        saniye_goster = kalan % 60
        print(f"Yikama sürüyor... {dakika_goster:02d}:{saniye_goster:02d}", end="\r")
        time.sleep(1)

    print("\n Yikama tamamlandi.")
    tik_sesi_dosyadan()

def ana_program():
    try:
        adet = int(input("Kaç kiyafet atacaksiniz? (5-10 arasi): "))
        if adet < 5 or adet > 10:
            print("5 ile 10 arasinda kiyafet seçmelisiniz.")
            sys.exit()
    except ValueError:
        print("Lütfen geçerli bir sayi girin.")
        sys.exit()

    print("\n Seçilebilecek kiyafetler:")
    print(", ".join(sorted(tum_kiyafetler)))

    secimler = []
    for i in range(adet):
        kiyafet = input(f"{i+1}. kiyafet: ").strip().lower()
        if kiyafet not in tum_kiyafetler:
            print("Geçersiz kiyafet seçildi!")
            sys.exit()
        secimler.append(kiyafet)

    uygun_programlar = []
    for program_adi, grup in programlar.items():
        if all(k in grup for k in secimler):
            uygun_programlar.append(program_adi)

    print("\nSeçilen kiyafetler:", ", ".join(secimler))

    if uygun_programlar:
        print(" Ortak programlar bulundu:")
        for p in uygun_programlar:
            print(f" - {p}")
        input("\n Makineyi başlatmak için Enter'a basin...")
        yikama_baslat_kullanicidan_sure()
    else:
        print(" Seçtiğiniz kiyafetler ortak bir programda yikanamaz.")

ana_program()
