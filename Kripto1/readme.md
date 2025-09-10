# Hill Cipher (Enkripsi, Dekripsi, dan Pencarian Kunci)

Program ini adalah implementasi algoritma **Hill Cipher** menggunakan Python dan `numpy`.  
Hill Cipher adalah algoritma kriptografi klasik berbasis **aljabar linear** dengan operasi matriks pada modulo 26 (alfabet A–Z).  

---

## Fitur Program
1. **Enkripsi**  
   - Mengubah plaintext menjadi ciphertext menggunakan matriks kunci.  
   - Plaintext diproses dalam blok-blok dengan ukuran sesuai matriks kunci.  

2. **Dekripsi**  
   - Mengubah ciphertext kembali menjadi plaintext dengan matriks kunci.  
   - Program otomatis menghitung **invers matriks modulo 26** jika memungkinkan.  
   - Jika matriks kunci tidak invertible, dekripsi gagal.  

3. **Cari Kunci**  
   - Menemukan matriks kunci berdasarkan pasangan plaintext dan ciphertext.  
   - Berguna untuk analisis kriptografi (known-plaintext attack).  

4. **Validasi Input**  
   - Menolak input kosong.  
   - Mengecek ukuran matriks agar positif.  
   - Memastikan setiap baris matriks memiliki jumlah angka sesuai ukuran.  
   - Menolak input non-angka pada matriks.  

---

## Alur Program

- Pengguna diminta memasukkan pilihan (`1`, `2`, `3`, atau `0`).

---

## 1. Enkripsi
Jika pengguna memilih **1 (Enkripsi)**:
1. Program meminta input **plaintext**.
2. Program meminta ukuran matriks kunci **n**.
3. Program meminta pengguna memasukkan matriks kunci ukuran `n × n` baris per baris.
4. Proses enkripsi:
 - Plaintext diubah menjadi angka (`A=0 ... Z=25`).
 - Teks angka dibagi ke dalam blok berukuran `n`.
 - Jika blok terakhir kurang panjang, ditambah angka `0` sebagai padding.
 - Setiap blok dikalikan dengan matriks kunci.
 - Hasil perkalian diambil **modulo 26**.
 - Angka hasil dikonversi kembali menjadi huruf.
5. Program menampilkan hasil **ciphertext**.

**Alur Ringkas:**
Plaintext → Ubah ke angka → Bagi blok → Kali matriks kunci (mod 26) → Ciphertext

---

## 2. Dekripsi
Jika pengguna memilih **2 (Dekripsi)**:
1. Program meminta input **ciphertext**.
2. Program meminta ukuran matriks kunci **n**.
3. Program meminta pengguna memasukkan matriks kunci ukuran `n × n` baris per baris.
4. Program menghitung:
   - Determinan matriks kunci.
   - Mengecek apakah determinan relatif prima dengan 26.
   - Jika valid, program membuat matriks invers modulo 26.
5. Proses dekripsi:
   - Ciphertext diubah menjadi angka (`A=0 ... Z=25`).
   - Dibagi ke dalam blok berukuran `n`.
   - Setiap blok dikalikan dengan matriks invers.
   - Hasil dikonversi kembali menjadi huruf.
6. Program menampilkan hasil **plaintext**.

Jika determinan matriks tidak relatif prima dengan 26 → matriks tidak punya invers, sehingga dekripsi gagal.

**Alur Ringkas:**
Ciphertext → Ubah ke angka → Hitung invers kunci (mod 26) → Bagi blok → Kali invers → Plaintext


---

## 3. Cari Kunci
Jika pengguna memilih **3 (Cari Kunci)**:
1. Program meminta input **plaintext**.
2. Program meminta input **ciphertext**.
3. Program meminta ukuran matriks kunci **n**.
4. Program membentuk:
   - Matriks **P** dari plaintext.
   - Matriks **C** dari ciphertext.
5. Program memilih kombinasi kolom untuk membentuk submatriks `P_sub` dan `C_sub` ukuran `n × n`.
6. Program menghitung:
   - Invers dari `P_sub` (mod 26).
   - Matriks kunci dengan rumus:
     ```
     K = (C_sub × P_sub⁻¹) mod 26
     ```
7. Jika berhasil, program menampilkan **matriks kunci**.
8. Jika tidak, program menampilkan pesan bahwa kunci tidak ditemukan.

**Alur Ringkas:**
Plaintext + Ciphertext → Bentuk matriks → Cari invers P_sub (mod 26) → Hitung Kunci → Output Matriks Kunci
