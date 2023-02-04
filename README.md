# Pacmann-Super-Cashier

<h2>Background</h2>
Seorang pemilik supermarket ingin membuat kasir self-service dimana pelanggan bisa memasukkan jenis item yang mau dibeli, jumlahnya dan harganya secara mandiri. Karena itu, dalam project kali ini, akan dibuat Pacmann Super Cashier untuk memenuhi kebutuhan tersebut.
<h2>Feature requirements</h2>
Agar Pacmann Super Cashier sebagai aplikasi self-service untuk melakukan belanja dapat memenuhi kebutuhan pelanggannya, maka perlu disusun fungsi-fungsi yang mendukung. Berikut fasilitas yang diperlukan :

<ol>
<li>Fungsi untuk memulai belanja
<li>Fungsi untuk memasukkan nama barang, jumlahnya dan harganya
<li>Fungsi untuk melakukan perubahan nama barang
<li>Fungsi untuk melakukan perubahan jumlah barang
<li>Fungsi untuk melakukan perubahan harga barang
<li>Fungsi untuk menghapus barang tertentu yang akan dibeli 
<li>Fungsi untuk menghapus semua barang yang akan dibeli
<li>Fungsi cek pesanan sebelum melakukan pembayaran
</ol>

Untuk mempermudah implementasi, maka dibuat alur program untuk aplikasi kasir self service ini sebelum dibuatkan kodenya. 
Ketika pelanggan mulai belanja, maka akan diberikan keranjang belanja yang masih kosong. Untuk itu pelanggan akan diberikan pilihan menu untuk memulai belanja. Jika pelanggan sudah memasukkan barang, maka keranjang belanjanya akan mulai terisi,sehingga menu perubahan barang, penghapusan barang dan cek pesanan akan dimunculkan.

