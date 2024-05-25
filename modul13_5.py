# Fungsi rekursif untuk menghitung kombinasi
def kombinasi (n, r):
    if r == 0 or r == n:
        return 1
    else:
        return kombinasi(n-1, r-1) + kombinasi(n-1, r)

print(kombinasi(5, 2))

