def harf_notu_belirle(ort_not):
    if ort_not>90:
        harf_not="AA"
    elif ort_not>85:
        harf_not="BA"
    elif ort_not>80:
        harf_not="BB"
    elif ort_not>75:
        harf_not="CB"
    elif ort_not>70:
        harf_not="CC"
    elif ort_not>65:
        harf_not="DC"
    elif ort_not>60:
        harf_not="DD"
    else:
        harf_not="FF"
    return harf_not
def analiz_et(liste):
    sinif_top = sum(ogrenci["Ortalama"] for ogrenci in liste.values())
    sinif_ort = sinif_top/len(liste)
    en_dusuk = min(liste.values(), key=lambda x: x["Ortalama"])
    en_yuksek = max(liste.values(), key=lambda x: x["Ortalama"])
    print(f"Sınıf Ortalaması: {sinif_ort}")
    print(f"En düşük ortalamalı öğrenci: {en_dusuk['İsim']} {en_dusuk['Soyisim']}, Ortalama: {en_dusuk['Ortalama']}")
    print(f"En yüksek ortalamalı öğrenci: {en_yuksek['İsim']} {en_yuksek['Soyisim']}, Ortalama: {en_yuksek['Ortalama']}")
def ogrenci_analiz_sistemi():
    ogrenci_listesi = {}
    sayac = 0
    while True:
        if len(ogrenci_listesi) >= 5:
            print(f"{len(ogrenci_listesi)} sayıda öğrenci girdiniz. 'bitir' yazarak programdan çıkabilirsiniz.")
        else:
            print(f"{5-len(ogrenci_listesi)} kadar daha öğrenci girmeniz gerekmektedir.")
        
        isim = input("İsim (bitirmek için 'bitir' yazınız.): ").lower()
        if isim == "bitir":
            if len(ogrenci_listesi) >= 5:
                break
            else:
                print(f"{5-len(ogrenci_listesi)} kadar daha öğrenci girmeniz gerekmektedir.")
                continue
        isim = isim.title()
        soyisim = input("Soyisim: ")
        notlar = {}
        sinavlar = ["vize_1", "vize_2", "final"]
        for sinav in sinavlar:
            while True:
                try:
                    _not = int(input(f"{sinav} notu: "))
                    if 0 <= _not <= 100:
                        notlar[sinav] = _not
                        break
                    else:
                        print("Not 0-100 aralığında bir tam sayı olmalıdır.")
                except ValueError:
                    print("Not 0-100 aralığında bir tam sayı olmalıdır.")
        
        ortalama = notlar["vize_1"]*0.2 + notlar["vize_2"]*0.2 + notlar["final"]*0.6
        harf_notu = harf_notu_belirle(ortalama)
        ogrenci_no = sayac+1
        
        ogrenci = {
            "İsim": isim,
            "Soyisim": soyisim,
            "Notlar": notlar,
            "Ortalama": ortalama,
            "Harf Notu": harf_notu
        }       
        ogrenci_listesi[ogrenci_no] = ogrenci
        sayac += 1
    
    analiz_et(ogrenci_listesi)

ogrenci_analiz_sistemi()