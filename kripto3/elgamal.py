# ElGamal sederhana (modular exponentiation)
# Note: ini contoh edukasi, bukan implementasi kriptografi aman!

def mod_pow(base, exp, mod):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("No modular inverse")
    return x % m

def elgamal_encrypt(plaintext_nums, p, g, y, k):
    a = mod_pow(g, k, p)
    s = mod_pow(y, k, p)  # shared secret
    ciphertext = [(a, (m * s) % p) for m in plaintext_nums]
    return ciphertext

def elgamal_decrypt(ciphertext, p, x):
    result = []
    for a, b in ciphertext:
        s = mod_pow(a, x, p)
        inv_s = mod_inv(s, p)
        m = (b * inv_s) % p
        result.append(m)
    return result

def text_to_num(text):
    return [ord(c) - ord('A') for c in text]

def num_to_text(nums):
    return ''.join(chr(n + ord('A')) for n in nums)

if __name__ == "__main__":
    p, g, x, k = 37, 3, 2, 15
    y = mod_pow(g, x, p)

    plaintext = "EZKRIPTOGRAFI"
    m = text_to_num(plaintext)

    print("Plaintext nums:", m)

    cipher = elgamal_encrypt(m, p, g, y, k)
    print("Ciphertext:", cipher)

    decrypted_nums = elgamal_decrypt(cipher, p, x)
    print("Decrypted nums:", decrypted_nums)
    print("Decrypted text:", num_to_text(decrypted_nums))
