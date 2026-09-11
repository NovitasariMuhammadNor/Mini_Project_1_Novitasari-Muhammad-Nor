# Mini_Project_1_Novitasari-Muhammad-Nor
Nama : Novitasari Muhammad Nor  
Nim : 2609116082

# *Penjelasan tentang flowchart dan sistem reservasi buku perpustakaan*

# flowchart 
- Penjelasan Rinci Flowchart Sistem Reservasi Buku
Start  
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

-Decision (valid?)  
Program memeriksa apakah input valid (1–5).

- Jika valid → lanjut ke proses sesuai pilihan.

- Jika tidak valid → tampilkan pesan “Pilihan salah, coba lagi” dan kembali ke menu.

- Pilihan 1 – Tambah Reservasi  
User mengisi judul buku, nama pemesan, dan tanggal reservasi.
Data disimpan ke list reservasi dengan status default “Menunggu”.
Output: “Reservasi ditambahkan!”

- Pilihan 2 – Lihat Semua Reservasi  
Program menampilkan seluruh isi list reservasi dalam format daftar.
Output: “Daftar reservasi”

- Pilihan 3 – Ubah Status Reservasi  
User memilih nomor reservasi yang ingin diubah, lalu memasukkan status baru (Menunggu/Selesai/Dibatalkan).
Program memperbarui tuple di list.
Output: “Status diubah!”

- Pilihan 4 – Hapus Reservasi  
User memilih nomor reservasi yang ingin dihapus.
Program menghapus tuple dari list.
Output: “Reservasi dihapus!”

- Pilihan 5 – Keluar  
Program menampilkan pesan “Keluar program” dan berhenti.
End of program.

- Selain itu (input salah)  
Jika user memasukkan angka selain 1–5, program menampilkan pesan “Pilihan salah, coba lagi” dan kembali ke menu utama.

- Kembali ke Menu  
Setelah setiap operasi (tambah, lihat, ubah, hapus, atau input salah), program kembali ke menu utama agar user bisa memilih lagi.
<img width="350" height="437" alt="Screenshot 2026-09-11 193013" src="https://github.com/user-attachments/assets/2c26ce35-c1f8-483c-8f80-69a9aa45aaf6" />

# sistem reservasi buku perpustakaan












