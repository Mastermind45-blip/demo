jumlah_bilangan = int(input("masukan jumlah bilangan: "))
n = 0
total = 0
while n < jumlah_bilangan:
    bilangan = int(input(f"masukan bilangan {n+1}: "))
    n += 1
    total += bilangan
    result = total / jumlah_bilangan
    
print('hasilnya adalah', result)