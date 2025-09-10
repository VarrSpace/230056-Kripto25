import numpy as np
from math import gcd
from itertools import combinations

def inv_mod(a, m=26):
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def text_to_num(text):
    t = text.upper().replace(" ", "")
    return [ord(c) - 65 for c in t if c.isalpha()]

def num_to_text(nums):
    return ''.join(chr(x % 26 + 65) for x in nums)

def make_blocks(nums, n):
    if not nums:
        return []
    blocks = [nums[i:i+n] for i in range(0, len(nums), n)]
    if len(blocks[-1]) < n:
        blocks[-1] += [0] * (n - len(blocks[-1]))
    return blocks

def hill_encrypt(pt, key):
    if key.shape[0] != key.shape[1]:
        return None
    n = key.shape[0]
    blocks = make_blocks(text_to_num(pt), n)
    if not blocks:
        return None
    enc = []
    for b in blocks:
        enc.extend(key.dot(np.array(b)) % 26)
    return num_to_text(enc)

def hill_decrypt(ct, key):
    if key.shape[0] != key.shape[1]:
        return None
    n = key.shape[0]
    det = int(round(np.linalg.det(key)))
    inv_det = inv_mod(det % 26)
    if inv_det is None or gcd(det, 26) != 1:
        return None
    key_inv = (inv_det * np.round(det * np.linalg.inv(key)).astype(int)) % 26
    blocks = make_blocks(text_to_num(ct), n)
    if not blocks:
        return None
    dec = []
    for b in blocks:
        dec.extend(key_inv.dot(np.array(b)) % 26)
    return num_to_text(dec)

def find_key(pt, ct, n):
    P = np.array(make_blocks(text_to_num(pt), n)).T
    C = np.array(make_blocks(text_to_num(ct), n)).T
    if P.shape != C.shape or P.size == 0:
        return None
    for cols in combinations(range(P.shape[1]), n):
        P_sub, C_sub = P[:, cols], C[:, cols]
        detP = int(round(np.linalg.det(P_sub)))
        inv_detP = inv_mod(detP % 26)
        if inv_detP is None:
            continue
        P_inv_mod = (inv_detP * np.round(detP * np.linalg.inv(P_sub)).astype(int)) % 26
        return (C_sub.dot(P_inv_mod)) % 26
    return None

def get_matrix(n):
    key = []
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Baris {i+1}: ").split()))
                if len(row) != n:
                    print(f"Masukkan tepat {n} angka.")
                    continue
                key.append(row)
                break
            except ValueError:
                print("Input harus berupa angka.")
    return np.array(key)

while True:
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Cari Kunci")
    print("0. Keluar")
    pilih = input("Pilih: ").strip()
    if pilih == "1":
        pt = input("Plaintext: ").strip()
        if not pt:
            print("Plaintext kosong.")
            continue
        try:
            n = int(input("Ukuran matriks kunci (n): "))
            if n <= 0:
                print("Ukuran harus positif.")
                continue
        except ValueError:
            print("Ukuran tidak valid.")
            continue
        key = get_matrix(n)
        ct = hill_encrypt(pt, key)
        if ct:
            print("Ciphertext:", ct)
        else:
            print("Enkripsi gagal.")
    elif pilih == "2":
        ct = input("Ciphertext: ").strip()
        if not ct:
            print("Ciphertext kosong.")
            continue
        try:
            n = int(input("Ukuran matriks kunci (n): "))
            if n <= 0:
                print("Ukuran harus positif.")
                continue
        except ValueError:
            print("Ukuran tidak valid.")
            continue
        key = get_matrix(n)
        pt = hill_decrypt(ct, key)
        if pt:
            print("Plaintext:", pt)
        else:
            print("Dekripsi gagal. Kunci tidak valid.")
    elif pilih == "3":
        pt = input("Plaintext: ").strip()
        ct = input("Ciphertext: ").strip()
        if not pt or not ct:
            print("Plaintext atau Ciphertext kosong.")
            continue
        try:
            n = int(input("Ukuran matriks kunci (n): "))
            if n <= 0:
                print("Ukuran harus positif.")
                continue
        except ValueError:
            print("Ukuran tidak valid.")
            continue
        K = find_key(pt, ct, n)
        if K is not None:
            print("Matriks Kunci:\n", K.astype(int))
        else:
            print("Kunci tidak ditemukan.")
    elif pilih == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan salah.")
