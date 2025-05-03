##################################################
def not_hesapla(satır):
    satır=satır.strip()
    try:
        liste=satır.split(":")
        öğrenci_adı=liste[0]
        notlar=liste[1].split(",")
        not1,not2,not3=map(int,notlar)
        ortalama=(not1+not2+not3)/3

        if 90<=ortalama<=100:
            harf="AA"
        elif 85<ortalama<=89:
            harf="BA"
        elif 80<=ortalama<=84:
            harf="BB"
        elif 75<=ortalama<=79:
            harf="CB"
        elif 70<=ortalama<=74:
            harf="CC"
        elif 65<=ortalama<=69:
            harf="DC"
        elif 60<=ortalama<=64:
            harf="DD"
        elif 50<=ortalama<=59:
            harf="FD"
        else:
            harf="FF"

        return f"{öğrenci_adı}: {harf}\n"

    except (ValueError, IndexError):
        return f"Hatalı satır: {satır}\n"
##################################################
def ortalamaları_oku():
    try:
        with open("sınav_notları.txt","r",encoding="utf-8") as file:
            for satır in file:
                print(not_hesapla(satır))
                print("-----------------------------------")
    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen 'sınav_notları.txt' dosyasını oluşturun.")
print("-----------------------------------")
##################################################
def not_gir():
    ad=input("Ad Girin : ").strip()
    soyad=input("Soyad Girin : ").strip()
    try:
        not1=int(input("1. Notu Girin (0-100): ").strip())
        not2=int(input("2. Notu Girin (0-100): ").strip())
        not3=int(input("3. Notu Girin (0-100): ").strip())
        if not (0<=not1<=100 and 0<=not2<=100 and 0<=not3<=100):
            raise ValueError("Notlar 0 ile 100 arasında olmalıdır.")
        print("-----------------------------------")
        with open("sınav_notları.txt","a",encoding="utf-8") as file:
            file.write(f"{ad} {soyad}:{not1},{not2},{not3}\n")
        print("Not başarıyla kaydedildi!")
    except ValueError as e:
        print(f"Hatalı giriş: {e}")
print("-----------------------------------")
##################################################
def notları_kaydet():
    try:
        with open("sınav_notları.txt","r",encoding="utf-8") as file:
            liste=[not_hesapla(i) for i in file]
        with open("sonuçlar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)
        print("Notlar başarıyla 'sonuçlar.txt' dosyasına kaydedildi!")
    except FileNotFoundError:
        print("Dosya bulunamadı. Lütfen 'sınav_notları.txt' dosyasını oluşturun.")
    print("-----------------------------------")
##################################################
while True:
    try:
        işlem=int(input("1-Notları Oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Çıkış\n\nSeçim Yapın : ").strip())
        print("-----------------------------------")
        if işlem==1:
            ortalamaları_oku()
        elif işlem==2:
            not_gir()
        elif işlem==3:
            notları_kaydet()
        elif işlem==4:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.Lütfen 1-4 arasında bir değer girin.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
    print("-----------------------------------")
