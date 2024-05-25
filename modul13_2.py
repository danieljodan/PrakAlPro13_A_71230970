def palindrom(kalimat: str, counter: int = None):
    kalimat_lower = kalimat.lower()
    kalimat_alpha = [x for x in kalimat_lower if x.isalpha()]
    kalimat_bersih = "".join(kalimat_alpha)
    if counter is None:
        counter = len(kalimat_bersih)
    if counter <= 1:
        return True
    if kalimat_bersih[0] != kalimat_bersih[-1]:
        return False
    return palindrom(kalimat_bersih[1:-1], counter - 2)

print(palindrom("Katak."))

