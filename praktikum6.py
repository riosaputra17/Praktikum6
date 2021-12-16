data_base = {} 

def ruler():
    print(73*"=")

def header():
    ruler()
    print("| {0:^2} | {1:^9} | {2:^18} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("NO", "NIM", "NAMA", "TUGAS", "UTS", "UAS", "N.AKHIR"))
    ruler()

def nodata(): 
    header()          
    print("|{0:^72}|".format("Data Not Found!!"))
    ruler()

def tambah():
    print("Tambah Data")
    nama       = input("Nama        : ")
    nim        = input("NIM         : ")
    nilaiTugas = int(input("Nilai Tugas : "))
    nilaiUTS   = int(input("Nilai UTS   : "))
    nilaiUAS   = int(input("Nilai UAS   : "))
    nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUTS * 35/100) + (nilaiUAS * 35/100)
    data_base[nama] = [nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir]
    print(f"Berhasil menambahkan data '{nama}' dengan NIM : {nim}!")

def Tampilkan():
    print("============================Daftar Mahasiswa============================")
    if len(data_base) <= 0:  
        nodata()
    else:
        no = 0
        header()
        for data in data_base.items():
            no += 1 
            print(f"| {no:>2} | {data[1][0]:<9} | {data[0]:<18} | {data[1][1]:>5} | {data[1][2]:>5} | {data[1][3]:>5} | {data[1][4]:>7.2f} |")               
        ruler() 

def ubah():
    print("Ubah Data Mahasiswa berdasarkan Nama")
    if len(data_base) <= 0:  
        nodata()

    else:
        nama = input("Masukan Nama : ") 
        if nama in data_base.keys():
            print(f"Data ditemukan!")
            print(25*"=")
            print(f"Nama        : {nama}")
            print(f"NIM         : {data_base[nama][0]}")
            print(f"Nilai Tugas : {data_base[nama][1]}")
            print(f"Nilai UTS   : {data_base[nama][2]}")
            print(f"Nilai UAS   : {data_base[nama][3]}")
            print(25*"=")
            print("1. Nama\n2. NIM\n3. Nilai\n0. Kembali")
            tanya = int(input("Apa yang ingin diubah? [1-3] : "))
            if tanya == 1:
                _nama = input("Masukan Nama Baru : ")
                data_base[_nama] = data_base.pop(nama)
                print("Berhasil merubah Nama! ")

            elif tanya == 2:
                _nim = input("Masukan Nim Baru : ")
                data_base[nama][0] = _nim
                print("Berhasil merubah NIM!")

            elif tanya == 3:
                _nilaiTugas = int(input("Masukan Nilai Tugas Baru : "))
                _nilaiUTS = int(input("Masukan Nilai UTS Baru : "))
                _nilaiUAS = int(input("Masukan Nilai UAS Baru : "))
                _nilaiAkhir = _nilaiTugas * 30/100 + _nilaiUTS * 35/100 + _nilaiUAS * 35/100
                data_base[nama][1:4] = _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir
                print("Berhasil merubah data nilai!")
            elif tanya == 0:
                pass
            
            else:
                print(f"Pilihan {tanya} tidak ada! Silahkan masukan [1-3]")

        else:
            print(f"Data {nama} tidak ditemukan!") 

def hapus():
    print("Hapus Data Mahasiswa berdasarkan Nama")
    if len(data_base) <= 0:  
        nodata()

    else:
        nama = input("Masukan nama : ")
        if(nama in data_base):
            del data_base[nama]
            print(f"Data {nama} berhasil dihapus!")
        else:
            print(f"Data {nama} tidak ditemukan!")

while True:
    print()
    print(25*"-", "Program Input Nilai", 25*"-")
    print("1. Tambah Data \n2. Tampilkan Data \n3. Ubah Data \n4. Hapus Data \n0. Keluar")
    print(73*"-")
    menu = int(input("Pilih menu : "))
    print(73*"-")
    print()

    if menu == 1:
        tambah()       

    elif menu == 2:
        Tampilkan()

    elif menu == 3:
        ubah() 

    elif menu == 4:
        hapus()

    elif menu == 0:
        print("End Program")
        loop = False 

    else:
        print(f"Menu '{menu}' yang anda pilih tidak ada  [0-4]")
