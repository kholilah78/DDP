jumbaris = int(input("Masukan jumlah baris: "))
for baris in range(1, jumbaris+1):
    for kolom in range(baris):
        print('*', end=' ')
    print()