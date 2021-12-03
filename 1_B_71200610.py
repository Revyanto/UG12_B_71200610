angka = int(input("Masukkan banyak bilangan: "))
total = 0
kalimat = "total ="
for i in range (1,angka+1) :
    if i % 7 == 0:
        jumlah = " + 0"
        total = total + 0
    elif i % 3 == 0:
        jumlah = " - "+str(i)
        total = total + (i*-1)
    elif i == 1:
        jumlah = " 1"
        total = total + i
    else:
        jumlah = " + "+str(i)
        total = total + i
    kalimat = kalimat + jumlah
print (kalimat)
print ("Hasil perhitungan diatas ialah",total)