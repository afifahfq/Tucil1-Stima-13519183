# Nama : Afifah Fathimah Q
# NIM : 13519183
# Kelas : K-04

# PROGRAM PENYELESAIAN CRYPTARITHMATIC DENGAN BRUTE FORCE

import time

#### Procedure dan Function ####

def chartoint(huruf, angka, curr) :
# Fungsi untuk mengonversi huruf menjadi angka
    '''
    KAMUS LOKAL
    indeks : integer
    ALGORITMA
    '''
    i = huruf.index(curr)
    return angka[i]

def printsolusi(hasil):
# Fungsi untuk mencetak solusi
    '''
    KAMUS LOKAL
    max, i, selisih : integer
    ALGORITMA
    '''
    max = len(str(hasil[-1]))
    for i in range(0, len(hasil)-1) :
        curr = max - len(str(hasil[i]))
        while curr>0 :
            print(" ", end="")
            curr -= 1
        print(str(hasil[i]))
    print((max * "-") + "+")
    print(hasil[-1])

def cek(huruf, angka, awal, kalimat) :
# Fungsi untuk mengecek kombinasi angka yang didapat apakah memenuhi penjumlahan di soal
    '''
    KAMUS LOKAL
    total, tambah : integer
    x : character
    bil, current : string
    solusi, bilangan : List of integer
    ALGORITMA
    '''
    solusi = [-999]
    
    for x in awal :
        if chartoint(huruf, angka, x) == 0 :
            return solusi

    bilangan = []
    bil = ""
    for i in range(0, len(kalimat)) :
        if kalimat[i] != "/" :
            current = str(chartoint(huruf, angka, kalimat[i]))
            bil += current
        else :
            bilangan.append(bil)
            bil = ""

    total = 0
    for j in range(0, len(bilangan)-2) :
        tambah = int(bilangan[j])
        total += tambah
        solusi.append(tambah)
    if total == int(bilangan[len(bilangan)-1]) :
        solusi.append(int(bilangan[len(bilangan)-1]))
        solusi.pop(0)
    else :
        solusi = [-999]
    return solusi

#### Program Utama ####
''' KAMUS
    operand1, operand2, sumresult : string
    a, b, c, d, e, f, g, h, i, j, selisih, testcount : integer
    kalimat, awal, huruf : List of character
    angka : List of integer
    found : boolean
    start : time
    ALGORITMA
    '''

# Proses input 
filename = input("Masukkan nama file (ditambah .txt)\n")
f = open(filename, "r")
kata = f.readline().strip("\n")
if kata == "" :
    print("teks kosong")
    quit()
else :
    kalimat = []
    awal = []
    while kata :
        print(kata)
        for i in range(0, len(kata)) :
            if kata[i] != "-" and kata[i] != "+" :
                kalimat.append(kata[i])
                if i==0 :
                    awal.append(kata[i])
        kalimat.append("/")
        kata = f.readline().strip("\n")

# Mengumpulkan huruf-huruf dalam string unik (Menghapus huruf yang berduplikat)
huruf = []
for x in kalimat :
    if x not in huruf :
        huruf.append(x)
huruf.remove("/")
if len(huruf)>10 :
    print("karakter lebih dari 10")
    quit()

# Set waktu eksekusi dan jumlah tes
start = time.time()
testcount = 0

# Permutasi
found = False
angka = [-1 for i in range(10)]

a = 0
while a < 10 and not found:
    b = 0
    while b < 10 and not found:
        if b != a:
            c = 0
            while c < 10 and not found:
                if c != a and c != b:
                    d = 0
                    while d < 10 and not found:
                        if d != a and d != b and d != c:
                            e = 0
                            while e < 10 and not found:
                                if e != a and e != b and e != c and e != d:
                                    f = 0
                                    while f < 10 and not found:
                                        if f != a and f != b and f != c and f != d and f != e:
                                            g = 0
                                            while g < 10 and not found:
                                                if g != a and g != b and g != c and g != d and g != e and g != f:
                                                    h = 0
                                                    while h < 10 and not found:
                                                        if h != a and h != b and h != c and h != d and h != e and h != f and h != g:
                                                            i = 0
                                                            while i < 10 and not found:
                                                                if i != a and i != b and i != c and i != d and i != e and i != f and i != g and i != h:
                                                                    j = 0
                                                                    while j < 10 and not found:
                                                                        if j!= a and j != b and j != c and j != d and j != e and j != f and j != g and j != h and j != i:
                                                                            testcount += 1
                                                                            angka = [a,b,c,d,e,f,g,h,i,j] 
                                                                            hasil = cek(huruf, angka, awal, kalimat)
                                                                            if hasil[0] != -999 :
                                                                                found = True
                                                                        if not found:
                                                                            j += 1
                                                                if not found:
                                                                    i += 1
                                                        if not found:
                                                            h += 1
                                                if not found:
                                                    g += 1
                                        if not found:
                                            f += 1
                                if not found:
                                    e += 1
                        if not found:
                            d += 1
                if not found:
                    c += 1
        if not found:
            b += 1
    if not found:
        a += 1

# Solusi sudah ditemukan
if not found :
    print("Tidak ditemukan solusi")
else :
    print("solusi : \n")
    printsolusi(hasil)
    print("Tes ke- : ", testcount)
    print("Waktu : ", (time.time() - start), " detik")
