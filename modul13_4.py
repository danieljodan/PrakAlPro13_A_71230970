# Fungsi rekursif untuk mengetahui jumlah digit dari suatu bilangan
def digit(n = 0):
    n = int(n)
    if n == 0:
        return 0
    else:
        return n % 10 + digit(n // 10)      

print(digit("234"))


