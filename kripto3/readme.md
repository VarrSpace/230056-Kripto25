
vigenere_cipher:
  - Program menggunakan prinsip substitusi huruf dengan kunci.
  - Plaintext dan kunci diubah menjadi huruf kapital.
  - Jika kunci lebih pendek dari plaintext, kunci diulang hingga sama panjang.
  - Enkripsi dilakukan dengan menambahkan posisi huruf plaintext dan huruf kunci, lalu hasilnya dimodulo 26.
  - Dekripsi dilakukan dengan mengurangi posisi huruf ciphertext dengan huruf kunci, lalu dimodulo 26.
  - Output program berupa ciphertext hasil enkripsi dan plaintext hasil dekripsi.

elgamal:
  - Program menggunakan konsep kriptografi kunci publik.
  - Parameter utama: bilangan prima p, generator g, kunci privat x, dan bilangan acak k.
  - Kunci publik dihitung dengan rumus y = g^x mod p.
  - Enkripsi plaintext dilakukan dengan:
      1. Mengubah huruf menjadi angka.
      2. Menghitung c1 = g^k mod p.
      3. Menghitung c2 = (m * y^k) mod p, dengan m = nilai angka huruf.
  - Ciphertext berupa pasangan (c1, c2).
  - Dekripsi dilakukan dengan rumus m = (c2 * (c1^x)^-1) mod p.
  - Output program berupa hasil enkripsi dalam angka dan hasil dekripsi kembali ke huruf.

tujuan:
  - Memberikan contoh implementasi kriptografi klasik (Vigenere) dan modern (ElGamal).
  - Menunjukkan perbedaan cara kerja antara substitusi sederhana dengan operasi eksponensial modular.
  - Membantu memahami alur enkripsi dan dekripsi melalui contoh program yang ringkas.
