# Mini_Project_1_Novitasari-Muhammad-Nor
# Nama : Novitasari Muhammad Nor  
# Nim : 2609116082

# *Penjelasan tentang flowchart dan sistem reservasi buku perpustakaan*

- # flowchart 
- Penjelasan Rinci Flowchart Sistem Reservasi Buku Perpustakaan yaitu
Start  pertama
- Program dimulai dan siap menjalankan proses utama.

- Inisialisasi list reservasi = []  
Membuat list kosong bernama reservasi untuk menyimpan data pemesanan buku.
Setiap data reservasi akan disimpan dalam bentuk tuple (judul, nama, tanggal, status).

- While True  
Program masuk ke perulangan tak terbatas agar menu selalu muncul kembali setelah satu operasi selesai.
Loop ini berhenti hanya jika user memilih keluar.

- Tampilkan Menu  
Program menampilkan pilihan:

1. Tambah Reservasi

2. Lihat Semua Reservasi

3. Ubah Status Reservasi

4. Hapus Reservasi

5. Keluar

- Input Pilihan  
User memasukkan angka sesuai menu yang diinginkan.

- Decision (valid?)  
Program memeriksa apakah input valid (1-5).

- Jika valid : lanjut ke proses sesuai pilihan.

- Jika tidak valid : tampilkan pesan Pilihan salah, coba lagi dan kembali ke menu.

- Pilihan 1 Tambah Reservasi  
User mengisi judul buku, nama pemesan, dan tanggal reservasi.
Data disimpan ke list reservasi dengan status default Menunggu.
Output: Reservasi ditambahkan!

- Pilihan 2 Lihat Semua Reservasi  
Program menampilkan seluruh isi list reservasi dalam format daftar.
Output: Daftar reservasi

- Pilihan 3 Ubah Status Reservasi  
User memilih nomor reservasi yang ingin diubah, lalu memasukkan status baru (Menunggu/Selesai/Dibatalkan).
Program memperbarui tuple di list.
Output:Status diubah

- Pilihan 4 Hapus Reservasi  
User memilih nomor reservasi yang ingin dihapus.
Program menghapus tuple dari list.
Output:Reservasi dihapus

- Pilihan 5 Keluar  
Program menampilkan pesan Keluar program dan berhenti.
End of program.

- Selain itu (input salah)  
Jika user memasukkan angka selain 1-5, program menampilkan pesan Pilihan salah, coba lagi dan kembali ke menu utama.

- Kembali ke Menu  
Setelah setiap operasi (tambah, lihat, ubah, hapus, atau input salah), program kembali ke menu utama agar user bisa memilih lagi.
<img width="350" height="437" alt="Screenshot 2026-09-11 193013" src="https://github.com/user-attachments/assets/2c26ce35-c1f8-483c-8f80-69a9aa45aaf6" />

- # Sistem Reservasi Buku Perpustakaan

Bagian awal program berfungsi untuk menyiapkan data reservasi buku yang akan digunakan dalam sistem.
Data disimpan dalam bentuk list berisi tuple, karena setiap tuple merepresentasikan satu reservasi lengkap.

<img width="602" height="123" alt="image" src="https://github.com/user-attachments/assets/8d8a791a-e500-412e-ba5a-62abfec7594f" />


- lihat_reservasi()  
Menampilkan seluruh data reservasi yang tersimpan di list.
Kalau list kosong, program menampilkan pesan Belum ada data reservasi.  
Tujuannya supaya pengguna bisa melihat semua data yang sudah ditambahkan.

- ubah_status()  
Mengubah status reservasi tertentu.
Pengguna memilih nomor reservasi, lalu memasukkan status baru (Menunggu/Selesai/Dibatalkan).
Program memperbarui tuple di list dan menampilkan pesan Status berhasil diubah!  
Ada validasi supaya input salah tidak bikin error.

- hapus_reservasi()  
Menghapus data reservasi berdasarkan nomor yang dipilih.
Kalau nomor tidak valid, muncul pesan Nomor reservasi tidak valid. 
Kalau berhasil, muncul Reservasi berhasil dihapus

- Menu utama  
Bagian while True yang menampilkan pilihan 1-5 dan memanggil fungsi sesuai input.
Kalau input salah, muncul pesan Pilihan tidak valid, silakan coba lagi.  
Ini bagian yang memastikan looping berjalan dan program tidak crash.

<img width="589" height="118" alt="image" src="https://github.com/user-attachments/assets/ca2455a9-d444-4c2f-a760-914436998df3" />


- Fungsi ini dipakai untuk menampilkan daftar reservasi yang tersimpan di list reservasi.
Kalau list kosong, program menulis belum ada data reservasi.  
Kalau ada isinya, program menampilkan semua data satu per satu dengan format:
<img width="689" height="120" alt="image" src="https://github.com/user-attachments/assets/d95f367d-aeeb-4be9-97ca-87991f503cc0" />

