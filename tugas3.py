import cv2
import os

# Folder tempat citra asli
folder_citra = "citra"

# Folder untuk menyimpan hasil
folder_hasil = "hasil"

# Membuat folder hasil jika belum ada
os.makedirs(folder_hasil, exist_ok=True)

# Memproses citra nomor 1 sampai 9
for i in range(1, 10):

    # Nama file citra
    nama_file = f"{i}.jpg"

    # Lokasi lengkap citra
    path_citra = os.path.join(folder_citra, nama_file)

    # Membaca citra
    citra = cv2.imread(path_citra)

    # Mengecek apakah citra berhasil dibaca
    if citra is None:
        print(f"Citra {i} tidak ditemukan!")
        continue

    # Mengubah citra warna menjadi grayscale
    grayscale = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)

    # Menyimpan citra grayscale
    path_grayscale = os.path.join(folder_hasil, f"grayscale_{i}.jpg")
    cv2.imwrite(path_grayscale, grayscale)

    print(f"Citra {i} berhasil diubah menjadi grayscale.")

print("Semua citra selesai diproses.")

# ============================================================
# TAHAP 2: MEMBUAT HISTOGRAM CITRA
# ============================================================

import matplotlib.pyplot as plt

# Memproses citra nomor 1 sampai 9
for i in range(1, 10):

    # Menentukan nama file citra
    nama_file = f"{i}.jpg"

    # Menentukan lokasi citra asli
    path_citra = os.path.join(folder_citra, nama_file)

    # Membaca citra asli
    citra = cv2.imread(path_citra)

    # Mengecek apakah citra berhasil dibaca
    if citra is None:
        print(f"Citra {i} tidak ditemukan!")
        continue

    # Mengubah citra berwarna menjadi grayscale
    grayscale = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)

    # Membuat gambar histogram dengan 2 bagian
    plt.figure(figsize=(12, 5))

    # ========================================================
    # HISTOGRAM CITRA ASLI
    # ========================================================

    plt.subplot(1, 2, 1)

    # Mengambil masing-masing kanal warna
    # OpenCV menggunakan urutan BGR
    kanal_b, kanal_g, kanal_r = cv2.split(citra)

    # Membuat histogram kanal Biru
    plt.hist(
        kanal_b.ravel(),
        bins=256,
        range=[0, 256],
        alpha=0.5,
        label="B (Blue)"
    )

    # Membuat histogram kanal Hijau
    plt.hist(
        kanal_g.ravel(),
        bins=256,
        range=[0, 256],
        alpha=0.5,
        label="G (Green)"
    )

    # Membuat histogram kanal Merah
    plt.hist(
        kanal_r.ravel(),
        bins=256,
        range=[0, 256],
        alpha=0.5,
        label="R (Red)"
    )

    # Memberikan judul dan nama sumbu
    plt.title(f"Histogram Citra Asli {i}")
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")

    # Menampilkan keterangan kanal
    plt.legend()

    # ========================================================
    # HISTOGRAM GRAYSCALE
    # ========================================================

    plt.subplot(1, 2, 2)

    # Membuat histogram citra grayscale
    plt.hist(
        grayscale.ravel(),
        bins=256,
        range=[0, 256]
    )

    # Memberikan judul dan nama sumbu
    plt.title(f"Histogram Grayscale {i}")
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")

    # Mengatur jarak antar grafik
    plt.tight_layout()

    # Menentukan nama file histogram
    nama_histogram = os.path.join(
        folder_hasil,
        f"histogram_{i}.png"
    )

    # Menyimpan histogram
    plt.savefig(nama_histogram)

    # Menutup gambar setelah disimpan
    plt.close()

    print(f"Histogram citra {i} berhasil dibuat.")

print("Semua histogram selesai dibuat.")

# ============================================================
# TAHAP 3: ANALISIS STATISTIK INTENSITAS CITRA
# ============================================================

import numpy as np

