# Sistem Reservasi Buku Perpustakaan
# Data disimpan dalam list berisi tuple

reservasi = [ ("Algoritma Pemrograman", "vita", "2026-09-11", "Menunggu"),
    ("Basis Data", "Andi", "2026-09-12", "Selesai"),
    ("Jaringan Komputer", "jungkook", "2026-09-13", "Menunggu") 
    ]

def tambah_reservasi(): 
    judul = input("masukan judul buku: ")
    nama = input("masukan nama pemesan: ")
    tanggal = input("masukan tanggal reservasi (YYYY-MM-DD): ")
    status = "menunggu"
    reservasi.append((judul, nama, tanggal, status))
    print("reservasi telah berhasil ditambahkan!\n")

def lihat_reservasi():
    if not reservasi:
        print("belum ada data reservasi.\n")
    else :
        print("daftar reservas: ")
        for i, data in enumerate(reservasi):
            print(f"{i+1}. judul: {data[0]} , nama: {data[1]} , tanggal: {data[2]} , status: {data[3]}")
            print()

def ubah_status():
    if not reservasi: 
        print("tidak ada data yang mau diubah.\n")
        return
    lihat_reservasi()
    try:
        index = int(input("pilih nomor reservasi yang ingin diubah statusnya: ")) - 1
        if 0 <= index < len(reservasi):
            status_baru = input("masukan status baru (menunggu/selesai/dibatalkan): ")
            judul, nama, tanggal, _ = reservasi[index]
            reservasi[index] = (judul, nama, status_baru)
            print("status telah berhasil diubah!\n")
        else:
            print("nomor reservasi tidak valid.\n")
    except ValueError:
        print("input harus berupa angka.\n")

def hapus_reservasi():
    if not reservasi:
        print("tidak ada data yang mau dihapus.\n")
        return
    lihat_reservasi()
    try:
        index = int(input("pilih nomor reservasi yang ingin dihapus: ")) - 1
        if 0 <= index < len(reservasi):
            reservasi.pop(index)
            print("reservasi telah berhasil dihapus!\n")
        else:
            print("nomor reservasi tidak valid.\n")
    except ValueError:
        print("input harus berupa angka.\n")

while True:
    print(">>>> SISTEM RESERVASI BUKU PERPUSTAKAAN <<<< ")
    print("1. tambahkan reservasi")
    print("2. lihat reservasi")
    print("3. ubah status reservasi")
    print("4. hapus reservasi")
    print("5. keluar")

    pilih = input("pilih menu (1-5): ")

    if pilih == "1" :
        tambah_reservasi()
    elif pilih == "2" :
        lihat_reservasi()
    elif pilih == "3" :
        ubah_status()
    elif pilih == "4" :
        hapus_reservasi()
    elif pilih == "5" :
        print("terimakasih! program selesai.")
        break
    else:
        print("pilihan tidak valid, silahkan coba lagi.\n")
        