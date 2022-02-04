import random
import datetime
from customer import Customer

atm = Customer(id)

while True:

    id = int(input("Masukkan pin anda: "))
    
    tryCount = 0

    while (id != int(atm.checkPin()) and tryCount < 3):
        print("Pin anda salah.")
        id = int(input("Silahkan masukkan pin anda kembali: "))
        tryCount += 1

        if tryCount == 3:
            print("Akun anda terboklir")
            exit()

    while True:
            print("Selamat datang")
            print("Pilih Menu :\n 1 -  Cek Saldo\n 2 - Debet\n 3 - Simpan\n 4 - Ganti Pin\n 5 - Keluar")
            menuPilihan = int(input("Pilihan : "))

            if menuPilihan == 1:
                print("Rp. " + str(atm.checkSaldo()))
            elif menuPilihan == 2:
                nominal = int(input('Masukan jumlah yang ingin ditarik: '))
                if nominal < atm.custSaldo:
                    atm.debet(nominal)
                    print("Berhasil menarik sejumlah Rp. " + str(nominal))
                    print("Saldo anda saat ini adalah " + str(atm.checkSaldo()))
                else:
                    print("Saldo anda kurang!")
            elif menuPilihan == 3:
                nominal = int(input('Masukan jumlah yang ingin disimpan: '))
                atm.simpan(nominal)
                print("Berhasil menyimpan sejumlah Rp. " + str(nominal))
                print("Saldo anda saat ini adalah " + str(atm.checkSaldo()))
            elif menuPilihan == 4:
                verifyPin = int(input('Masukkan pin anda :'))
                while verifyPin != atm.checkPin():
                    print("Pin salah!")
                    verifyPin = int(input('Masukkan pin anda :'))

                if verifyPin == atm.checkPin():
                    newPin = int(input('Masukkan pin baru : '))
                    verifyNewPin = int(input('Konfirmasi pin baru : '))
                    while newPin != verifyNewPin:
                        print("Konfirmasi pin baru salah!\n")
                        newPin = int(input('Masukkan pin baru : '))
                        verifyNewPin = int(input('Konfirmasi pin baru : '))
                    atm.changePin(newPin)
                    print("Pin anda berhasil diganti!")
            elif menuPilihan == 5:
                print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
                print("No. Rekord: ", random.randint(100000, 1000000))
                print("Tanggal: ", datetime.datetime.now())
                print("Saldo akhir: ", atm.checkSaldo())
                print("Terima kasih telah menggunakan ATM Progate!")
                exit()
            else:
                print("Menu tidak ditemukan")