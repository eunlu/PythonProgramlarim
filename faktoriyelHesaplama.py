# -- coding: cp1254 --

#--------------------------------------------------------------
# @Yazar     : Erkan �nl�
# @Proje Ad� : Programlar
# @Dosya Ad� : faktoriyelHesaplama.py
# @Zaman     : 26.12.2017 17:37
# @Lisans    : GNU/GPLv3
# -------------------------------------------------------------
# Normal fonksiyonla hesaplama
def fakt1(n):
    fakt = 1

    for x in range(1, n + 1):
        fakt *= x
    print n, "!=1x2x3...", n, "=", fakt
    print "x=", x
# recursive fonksiyon olarak hesaplayal�m
def fakt2(n):
    if n==1:
        return 1
    else:
        return n*fakt2(n-1)

sayi = input("Faktoriyelini hesaplatmak istedi�iniz say�y� girin: ")
print fakt1(sayi)
#sayi = input("Faktoriyelini hesaplatmak istedi�iniz say�y� girin: ")
print fakt2(sayi)