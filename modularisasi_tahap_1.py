"""
Program menghitung luas segitiga
luas_segitiga = al * tinggi/2
"""
def luas_segitiga(alas,tinggi):
    hitung_luas = alas * tinggi/2
    return hitung_luas
print(f'luas segitiga adalah {luas_segitiga(6,8)}')
alas = 7
tinggi = 12
print(f'alas = {alas}, tinggi = {tinggi} jadi Luas Segitiga Adalah {luas_segitiga(alas,tinggi)}')