![image](https://user-images.githubusercontent.com/116284597/216740745-543a901b-f8c3-4391-b827-e04e5873ec08.png)

Untuk panambahan item baru, flownya sebagai berikut

![image](https://user-images.githubusercontent.com/116284597/216740782-73f3380f-f00f-4375-aeba-a121f2632949.png)

Nama barang harus berbeda dengan nama barang lain yang ada di keranjang belanja. Untuk jumlah dan harga barang harus berupa angka. Jika semua sudah benar, akan dimasukkan ke keranjang belanja, ditampilkan dan dimunculkan menu agar pelanggan bisa melakukan proses lainnya.

Terkait perubahan nama, jumlah, atau harga barang dalam keranjang belanja, alurnya dapat dilihat pada diagram dibawah ini.

![image](https://user-images.githubusercontent.com/116284597/216740839-45262416-2b24-48bb-83e7-456806bab15d.png)

Pelanggan harus memilih nomor item barang yang akan dilakukan perubahan. Nomor item harus berupa angka integer. Jika sudah benar, pelanggan akan diminta input data perubahan nama/jumlah/harga barang. Setelah dicek benar, maka keranjang belanja diupdate, ditampilkan dan dimunculkan menu agar pelanggan bisa melakukan proses lainnya.

Untuk penghapusan item tertentu dalam keranjang belanja, diagram alurnya sebagai berikut:

![image](https://user-images.githubusercontent.com/116284597/216740892-cd048187-eb0e-4766-abb2-952a8ff13434.png)

Pelanggan harus menentukan nomor item barang yang akan dihapus. Jika sudah benar, akan dicek apakah nomor item tersebut ada di keranjang belanja. Jika tidak ada akan ditampilkan pesan item tersebut tidak ada sedangkan jika ada akan dikonfirmasi proses penghapusannya. Jika user mengkonfirmasi memang item tersebut akan dihapus, maka dilakukan penghapusan kemudian ditampilkan keranjang belanja yang terbaru dan juga menunya.

Bila pelanggan akan menghapus semua item dalam keranjang belanja, maka akan dikonfirmasi bahwa memang akan dihapus semua. Jika ya, keranjang belanja dikosongkan, kemudian ditampilkan keranjang belanja yang terupdate dan juga menunya. Diagram alur penghapusan semua item keranjang belanja dapat dilihat di gambar dibawah ini.

![image](https://user-images.githubusercontent.com/116284597/216741210-35417318-ceaa-40ef-a817-37c06b37f7f5.png)

Jika proses belanja sudah selesai dan pelanggan ingin melakukan cek pesanan, maka diagram alurnya sebagai berikut. Akan ditampilkan keranjang belanja lengkap dengan diskon dan total yang harus dibayar. Selanjutnya akan dikonfirmasi apakah pesanan sudah benar. Jika belum, silahkan direvisi, akan ditampilkan keranjang belanja dan menunya, sedangkan jika sudah silahkan dibayar, proses belanja dinyatakan selesai.

![image](https://user-images.githubusercontent.com/116284597/216741225-f605fada-0fae-4a6f-a8c7-7e594e47b6a4.png)

<h2>Script Development</h2>
Tahap selanjutnya adalah membuat script untuk mewujudkan aplikasi super cashier sesuai dengan feature dan diagram alur yang dibuat. Pembuatan script akan menggunakan bahasa pemrograman python, dalam bentuk class yang akan dijalankan pada program utama.  
Dibuat class dengan nama Transaction untuk menangani transaksi dalam super cashier. Jenis transaksi yang akan dilakukan tambah barang, ubah nama barang, ubah jumlah barang, ubah harga barang, hapus barang tertentu, hapus semua barang, dan cek pesanan. Untuk menangani hal tersebut, akan diinisialisasi variabel yang dipakai dan dibuat prosedur yang dibutuhkan. Prosedur-prosedur tersebut adalah:
<ul>
<li>satudigit, duadigit, tigadigit, dan terbilang untuk mengubah angka menjadi kata-kata
<li>isnumeric untuk mengecek apakah input yang diberikan berupa angka
<li>cek_item untuk mengecek apakah nomor item yang dipilih ada di keranjang belanja
<li>inputyatidak untuk memvalidasi apakah user memasukkan jawaban Y/y/T/t
<li>inputnumeric, inputinteger, inputnamabarang digunakan untuk menangani input angka, integer, nama barang dan melakukan pengecekan apakah inputnya sesuai yang seharusnya
<li>total_price untuk menghtung total nilai belanja dan diskonnya jika ada
<li>printcart untuk menampilkan daftar belanjaan dengan format tertentu
<li>add_item untuk menangani penambahan barang kedalam keranjang belanja
<li>delete_item untuk mengahapus item tertentu dalam keranjang belanja
<li>reset_transaction untuk mengahapus semua item dalam keranjang belanja
<li>update_item_price, update_item_qty, update_item_name untuk menangani perubahan harga, jumlah atau nama barang dalam keranjang belanja
</ul>

Penjelasan lebih detail untuk masing-masing procedure sebagai berikut:
<ul>
<li>satudigit: untuk mengubah angka satu digit menjadi kata-kata. Inputnya berupa angka yang panjangnya satu digit, outputnya berupa kata terbilang dari angka input.
<li>duadigit: untuk mengubah angka dua digit menjadi kata-kata. Inputnya berupa angka yang panjangnya dua digit. Untuk memproses satuan, angka memanggil fungsi satudigit. Outputnya berupa kata terbilang dari angka input.
<li>tigadigit: untuk mengubah angka tiga digit menjadi kata-kata. Inputnya berupa angka yang panjangnya tiga digit. Untuk memproses ratusan, angka memanggil fungsi duadigit. Outputnya berupa kata terbilang dari angka input.
<li>terbilang: untuk mengubah angka menjadi kata-kata. Inputnya berupa angka maksimal 999,999,999,999,999,999. Outputnya berupa kata terbilang dari angka input.
<li>isnumeric: untuk cek apakah input berupa float / integer atau bukan. Inputnya berupa angka yang akan dicek dan tipe yang dimaksud (float/int). Outputnya berupa true jika sesuai tipe yang dimaksud dan false jika tidak sesuai.
<li>cek_item: untuk cek apakah nomor item yang dipilih ada dalam keranjang belanja.Inputnya berupa nomoritem yang mempresentasikan barang di keranjang belanja. Outputnya berupa key dari barang di keranjang belanja atau kosong jika tidak ditemukan barangnya.
<li>inputyatidak: untuk minta input Y/T untuk konfirmasi suatu hal. Inputnya berupa deskripsi hal yang akan dikonfirmasi. Outputnya berupa karakter Y atau T.
<li>inputnumeric: untuk minta input numeric dengan batas tertentu. Inputnya berupa deskripsi dari input yang diminta dan batas angka maksimal yang dibolehkan. Outputnya berupa angka numerik yang diisikan.
<li>inputinteger: untuk minta input integer. Inputnya berupa keterangan dari input yang diminta. Outputnya berupa angka integer yang diisikan.
<li>inputnamabarang: untuk minta input nama barang berupa karakter dengan panjang maksimal yang ditentukan. Inputnya berupa keterangan dari input yang diminta, nama barang lama jika ada dan panjang maksimal karakter yang diperbolehkan. Outputnya berupa nama barang yang diisikan.
<li>total_price: untuk menghitung total harga di keranjang belanja dan juga diskonnya. Inputnya tidak ada, outputnya berupa total nilai barang di keranjang belanja dan diskonnya.
<li>printcart: untuk menampilkan isi keranjang belanja. Inputnya berupa tipe tampilan keranjang belanja apakah diskon dan total yang harus dibayar ditampilkan atau tidak. Outputnya berupa keranjang belanja yang dicetak di layer.
<li>add_item: untuk penambahan item baru di keranjang belanja. Inputnya nama_item untuk nama barang jumlah_item untuk jumlah barang dan harga_item untuk harga barang keranjang belanja akan diupdate dengan barang yang ditambahkan.
<li>delete_item: untuk hapus item barang tertentu di keranjang belanja. Inputnya  nama_item untuk nama barang yang akan dihapus barang di keranjang belanja dengan key sama dengan nama_item akan dihapus.
<li>reset_transaction: untuk hapus semua barang  di keranjang belanja. Inputnya tidak ada, barang di keranjang belanja akan dihapus semua.
<li>update_item_price: untuk update harga item barang tertentu di keranjang belanja. Inputnya nama_item sebagai nama barang dan update_harga_item sebagai harga baru barang tersebut. Barang di keranjang belanja dengan key sama dengan nama_item akan diupdate harganya menjadi update_harga_item.
<li>update_item_qty: untuk update jumlah barang tertentu di keranjang belanja. Inputnya nama_item sebagai nama barang dan update_jumlah_item sebagai jumlah baru barang tersebut. Barang di keranjang belanja dengan key sama dengan nama_item akan diupdate jumlahnya menjadi update_jumlah_item.
<li>update_item_name: untuk update nama barang tertentu di keranjang belanja. Inputnya nama_item sebagai nama barang dan update_nama_item sebagai nama baru barang tersebut. Barang di keranjang belanja dengan key sama dengan nama_item akan diupdate namanya menjadi update_nama_item.
</ul>

Dibuat juga main program untuk menampilkan menu dan memproses sesuai dengan menu yang dipilih. Menu akan ditampilkan terus selama pelanggan belum keluar dari proses belanja. Jika ada kesalahan, maka akan ditampilkan pesan kesalahan yang terjadi.

<h2>Application Demo</h2>

![image](https://user-images.githubusercontent.com/116284597/216741708-49707b4b-ddf6-4c60-a75d-9115fefefc94.png)

Ketika diajalankan pertama kali, akan ditampilkan menu super cashier. Untuk memulai belanja, pelanggan dapat memilih menu nomor 1. Akan ditampilkan form untuk tambah item.

![image](https://user-images.githubusercontent.com/116284597/216741726-c1cd252d-b271-4fef-b296-ed34966e631e.png)

Setelah di ENTER, akan ditampilkan keranjang belanja dan menunya.

![image](https://user-images.githubusercontent.com/116284597/216741740-fb275dd5-9911-4600-bf65-80bacc136683.png)

Untuk penambahan item berikutnya, pilih menu 1 kemudian tekan ENTER. Penambahan item akan langsung dimasukkan ke keranjang belanja.

![image](https://user-images.githubusercontent.com/116284597/216741767-cd96fe59-2981-47b9-bdd6-ff3d91471505.png)

Untuk menghapus item tertentu dalam keranjang belanja, pilih menu 5 kemudian tekan ENTER.

![image](https://user-images.githubusercontent.com/116284597/216741795-cdc3e494-f844-435d-8699-3893471f8bbe.png)

Jika sudah benar, tekan ENTER. Akan ditampilkan keranjang belanja yang terbaru.

![image](https://user-images.githubusercontent.com/116284597/216741815-cdd7d3b0-6745-4450-8019-6635bb1c68a9.png)

Untuk menghapus semua item, pilih menu 6 kemudian tekan ENTER.

![image](https://user-images.githubusercontent.com/116284597/216741829-02677176-5cbc-4625-b54a-8f5e8a326901.png)

Jika sudah yakin akan dihapus semua item di keranjang belanja, tekan ENTER. Akan ditampilkan keranjang belanja terbaru dan menunya.

![image](https://user-images.githubusercontent.com/116284597/216741852-a42a002e-a5e8-4260-95ec-74298b812a68.png)

Pelanggan dapat memasukkan lagi item barang yang ingin dibelinya. Jika dirasakan sudah semua, pelanggan bisa memilih menu nomor 7 untuk melakukan pengecekan pesanan. Akan ditampilkan keranjang belanja beserta diskonnya jika ada dan total pembayaran yang harus dibayar pelanggan.

![image](https://user-images.githubusercontent.com/116284597/216741877-83128344-5ad6-4cfb-8b61-b18a693a06b4.png)

Jika sudah benar, silahkan ketik Y dan tekan ENTER. Proses belanja menggunakan super cashier akan selesai dengan memberikan pesan mempersilahkan pelanggan  membayar belanjaannya.

![image](https://user-images.githubusercontent.com/116284597/216741888-bbf7167d-d583-4b9c-a53c-2f8205ac1a9f.png)


<h2>Conclusion</h2
Dengan aplikasi super cashier pelanggan dapat melakukan belanja secara mandiri dengan mudah dan akurat tanpa kendala yang berarti.

