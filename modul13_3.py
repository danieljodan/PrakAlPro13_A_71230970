# Fungsi rekursif untuk menghitung jumlah deret ganjil
def deretGanjil(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 != 0:
        return n + deretGanjil(n-2) 
    else:
        return deretGanjil(n-1)
        
print(deretGanjil(10))

