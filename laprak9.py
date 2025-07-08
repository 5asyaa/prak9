# Sistem Informasi Catatan Harian

catatan_harian = []  # List kosong untuk menyimpan catatan

users = {  # Data user untuk login
}

def login():  # Fungsi login
    print("=== Login ===")  # Tampilkan header login
    username = input("Username: ")  # Input username
    password = input("Password: ")  # Input password
    if username in users and users[username] == password:  # Verifikasi login
        print("✅ Login berhasil!\n")  # Jika benar, tampilkan pesan sukses
        return True  # Kembalikan True jika berhasil
    else:  # Jika username atau password salah
        print("❌ Username atau password salah.\n")  # Pesan gagal login
        return False  # Kembalikan False

def tambah_catatan():  # Fungsi tambah catatan
    tanggal = input("Tanggal (YYYY-MM-DD): ")  # Input tanggal
    kategori = input("Kategori: ")  # Input kategori catatan
    isi = input("Catatan: ")  # Input isi catatan
    catatan = {  # Buat dict catatan
        'tanggal': tanggal,  # Tanggal catatan
        'kategori': kategori.lower(),  # Kategori dalam huruf kecil
        'isi': isi  # Isi catatan
    }  # Akhir dict
    catatan_harian.append(catatan)  # Tambahkan catatan ke list
    print("Catatan ditambahkan.\n")  # Konfirmasi berhasil

def tampilkan_catatan():  # Fungsi tampilkan semua catatan
    if not catatan_harian:  # Jika list kosong
        print("Belum ada catatan.\n")  # Pesan tidak ada catatan
        return  # Kembali
    print("\n=== Daftar Catatan ===")  # Header daftar catatan
    for i, c in enumerate(catatan_harian, 1):  # Loop catatan
        print(f"{i}. [{c['tanggal']}] ({c['kategori']}) - {c['isi']}")  # Tampilkan
    print()  # Baris kosong

def cari_catatan():  # Fungsi cari catatan
    if not catatan_harian:  # Cek apakah ada catatan
        print("Belum ada catatan.\n")  # Tidak ada catatan
        return  # Kembali
    kategori = input("Cari kategori: ").lower()  # Input kategori cari
    hasil = [c for c in catatan_harian if c['kategori'] == kategori]  # Cari hasil
    if not hasil:  # Jika tidak ada hasil
        print("Tidak ditemukan.\n")  # Pesan tidak ditemukan
    else:  # Jika ditemukan
        print(f"\nHasil kategori '{kategori}':")  # Header hasil
        for i, c in enumerate(hasil, 1):  # Loop hasil
            print(f"{i}. [{c['tanggal']}] - {c['isi']}")  # Tampilkan
        print()  # Baris kosong

def hapus_catatan():  # Fungsi hapus catatan
    if not catatan_harian:  # Jika list kosong
        print("Belum ada catatan.\n")  # Pesan tidak ada
        return  # Kembali
    tampilkan_catatan()  # Tampilkan semua catatan
    try:  # Mulai blok try
        nomor = int(input("Nomor catatan yang dihapus: "))  # Input nomor
        if 1 <= nomor <= len(catatan_harian):  # Validasi nomor
            konfirmasi = input("Yakin hapus? (y/n): ").lower()  # Konfirmasi hapus
            if konfirmasi == 'y':  # Jika ya
                catatan_harian.pop(nomor - 1)  # Hapus catatan
                print("Catatan dihapus.\n")  # Konfirmasi hapus
            else:  # Jika tidak
                print("Batal hapus.\n")  # Pesan batal
        else:  # Jika nomor salah
            print("Nomor salah.\n")  # Pesan error
    except ValueError:  # Tangkap error jika input bukan angka
        print("Masukkan angka yang benar.\n")  # Pesan error

def menu_utama():  # Fungsi menu utama
    while True:  # Loop menu
        print("=== Menu Utama ===")  # Header menu
        print("1. Tambah Catatan")  # Opsi 1
        print("2. Lihat Catatan")  # Opsi 2
        print("3. Cari Catatan")  # Opsi 3
        print("4. Hapus Catatan")  # Opsi 4
        print("5. Logout")  # Opsi 5
        pilih = input("Pilih (1-5): ")  # Input pilihan
        if pilih == '1':  # Jika pilih 1
            tambah_catatan()  # Panggil fungsi tambah
        elif pilih == '2':  # Jika pilih 2
            tampilkan_catatan()  # Panggil fungsi tampil
        elif pilih == '3':  # Jika pilih 3
            cari_catatan()  # Panggil fungsi cari
        elif pilih == '4':  # Jika pilih 4
            hapus_catatan()  # Panggil fungsi hapus
        elif pilih == '6':
            tampilkan_grafik()
        elif pilih == '5':  # Jika pilih 5
            print("Logout...\n")  # Tampilkan pesan keluar
            break  # Keluar loop
        else:  # Jika salah input
            print("Pilihan tidak valid.\n")  # Pesan error

def menu_login():  # Fungsi menu login
    while True:  # Loop login
        print("=== Sistem Catatan Harian ===")  # Header
        print("1. Login")  # Opsi 1
        print("2. Keluar")  # Opsi 2
        pilih = input("Pilih (1-2): ")  # Input pilihan
        if pilih == '1':  # Jika pilih login
            if login():  # Jika login berhasil
                menu_utama()  # Masuk menu utama
            else:  # Jika login gagal
                continue  # Kembali ke login
        elif pilih == '2':  # Jika pilih keluar
            print("Terima kasih.\n")  # Pesan keluar
            break  # Keluar loop
        else:  # Jika salah input
            print("Pilihan tidak valid.\n")  # Pesan error

def tampilkan_grafik():
    import matplotlib.pyplot as plt

    if not catatan_harian:
        print("Belum ada catatan untuk ditampilkan dalam grafik.\n")
        return

    kategori_count = {}
    for c in catatan_harian:
        kategori = c['kategori']
        kategori_count[kategori] = kategori_count.get(kategori, 0) + 1

    plt.bar(kategori_count.keys(), kategori_count.values(), color='skyblue')
    plt.xlabel('Kategori')
    plt.ylabel('Jumlah Catatan')
    plt.title('Grafik Catatan per Kategori')
    plt.tight_layout()
    plt.show()

menu_login()  # Panggil menu login pertama kali
