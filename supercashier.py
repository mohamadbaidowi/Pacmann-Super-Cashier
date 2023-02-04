# import untuk memakai fungsi membersihkan layar konsole
from os import system

class Transaction:
    ##############################################################################################################################################
    # class untuk menangani transaksi. Dalam transaksi akan dilakukan tambah barang, ubah nama barang, ubah jumlah barang, ubah harga barang,
    # hapus barang tertentu, hapus semua barang, dan check order/konfirmasi pesanan. Untuk menangani hal tersebut, akan diinisialisasi variabel
    # yang dipakai dan dibuat prosedur yang dibutuhkan. prosedur tersebut adalah:
    # satudigit, duadigit, tigadigit, dan terbilang untuk mengubah angka menjadi kata-kata
    # isnumeric untuk mengecek apakah input yang diberikan berupa angka
    # cek_item untuk mengecek apakah nomor item yang dipilih ada di keranjang belanja
    # inputyatidak untuk memvalidasi apakah user memasukkan jawaban Y/y/T/t
    # inputnumeric, inputinteger, inputnamabarang digunakan untuk menangani input dan melakukan pengecekan apakah inputnya sesuai yang seharusnya
    # total_price untuk menghtung total nilai belanja dan diskonnya jika ada
    # printcart untuk menampilkan daftar belanjaan dengan format tertentu
    # add_item untuk menangani penambahan barang kedalam keranjang belanja
    # delete item untuk mengahapus item tertentu dalam keranjang belanja
    # reset_transaction untuk mengahapus semua item dalam keranjang belanja
    # update_item_price, update_item_qty, update_item_name untuk menangani perubahan harga, jumlah atau nama barang dalam keranjang belanja
    ##############################################################################################################################################

    def __init__(self):
        # inisialisasi variabel untuk keranjang belanja
        self.storecart = {}
        # inisialisai variabel lebar kolom untuk format keranjang belanja
        self.kolom1 = 5
        self.kolom2 = 50
        self.kolom3 = 15
        self.kolom4 = 20
        self.kolom5 = 30
        self.paddingbaris = self.kolom1 + self.kolom2 + self.kolom3 + self.kolom4 + self.kolom5 + 12
        self.paddingfooter = self.paddingbaris - self.kolom5 - 3
        # set format untuk baris dan footer keranjang belanja
        self.formatbaris = "{:<" + str(self.kolom1) + "} | {:<" + str(self.kolom2) + "} | {:<" + str(self.kolom3) + "} | {:<" + str(self.kolom4) + "} | {:<" + str(self.kolom5) + "}"
        self.formatfooter = "{:<" + str(self.paddingfooter) + "} | {:<" + str(self.kolom5) + "}"

    def satudigit(self,n):
        #########################################################################################################################################
        # fungsi untuk mengubah angka satu digit menjadi kata-kata
        # inputnya berupa angka yang panjangnya satu digit
        # outputnya berupa kata terbilang dari angka input
        #########################################################################################################################################
        hasil = ''
        if n==0:
            hasil = 'Nol'
        elif n==1:
            hasil = 'Satu'
        elif n==2:
            hasil = 'Dua'
        elif n==3:
            hasil = 'Tiga'
        elif n==4:
            hasil = 'Empat'
        elif n==5:
            hasil = 'Lima'
        elif n==6:
            hasil = 'Enam'
        elif n==7:
            hasil = 'Tujuh'
        elif n==8:
            hasil = 'Delapan'
        elif n==9:
            hasil = 'Sembilan'
        return hasil

    def duadigit(self,n):
        #########################################################################################################################################
        # fungsi untuk mengubah angka dua digit menjadi kata-kata
        # inputnya berupa angka yang panjangnya dua digit
        # untuk memproses satuan, angka memanggil fungsi satudigit
        # outputnya berupa kata terbilang dari angka input
        #########################################################################################################################################
        hasil = ''
        # memisahkan angka 2 digit menjadi puluhan dan satuan
        puluhan = n // 10
        satuan = n % 10
        if n < 10:
            # jika ternyata angka lebih kecil dari 10, langsung proses dengan fungsi satudigit
            hasil = self.satudigit(n)
        elif n < 20:
            # jika ternyata angka lebih besar dari 10 tapi lebih kecil dari 20, diproses khusus karena akhirannya belas dan untuk puluhan 1 = se... bukan satu
            if satuan == 0:
                hasil = 'Sepuluh'
            elif satuan == 1:
                hasil = 'Sebelas'
            else:
                hasil = self.satudigit(satuan) + ' Belas'
        elif n < 100:
            # jika lebih besar 20 dan lebih kecil 100 puluhan dikasih akhiran puluh
            hasil = self.satudigit(puluhan) + ' Puluh'
            if satuan > 0:
                hasil = hasil + ' ' + self.satudigit(satuan)
        return hasil

    def tigadigit(self,n):
        #########################################################################################################################################
        # fungsi untuk mengubah angka tiga digit menjadi kata-kata
        # inputnya berupa angka yang panjangnya tiga digit
        # untuk memproses ratusan, angka memanggil fungsi duadigit
        # outputnya berupa kata terbilang dari angka input
        #########################################################################################################################################
        hasil = ''
        if n < 100:
            # jika lebih kecil dari Seratus langsung diproses dengan fungsi duadigit
            hasil = self.duadigit(n)
        else:
            # jika lebih atau sama dengan 100, angka ratusan diproses sendiri sedangkan sisanya diproses dengan fungsi duadigit
            ratusan = n // 100
            sisa = n % 100
            if ratusan == 1:
                hasil = 'Seratus'
                if sisa > 0:
                    hasil = hasil + ' ' + self.duadigit(sisa)
            else:
                hasil = self.satudigit(ratusan) + ' Ratus'
                if sisa > 0:
                    hasil = hasil + ' ' + self.duadigit(sisa)
        return hasil

    def terbilang(self,uang):
        #########################################################################################################################################
        # fungsi untuk mengubah angka menjadi kata-kata
        # inputnya berupa angka dengan maksimal angkanya 999,999,999,999,999,999
        # outputnya berupa kata terbilang dari angka input
        #########################################################################################################################################
        if uang <= 999999999999999999:
            # mendefinisikan satuan setiap 3 angka
            keterangan = ['','Ribu','Juta', 'Milyar', 'Triliun', 'Biliun']
            # variabel untuk ambil indek list keterangan
            mulai = 0
            # memecah menjadi angka utama dan desimal, desimal yang diproses hanya dua angka
            pecahan = uang % 1
            n = int(uang - pecahan)
            pecahan = int(100*round(pecahan,2))
            hasil = ''
            # mulai proses angka utama dengan memprosesnya per tiga digit / perseribu
            while n >= 1000:
                # ambil 3 digit paling kanan
                palingkanan = n % 1000
                # jika lebih besar dari nol proses dengan fungsi tigadigit, penanganan khusus untuk angka seribu
                if palingkanan > 0:
                    if palingkanan == 1 and mulai == 1:
                        hasil = 'Seribu ' + hasil
                    else:
                        hasil = self.tigadigit(palingkanan) + ' ' + keterangan[mulai] + ' ' + hasil
                # ditambah nilainya untuk ambil indek list berikutnya
                mulai = mulai + 1
                #angkanya diupdate, dihilangkan tiga digit paling kanan yang sudah diproses
                n = n // 1000
            # memproses tiga digit terakhir
            if mulai == 1 and n == 1:
                hasil = 'Seribu ' + hasil
            else:
                hasil = self.tigadigit(n) + ' ' + keterangan[mulai] + ' ' + hasil
            # untuk memproses pecahan
            if pecahan > 0:
                hasil =  hasil.rstrip() + ' - ' + self.duadigit(pecahan) + ' Sen'
            return('Terbilang ' + hasil.rstrip())
        else:
            return('Out of range')

    def isnumeric(self, n, tipe):
        #########################################################################################################################################
        # fungsi untuk cek apakah input berupa float / integer atau bukan
        # inputnya berupa angka yang akan dicek dan tipe yang dimaksud (float/int)
        # outputnya berupa true jika sesuai tipe yang dimaksud dan false jika tidak sesuai
        #########################################################################################################################################
        try:
            if tipe == 'float':
                # dicek apakah bisa diubah menjadi float, jika tidak bisa akan menjalankan except blok
                float(n)
            elif tipe == 'int':
                # dicek apakah bisa diubah menjadi integer, jika tidak bisa akan menjalankan except blok
                int(n)
        except ValueError:
            # return false jika gagal diubah - input tidak sesuai tipe
            return False
        else:
            # return True jika berhasil diubah - input sesuai tipe
            return True

    def cek_item(self,nomoritem):
        #########################################################################################################################################
        # fungsi untuk cek apakah nomor item yang dipilih ada dalam keranjang belanja
        # inputnya berupa nomoritem yang mempresentasikan barang di keranjang belanja
        # outputnya berupa key dari barang di keranjang Belanja atau kosong jika tidak ditemukan barangnya
        #########################################################################################################################################
        # cek nomor yang dipilih lebih besar nol dan lebih kecil dari jumlah item di keranjang belanja
        if (nomoritem > 0) and (nomoritem <= len(self.storecart)):
            y = 0
            # dibandingkan dengan item di keranjang belanja.
            for items in self.storecart:
                y += 1
                # jika ada yang sesuai, return key dari dictionary dari item di keranjang belanja
                if y == nomoritem:
                    return items
                    break
        else:
            # jika tidak ada yang sesuai, kasih pesan item tidak ada
            print(" Tidak ada item nomor tersebut ".center(tr.paddingbaris,'*') )
            return ''

    def inputyatidak(self, ket):
        #########################################################################################################################################
        # fungsi untuk minta input Y/T untuk konfirmasi suatu hal
        # inputnya berupa deskripsi hal yang akan dikonfirmasi
        # outputnya berupa karakter Y atau T
        #########################################################################################################################################
        mintainput = True
        while mintainput == True:
            nilaiinput = input(ket + " (Y/T) : ")
            if nilaiinput.upper() == 'Y' or nilaiinput.upper() == 'T' :
                # jika jawaban sudah benar, proses input selesai
                mintainput = False
                return nilaiinput
            else:
                # jika jawaban salah, diberikan peringatan dan looping lagi minta input
                print(" Jawab dengan Y atau T ".center(tr.paddingbaris,'*'))

    def inputnumeric(self,ket,max):
        #########################################################################################################################################
        # fungsi untuk minta input numeric dengan batas tertentu
        # inputnya berupa deskripsi dari input yang diminta dan batas angka maksimal yang dibolehkan
        # outputnya berupa angka numeric yang diisikan
        #########################################################################################################################################
        # akan dilakukan looping selama input yang dimasukkan belum sesuai
        mintainput = True
        while mintainput == True:
            # minta input ke user
            nilaiinput = input(ket + " : ")
            # dicek apakah inputnya berupa angka
            if self.isnumeric(nilaiinput, 'float'):
                # dicek apakah angkanya lebih dari nol
                if float(nilaiinput) > 0.0:
                    # dicek apakah angkanya kurang atau sama dengan angka maksimal yang diperbolehkan
                    if float(nilaiinput) <= max:
                        # jika ya, input sudah sesuai
                        mintainput = False
                        return nilaiinput
                    else:
                        # input lebih besar dari maksimal angka yang diperbolehkan
                        warning = " Data input maksimal yang diperbolehkan " + "{:,.2f}".format(max) + " "
                        print(warning.center(tr.paddingbaris,'*'))
                else:
                    # input lebih kecil atau sama dengan nol
                    print(" Data input harus lebih besar dari nol ".center(tr.paddingbaris,'*'))
            else:
                # input bukan berupa angka
                print(" Data input harus berupa angka ".center(tr.paddingbaris,'*'))

    def inputinteger(self,ket):
        #########################################################################################################################################
        # fungsi untuk minta input integer
        # inputnya berupa deskripsi dari input yang diminta
        # outputnya berupa angka integer yang diisikan
        #########################################################################################################################################
        # akan dilakukan looping selama input yang dimasukkan belum sesuai
        mintainput = True
        while mintainput == True:
            # minta input ke user
            nilaiinput = input(ket + " : ")
            # dicek apakah inputnya berupa integer
            if self.isnumeric(nilaiinput, 'int'):
                # dicek apakah angkanya lebih dari nol
                if int(nilaiinput) > 0:
                    # jika ya, input sudah sesuai
                    mintainput = False
                    return nilaiinput
                else:
                    # input lebih kecil atau sama dengan nol
                    print(" Data input harus lebih besar dari nol ".center(tr.paddingbaris,'*'))
            else:
                # input bukan berupa integer
                print(" Data input harus berupa integer ".center(tr.paddingbaris,'*'))

    def inputnamabarang(self,ket,namalama,max):
        #########################################################################################################################################
        # fungsi untuk minta input nama barang berupa karakter dengan panjang maksimal yang ditentukan
        # inputnya berupa deskripsi dari input yang diminta, nama barang lama jika ada dan panjang maksimal karakter yang diperbolehkan
        # outputnya berupa nama barang yang diisikan
        #########################################################################################################################################
        mintainput = True
        while mintainput == True:
            # minta input ke user
            nilaiinput = input(ket + " : ")
            # dicek apakah namalama kosong, jika tidak artinya untuk ganti nama barang
            if namalama != '':
                # dicek apakah user input kosong
                if nilaiinput.replace(' ','') == '':
                    # jika kosong diberikan peringatan
                    print(" Nama baru tidak boleh kosong ".center(tr.paddingbaris,'*'))
                else:
                    # jika tidak kosong, cek panjang input apakah melebihi maksimal yang dibutuhkan
                    if len(nilaiinput) > max:
                        # jika melebih maksimal diberikan peringatan
                        warning = " Nama baru maksimal "+ str(max)  + " karakter "
                        print(warning.center(tr.paddingbaris,'*'))
                    else:
                        # cek apakah input sama dengan nama lama
                        if nilaiinput.replace(' ','').upper() == namalama.replace(' ','').upper() :
                            # jika sama diberikan peringatan
                            print(" Nama baru harus berbeda dengan nama sebelumnya ".center(tr.paddingbaris,'*'))
                        else:
                            # cek apakah input sama dengan nama barang lain di keranjang belanja
                            adayangsama = False
                            for keyslist in self.storecart:
                                if (keyslist != namalama) and (nilaiinput.replace(' ','').upper() == keyslist.replace(' ','').upper()) :
                                    # jika ada yang sama diberikan peringatan
                                    print(" Nama baru harus berbeda dengan nama item yang sudah ada ".center(tr.paddingbaris,'*'))
                                    adayangsama = True
                            # jika tidak ada yang sama, input sudah benar, looping dihentikan
                            if adayangsama == False:
                                mintainput = False
                                return nilaiinput
            else:
                # namalama kosong, input nama barang untuk tambah item baru
                # dicek apakah user input kosong
                if nilaiinput.replace(' ','') == '':
                    # jika kosong diberikan peringatan
                    print(" Nama barang tidak boleh kosong ".center(tr.paddingbaris,'*'))
                else:
                    # jika tidak kosong, cek panjang input apakah melebihi maksimal yang dibutuhkan
                    if len(nilaiinput) > max:
                        # jika melebih maksimal diberikan peringatan
                        warning = " Nama barang maksimal " + str(max) + " karakter "
                        print(warning.center(tr.paddingbaris,'*'))
                    else:
                        # cek apakah input sama dengan nama barang lain di keranjang belanja
                        adayangsama = False
                        for keyslist in self.storecart:
                            if nilaiinput.replace(' ','').upper() == keyslist.replace(' ','').upper() :
                                # jika ada yang sama diberikan peringatan
                                print(" Nama barang harus berbeda dengan nama item yang sudah ada ".center(tr.paddingbaris,'*'))
                                adayangsama = True
                        # jika tidak ada yang sama, input sudah benar, looping dihentikan
                        if adayangsama == False:
                            mintainput = False
                            return nilaiinput

    def total_price(self):
        #########################################################################################################################################
        # fungsi untuk menghitung total harga di keranjang belanja dan juga diskonnya
        # inputnya tidak ada
        # outputnya berupa total nilai barang di keranjang belanja dan diskonnya
        #########################################################################################################################################
        thetotal = []
        totalamount = 0
        discount = 0
        # menghitung total harga di keranjang
        for items in self.storecart:
            qtyprice = self.storecart[items]
            totalamount += qtyprice[0]*qtyprice[1]
        # jika total harga lebih dari 500rb diskon 10%
        if totalamount > 500000:
            discount = totalamount * 0.1
        # jika total harga antara 500rb dan 300rb diskon 8%
        elif totalamount <= 500000 and totalamount > 300000:
            discount = totalamount * 0.08
        # jika total harga antara 300rb dan 200rb diskon 5%
        elif totalamount <= 300000 and totalamount > 200000:
            discount = totalamount * 0.05
        else:
            discount = totalamount * 0
        # total harga dan diskon dimasukkan ke list ebagai return value
        thetotal.append(totalamount)
        thetotal.append(discount)
        return thetotal

    def printcart(self,tipe):
        #########################################################################################################################################
        # fungsi untuk menampilkan isi keranjang belanja
        # inputnya berupa tipe tampilan keranjang belanja apakah dilengkapi dengan diskon dan total yang harus dibayar atau tidak
        # outputnya berupa keranjang belanja yang dicetak di layar
        #########################################################################################################################################
        # bersihkan layar
        system('cls')
        # cetak header keranjang belanja
        print("Keranjang Belanja")
        print("-".rjust(self.paddingbaris,'-'))
        print(self.formatbaris.format('No', 'Nama Item', 'Jumlah','Harga','Total'))
        print("-".rjust(self.paddingbaris,'-'))
        # cetak item keranjang belanja
        noitem = 0
        totalamount = 0
        for items in self.storecart:
            qtyprice = self.storecart[items]
            noitem += 1
            amount = qtyprice[0]*qtyprice[1]
            totalamount += amount
            print(self.formatbaris.format(str(noitem).rjust(self.kolom1,' '), items,"{:,.2f}".format(qtyprice[0]).rjust(self.kolom3,' '),"{:,.2f}".format(qtyprice[1]).rjust(self.kolom4,' '),"{:,.2f}".format(amount).rjust(self.kolom5,' ')))
        # cetak total keranjang belanja
        totalharga = tr.total_price()
        print("-".rjust(self.paddingbaris,'-'))
        print(self.formatfooter.format('Total Harga'.rjust(self.paddingfooter,' '),"{:,.2f}".format(totalharga[0]).rjust(self.kolom5,' ')))
        print("-".rjust(self.paddingbaris,'-'))
        # jika total price on, cetak diskon dan total pembayaran serta terbilang
        if tipe == 'total price on':
            harusdibayar = totalharga[0] - totalharga[1]
            print(self.formatfooter.format('Diskon'.rjust(self.paddingfooter,' '),"{:,.2f}".format(totalharga[1]).rjust(self.kolom5,' ')))
            print("-".rjust(self.paddingbaris,'-'))
            print(self.formatfooter.format('Total Pembayaran'.rjust(self.paddingfooter,' '),"{:,.2f}".format(harusdibayar).rjust(self.kolom5,' ')))
            print("-".rjust(self.paddingbaris,'-'))
            print(self.terbilang(harusdibayar).rstrip().rjust(self.paddingbaris,' '))
        print("\n")

    def add_item(self,nama_item, jumlah_item, harga_item):
        #########################################################################################################################################
        # fungsi untuk penambahan item baru di keranjang belanja
        # inputnya  nama_item untuk nama barang jumlah_item untuk jumlah barang dan harga_item untuk harga barang
        # keranjang belanja akan diupdate dengan barang yang ditambahkan
        #########################################################################################################################################
        # inisialisai list untuk menampung jumlah dan harga barang
        theitem = []
        # memasukkan jumlah barang
        theitem.append(float(jumlah_item))
        # memasukkan harga barang
        theitem.append(float(harga_item))
        # menyimpan barang dalam keranjang belanja dalam bentuk dictionary dengan nama barang sebagai key nya
        self.storecart[nama_item] = theitem

    def delete_item(self,nama_item):
        #########################################################################################################################################
        # fungsi untuk hapus item barang tertentu di keranjang belanja
        # inputnya  nama_item untuk nama barang yang akan dihapus
        # barang di keranjang belanja dengan key sama dengan nama_item akan dihapus
        #########################################################################################################################################
        # dilakukan hapus keranjang belanja dengan mengahapus dictionary dengan key sesuai nama_item
        self.storecart.pop(nama_item)

    def reset_transaction(self):
        #########################################################################################################################################
        # fungsi untuk hapus semua barang  di keranjang belanja
        # inputnya tidak ada
        # barang di keranjang belanja akan dihapus semua
        #########################################################################################################################################
        # dilakukan hapus inisialisai dictionary keranjang belanja menjadi kosong
        self.storecart = {}

    def update_item_price(self,nama_item,update_harga_item):
        #########################################################################################################################################
        # fungsi untuk update harga item barang tertentu di keranjang belanja
        # inputnya nama_item sebagai nama barang dan update_harga_item sebagai harga baru barang tersebut
        # barang di keranjang belanja dengan key sama dengan nama_item akan diupdate harganya menjadi update_harga_item
        #########################################################################################################################################
        # ambil list dari keranjang belanja yang berisi jumlah dan harga barang
        qtyprice = self.storecart[nama_item]
        # update harga barang dengan harga yang baru
        qtyprice[1] = float(update_harga_item)
        # simpan dalam keranjang belanja
        self.storecart[nama_item] = qtyprice

    def update_item_qty(self,nama_item,update_jumlah_item):
        #########################################################################################################################################
        # fungsi untuk update jumlah barang tertentu di keranjang belanja
        # inputnya nama_item sebagai nama barang dan update_jumlah_item sebagai jumlah baru barang tersebut
        # barang di keranjang belanja dengan key sama dengan nama_item akan diupdate jumlahnya menjadi update_jumlah_item
        #########################################################################################################################################
        # ambil list dari keranjang belanja yang berisi jumlah dan harga barang
        qtyprice = self.storecart[nama_item]
        # update jumlah barang dengan harga yang baru
        qtyprice[0] = float(update_jumlah_item)
        # simpan dalam keranjang belanja
        self.storecart[nama_item] = qtyprice

    def update_item_name(self,nama_item,update_nama_item):
        #########################################################################################################################################
        # fungsi untuk update nama barang tertentu di keranjang belanja
        # inputnya nama_item sebagai nama barang dan update_nama_item sebagai nama baru barang tersebut
        # barang di keranjang belanja dengan key sama dengan nama_item akan diupdate namanya menjadi update_nama_item
        #########################################################################################################################################
        # ambil list dari keranjang belanja yang berisi jumlah dan harga barang
        qtyprice = self.storecart[nama_item]
        # hapus dari keranjang belanja barang yang key sama dengan nama_item
        self.storecart.pop(nama_item)
        # tambahkan dalam keranjang belanja barang baru dengan key sama dengan update_nama_item
        self.storecart[update_nama_item] = qtyprice

