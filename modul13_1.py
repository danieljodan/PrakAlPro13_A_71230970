# Rekursif Check Prima
def prima(n, i = 2):
    if n == 2:
        return True
    if n < 2 or n % i == 0:
        return False
    if i * i > n:
        return True

    return prima(n, i + 1)
        
print(prima(7))