# Memproses citra nomor 1 sampai 9
for i in range(1, 10):

    # Menentukan nama file citra
    nama_file = f"{i}.jpg"

    # Menentukan lokasi citra
    path_citra = os.path.join(folder_citra, nama_file)

    # Membaca citra asli
    citra = cv2.imread(path_citra)

    # Mengecek apakah citra berhasil dibaca
    if citra is None:
        print(f"Citra {i} tidak ditemukan!")
        continue

    # Mengubah citra menjadi grayscale
    grayscale = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)

    # Menghitung nilai intensitas minimum
    nilai_min = np.min(grayscale)

    # Menghitung nilai intensitas maksimum
    nilai_max = np.max(grayscale)

    # Menghitung nilai rata-rata intensitas
    nilai_mean = np.mean(grayscale)

    # Menghitung standar deviasi
    nilai_std = np.std(grayscale)

    # Menampilkan hasil analisis
    print(f"\nCitra {i}")
    print(f"  Intensitas minimum : {nilai_min}")
    print(f"  Intensitas maksimum : {nilai_max}")
    print(f"  Intensitas rata-rata : {nilai_mean:.2f}")
    print(f"  Standar deviasi : {nilai_std:.2f}")

    # ============================================================
# TAHAP 4: MENYIMPAN HASIL ANALISIS INTENSITAS
# ============================================================

# Menentukan nama file untuk menyimpan hasil analisis
file_analisis = os.path.join(
    folder_hasil,
    "analisis_intensitas.txt"
)

# Membuka file dalam mode tulis
with open(file_analisis, "w", encoding="utf-8") as file:

    # Menuliskan judul
    file.write("ANALISIS INTENSITAS CITRA\n")
    file.write("=" * 40 + "\n\n")

    # Memproses citra 1 sampai 9
    for i in range(1, 10):

        # Menentukan lokasi citra
        nama_file = f"{i}.jpg"
        path_citra = os.path.join(folder_citra, nama_file)

        # Membaca citra
        citra = cv2.imread(path_citra)

        # Jika citra tidak ditemukan, lanjut ke citra berikutnya
        if citra is None:
            continue

        # Mengubah citra menjadi grayscale
        grayscale = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)

        # Menghitung statistik intensitas
        nilai_min = np.min(grayscale)
        nilai_max = np.max(grayscale)
        nilai_mean = np.mean(grayscale)
        nilai_std = np.std(grayscale)

        # Menuliskan hasil ke file
        file.write(f"Citra {i}\n")
        file.write(f"Intensitas minimum : {nilai_min}\n")
        file.write(f"Intensitas maksimum : {nilai_max}\n")
        file.write(f"Intensitas rata-rata : {nilai_mean:.2f}\n")
        file.write(f"Standar deviasi : {nilai_std:.2f}\n")
        file.write("\n")

print("Hasil analisis intensitas berhasil disimpan.")

# ============================================================
# TAHAP 5: ENHANCEMENT / PERBAIKAN CITRA
# ============================================================

# ------------------------------------------------------------
# Fungsi Contrast Stretching
# ------------------------------------------------------------

def contrast_stretching(citra):
    """
    Memperluas rentang intensitas citra
    agar kontras menjadi lebih baik.
    """

    # Mengubah tipe data menjadi float
    # agar perhitungan tidak mengalami overflow
    citra_float = citra.astype(np.float32)

    # Mencari nilai minimum dan maksimum piksel
    min_val = np.min(citra_float)
    max_val = np.max(citra_float)

    # Menghindari pembagian dengan nol
    if max_val == min_val:
        return citra

    # Melakukan contrast stretching
    hasil = (
        (citra_float - min_val)
        * 255
        / (max_val - min_val)
    )

    # Memastikan nilai berada pada rentang 0-255
    hasil = np.clip(hasil, 0, 255)

    # Mengubah kembali menjadi uint8
    hasil = np.uint8(hasil)

    return hasil

# ------------------------------------------------------------
# Fungsi CLAHE
# ------------------------------------------------------------

def clahe_enhancement(citra):
    """
    Meningkatkan kontras lokal menggunakan CLAHE.
    """

    # Membuat objek CLAHE
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    # Menerapkan CLAHE pada citra grayscale
    hasil = clahe.apply(citra)

    return hasil

# ------------------------------------------------------------
# Fungsi Gamma Correction
# ------------------------------------------------------------