try:
    #########################################################################################################################################
    # main program untuk menampilkan menu dan memproses sesuai dengan menu yang dipilih
    # akan ditampilkan terus selama pelanggan belum keluar dan setelah cek pesanan dinyatakan sudah benar oleh pelanggan
    # jika ada kesalahan akan ditampilkan pesan kesalahan yang terjadi
    #########################################################################################################################################

    # memulai aplikasi dengan membuat Transaction object
    tr = Transaction()
    # selama belum berkakhir, akan ditampilkan menu aplikasinya
    whatever = True
    while whatever == True:
        # cek keranjang belanja apakah kosong atau tidak
        if len(tr.storecart) > 0:
            # jika keranjang belanja  tidak kosong, ditampilkan menu lengkap
            print("""
                Super Cashier:
                1-Tambah item
                2-Ubah nama item tertentu
                3-Ubah jumlah item tertentu
                4-Ubah harga item tertentu
                5-Hapus item tertentu
                6-Hapus semua item
                7-Cek Pesanan
                8-Keluar
            """)
            # menu apa yang dipilih
            choice = input("Pilih menu nomor : ")
            if choice == "1":
                # jika memilih menu tambah item
                print(" Tambah Item ".center(tr.paddingbaris,'='))
                # input nama barang
                namaitem = tr.inputnamabarang("Nama Barang","",40)
                # input jumlah barang
                jumlahitem = tr.inputnumeric("Jumlah Barang",10000)
                # input harga barang
                hargaitem = tr.inputnumeric("Harga Barang",1000000000)
                # memasukkan ke keranjang belanja
                tr.add_item(namaitem,jumlahitem,hargaitem)
                # menampilkan keranjang belanja
                tr.printcart('total price off')
            elif choice == "2":
                # jika memilih menu ubah nama item tertentu
                print(" Ubah Nama Item ".center(tr.paddingbaris,'='))
                # input item nomor berapa di keranjang belanja yang akan diubah
                itemdiedit = int(tr.inputinteger("Nomor item yang akan diubah namanya"))
                # cek apakah ada item tersebut di keranjang belanja
                if tr.cek_item(itemdiedit) != '':
                    # jika ada diminta input nama baru untuk barang tersebut
                    namaitem = tr.inputnamabarang("Nama Barang yang baru", tr.cek_item(itemdiedit),40)
                    # keranjang belanja diupdate
                    tr.update_item_name(tr.cek_item(itemdiedit),namaitem )
                else:
                    tunggu = input("Tidak ada item " + str(itemdiedit) + ". Tekan ENTER tombol untuk melanjutkan")
                # menampilkan keranjang belanja terupdate
                tr.printcart('total price off')
            elif choice == "3":
                # jika memilih menu ubah jumlah item tertentu
                print(" Ubah Jumlah Item ".center(tr.paddingbaris,'='))
                # input item nomor berapa di keranjang belanja yang akan diubah
                itemdiedit = int(tr.inputinteger("Nomor item yang akan diubah jumlahnya"))
                # cek apakah ada item tersebut di keranjang belanja
                if tr.cek_item(itemdiedit) != '':
                    # jika ada diminta input jumlah baru untuk barang tersebut
                    jumlahitem = tr.inputnumeric("Jumlah Barang yang baru",10000)
                    # keranjang belanja diupdate
                    tr.update_item_qty(tr.cek_item(itemdiedit),jumlahitem )
                else:
                    tunggu = input("Tidak ada item " + str(itemdiedit) + ". Tekan ENTER tombol untuk melanjutkan")

                # menampilkan keranjang belanja terupdate
                tr.printcart('total price off')
            elif choice == "4":
                # jika memilih menu ubah harga item tertentu
                print(" Ubah Harga Item ".center(tr.paddingbaris,'='))
                # input item nomor berapa di keranjang belanja yang akan diubah
                itemdiedit = int(tr.inputinteger("Nomor item yang akan diubah harganya"))
                # cek apakah ada item tersebut di keranjang belanja
                if tr.cek_item(itemdiedit) != '':
                    # jika ada diminta input harga baru untuk barang tersebut
                    hargaitem = tr.inputnumeric("Harga Barang yang baru",1000000000)
                    # keranjang belanja diupdate
                    tr.update_item_price(tr.cek_item(itemdiedit),hargaitem )
                else:
                    tunggu = input("Tidak ada item " + str(itemdiedit) + ". Tekan ENTER tombol untuk melanjutkan")
                # menampilkan keranjang belanja terupdate
                tr.printcart('total price off')
            elif choice == "5":
                # jika memilih menu hapus item tertentu
                print(" Hapus Item Tertentu ".center(tr.paddingbaris,'='))
                # input item nomor berapa di keranjang belanja yang akan dihapus
                itemdihapus = int(tr.inputinteger("Nomor item yang dihapus"))
                # cek apakah ada item tersebut di keranjang belanja
                if tr.cek_item(itemdihapus) != '':
                    # konfirmasi akan dihapus
                    YatauT = tr.inputyatidak("Apakah item " + str(itemdihapus) + " akan dihapus ?")
                    if YatauT.upper() == 'Y':
                        # keranjang belanja diupdate
                        tr.delete_item(tr.cek_item(itemdihapus))
                else:
                    tunggu = input("Tidak ada item " + str(itemdihapus) + ". Tekan ENTER tombol untuk melanjutkan")
                # menampilkan keranjang belanja terupdate
                tr.printcart('total price off')
            elif choice == "6":
                # jika memilih menu hapus semua item
                print(" Hapus Semua Item ".center(tr.paddingbaris,'='))
                # menampilkan konfirmasi untuk hapus semua item
                YatauT = tr.inputyatidak("Apakah mau dihapus semua ?")
                if YatauT.upper() == 'Y':
                    # jika ya, maka dihapus semua item
                    tr.reset_transaction()
                # menampilkan keranjang belanja terupdate
                tr.printcart('total price off')
            elif choice == "7":
                # jika memilih menu cek pesanan
                # menampilkan keranjang belanja dengan diskonnya
                tr.printcart('total price on')
                print(" Cek Pesanan ".center(tr.paddingbaris,'='))
                # mengkonfirmasi apakah pesanan sudah benar
                YatauT = tr.inputyatidak("Apakah pesanan sudah benar")
                if YatauT.upper() == 'Y':
                    # jika sudah benar diberi pesan Silahkan bayar
                    tr.printcart('total price on')
                    print(" Silahkan Bayar ".center(tr.paddingbaris,'='))
                    whatever = False
                else:
                    # jika belum benar diberi pesan untuk memperbaiki
                    tr.printcart('total price off')
                    print(" Silahkan diperbaiki ".center(tr.paddingbaris,'='))
            elif choice == "8":
                # jika memilih menu keluar aplikasi
                YatauT = tr.inputyatidak("Apakah mau benar mau keluar")
                if YatauT.upper() == 'Y':
                    system('cls')
                    whatever = False
                    print('Terima kasih')
                else:
                    tr.printcart('total price off')
            else:
                # jika memilih diluar yang ditentukan
                print(" Pilih 1,2,3,4,5,6,7 atau 8 ".center(tr.paddingbaris,'*'))
        else:
            # jika keranjang belanja kosong, hanya ditampilkan menu meulai belanja dan Keluar
            print("""
                Super Cashier:
                1-Mulai Belanja
                2-Keluar
            """)
            choice = input("Pilih menu nomor : ")
            if choice == "1":
                # jika memilih menu mulai belanja
                print(" Tambah Item ".center(tr.paddingbaris,'='))
                # input nama barang
                namaitem = tr.inputnamabarang("Nama Barang","",40)
                # input jumlah barang
                jumlahitem = tr.inputnumeric("Jumlah Barang",10000)
                # input harga barang
                hargaitem = tr.inputnumeric("Harga Barang",1000000000)
                # memasukkan ke keranjang belanja
                tr.add_item(namaitem,jumlahitem,hargaitem)
                # menampilkan keranjang belanja
                tr.printcart('total price off')
            elif choice == "2":
                # jika memilih menu keluar aplikasi
                YatauT = tr.inputyatidak("Apakah benar mau keluar")
                system('cls')
                if YatauT.upper() == 'Y':
                    whatever = False
                    print('Terima kasih')
            else:
                # jika memilih diluar yang ditentukan
                print(" Pilih 1 atau 2 ".center(tr.paddingbaris,'*'))
except Exception as error:
    print("Error with error message: ", error)
