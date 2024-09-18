kursUSD = 0.000065
kursEUR = 0.00006
kursJPY = 0.0092

IDR = float(input("Masukkan Uang (rupiah) : "))

USD = IDR * kursUSD
EUR = IDR * kursEUR
JPY = IDR * kursJPY

print(f"{IDR} Rupiah setara dengan {USD:.3f} Dolar Amerika")