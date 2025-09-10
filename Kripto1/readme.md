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
1. Program menampilkan menu utama:
