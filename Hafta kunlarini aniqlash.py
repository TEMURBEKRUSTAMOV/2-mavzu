K = int(input("K kun sonini kiriting : "))
haftaKunlari = [ "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba","yakshanba"]
kun = 0  
kun += K -1
haftakuni = kun % 7
natija = haftaKunlari[haftakuni]
print(f"{K}-kun {natija}ga to'g'ri keladi.")