- Loop enumerate() dipakai supaya tiap data punya nomor urut otomatis.
Tujuannya biar pengguna bisa melihat semua reservasi dengan rapi dan tahu kalau belum ada data sama sekali.


<img width="651" height="233" alt="image" src="https://github.com/user-attachments/assets/810f522b-8d05-492e-bec9-9335b1212002" />

- Fungsi ini dipakai untuk mengubah status reservasi yang sudah ada di list reservasi.
Langkah kerjanya:

Pertama, dicek apakah list kosong. Kalau kosong, muncul pesan tidak ada data yang mau diubah.

Kalau ada data, program menampilkan daftar reservasi lewat lihat_reservasi().

User memilih nomor reservasi yang ingin diubah, lalu memasukkan status baru (menunggu/selesai/dibatalkan).

Program mengganti status lama dengan status baru dan menampilkan pesan status telah berhasil diubah!.

Ada validasi: kalau nomor tidak valid atau input bukan angka, muncul pesan nomor reservasi tidak valid atau input harus berupa angka.


<img width="650" height="203" alt="image" src="https://github.com/user-attachments/assets/0f27edf0-f1d3-44ae-ada8-f0f064c06e23" />

- Fungsi ini dipakai untuk menghapus data reservasi dari list reservasi.
Langkah kerjanya:

Pertama dicek apakah list kosong. Kalau kosong, muncul pesan tidak ada data yang mau dihapus.

Kalau ada data, program menampilkan daftar reservasi lewat lihat_reservasi().

User memilih nomor reservasi yang ingin dihapus.

Program memeriksa apakah nomor valid, lalu menghapus data dengan reservasi.pop(index) dan menampilkan pesan reservasi telah berhasil dihapus!.

Kalau nomor tidak valid atau input bukan angka, muncul pesan nomor reservasi tidak valid atau input harus berupa angka.


<img width="626" height="145" alt="image" src="https://github.com/user-attachments/assets/5245aaf6-c745-4f94-aee5-935a1678446f" />

- Bagian ini adalah menu utama program yang terus berulang sampai pengguna memilih keluar.
Setiap kali loop berjalan, program menampilkan judul sistem dan lima pilihan menu:
1. Tambahkan reservasi

2. Lihat reservasi

3. Ubah status reservasi

4. Hapus reservasi

5. Keluar
Setelah itu, pengguna diminta memasukkan angka lewat input("pilih menu (1-5): ").
Nilai input ini nanti dipakai untuk menentukan fungsi mana yang dijalankan (tambah, lihat, ubah, hapus, atau keluar).
Tujuannya supaya program tetap aktif dan bisa menerima perintah berulang tanpa harus dijalankan ulang setiap kali.


<img width="641" height="200" alt="image" src="https://github.com/user-attachments/assets/13fbbbb9-d812-4342-af8f-a8d72d203f9a" />

- Potongan ini adalah logika pemilihan menu utama dari sistem reservasi.
Setelah pengguna memasukkan angka pilihan (1-5), program akan menjalankan fungsi sesuai angka tersebut:

1. memanggil tambah_reservasi() untuk menambah data baru.

2. memanggil lihat_reservasi() untuk menampilkan daftar reservasi.

3. memanggil ubah_status() untuk mengubah status reservasi.

4. memanggil hapus_reservasi() untuk menghapus data reservasi.

5. menampilkan pesan terimakasih! program selesai. lalu keluar dari loop dengan break.

Selain itu  menampilkan pesan pilihan tidak valid, silahkan coba lagi.
Tujuannya supaya setiap input dari pengguna langsung diarahkan ke fungsi yang sesuai, dan program tetap berjalan dengan aman sampai pengguna memilih keluar.

# Terminalnya

1. pertama tambah reservasi
<img width="640" height="216" alt="image" src="https://github.com/user-attachments/assets/dbcab90c-302e-4f22-b258-b7d129973610" />

2. kedua lihat reservasi
<img width="644" height="155" alt="image" src="https://github.com/user-attachments/assets/64f73a88-0091-4b84-b051-4308d1d720eb" />

3. ketiga ubah status
<img width="648" height="257" alt="image" src="https://github.com/user-attachments/assets/a3a3832d-7db4-4d9d-871b-e7887d2c88b9" />

4. keempat hapus reservasi
<img width="643" height="251" alt="image" src="https://github.com/user-attachments/assets/63bece71-ec50-4e65-9dd6-0e4eefed7136" />

5. kelima keluar atau kembali ke menu awal
<img width="650" height="119" alt="image" src="https://github.com/user-attachments/assets/e6c4d20a-d827-44e8-bf49-a49b71f7c9d0" />

*berikut yang diatas adalah penjelasan saya tentang flowchart dan sistem reservasi buku perpustakaan, baik sekian dari saya jikalau ada salah kata maupun ketikan saya mohon maaf, dan jikalau ketikan saya susah untuk dipahami saya juga minta maaf sekian dari saya terimakasih banyak:)*