def gamma_correction(citra, gamma=2.0):
    """
    Mengurangi kecerahan citra menggunakan Gamma Correction.
    Nilai gamma > 1 digunakan untuk citra yang terlalu terang.
    """

    # Membuat tabel perubahan nilai intensitas
    tabel = np.array([
        ((i / 255.0) ** gamma) * 255
        for i in range(256)
    ]).astype(np.uint8)

    # Menerapkan tabel gamma pada citra
    hasil = cv2.LUT(citra, tabel)

    return hasil

# ------------------------------------------------------------
# Memproses citra 1 sampai 9
# ------------------------------------------------------------

for i in range(1, 10):

    # Menentukan nama file
    nama_file = f"{i}.jpg"

    # Menentukan lokasi citra
    path_citra = os.path.join(folder_citra, nama_file)

    # Membaca citra
    citra = cv2.imread(path_citra)

    # Mengecek apakah citra berhasil dibaca
    if citra is None:
        print(f"Citra {i} tidak ditemukan!")
        continue

    # Mengubah citra menjadi grayscale
    grayscale = cv2.cvtColor(
        citra,
        cv2.COLOR_BGR2GRAY
    )

    # --------------------------------------------------------
    # Menentukan metode enhancement
    # --------------------------------------------------------
# --------------------------------------------------------
# Menentukan metode enhancement
# --------------------------------------------------------

    if i == 1:

        # Citra 1 memiliki kontras relatif rendah
        # sehingga menggunakan CLAHE
        hasil_enhancement = clahe_enhancement(grayscale)
        metode = "CLAHE"

    elif i == 9:

        # Citra 9 memiliki rentang intensitas yang sempit
        # sehingga menggunakan Contrast Stretching
        hasil_enhancement = contrast_stretching(grayscale)
        metode = "Contrast Stretching"

    else:

        # Citra 2 sampai 8 terlalu terang,
        # sehingga menggunakan Gamma Correction
        hasil_enhancement = gamma_correction(
            grayscale,
            gamma=3.0
        )

        # Menampilkan perbandingan rata-rata intensitas
        # sebelum dan sesudah Gamma Correction
        print(
            f"Citra {i} - Mean sebelum: "
            f"{np.mean(grayscale):.2f}"
        )

        print(
            f"Citra {i} - Mean sesudah Gamma: "
            f"{np.mean(hasil_enhancement):.2f}"
        )

        metode = "Gamma Correction"
    # --------------------------------------------------------
    # Menyimpan hasil enhancement
    # --------------------------------------------------------

    nama_hasil = os.path.join(
        folder_hasil,
        f"enhancement_{i}.jpg"
    )

    cv2.imwrite(
        nama_hasil,
        hasil_enhancement
    )

    print(
        f"Citra {i} berhasil di-enhancement "
        f"dengan metode {metode}."
    )

print("Semua citra selesai di-enhancement.")

# ============================================================
# TAHAP 6: HISTOGRAM SETELAH ENHANCEMENT
# ============================================================

# Memproses citra 1 sampai 9
for i in range(1, 10):

    # Menentukan nama file hasil enhancement
    nama_hasil = f"enhancement_{i}.jpg"

    # Menentukan lokasi file
    path_hasil = os.path.join(
        folder_hasil,
        nama_hasil
    )

    # Membaca citra hasil enhancement
    citra_enhancement = cv2.imread(
        path_hasil,
        cv2.IMREAD_GRAYSCALE
    )

    # Mengecek apakah file berhasil dibaca
    if citra_enhancement is None:
        print(
            f"Hasil enhancement citra {i} "
            "tidak ditemukan!"
        )
        continue

    # Membuat ukuran gambar histogram
    plt.figure(figsize=(8, 5))

    # Membuat histogram hasil enhancement
    plt.hist(
        citra_enhancement.ravel(),
        bins=256,
        range=[0, 256]
    )

    # Memberikan judul
    plt.title(
        f"Histogram Setelah Enhancement Citra {i}"
    )

    # Memberikan nama sumbu
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")

    # Mengatur tampilan
    plt.tight_layout()

    # Menentukan nama file histogram
    nama_histogram = os.path.join(
        folder_hasil,
        f"histogram_enhancement_{i}.png"
    )

    # Menyimpan histogram
    plt.savefig(nama_histogram)

    # Menutup grafik
    plt.close()

    print(
        f"Histogram enhancement citra {i} "
        "berhasil dibuat."
    )

print("Semua histogram setelah enhancement selesai dibuat.")