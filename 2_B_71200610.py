loop = 0
x = 0
nomor = ""
kalimat = ""
teks = ""
while loop == 0:
    nama = input("Masukkan nama : ")
    if nama == "STOP":
        loop = 1
    else :
        kursi = input ("Masukkan nomor kursi "+nama+" : ")
        x = x + 1
        if kursi in nomor:
            print ("Mohon maaf kursi tersebut telah terisi!")
        else:
            kalimat = "Kursi nomor "+kursi+" telah diisi oleh "+nama   
            nomor = nomor+kursi     
            teks = teks + kalimat + "\n"
else:
    print("\nList kursi yang telah terisi :")
    print (teks)