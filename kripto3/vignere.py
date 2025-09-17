# Vigenere Cipher sederhana
# A = 0 ... Z = 25

def text_to_num(text):
    return [ord(c) - ord('A') for c in text]

def num_to_text(nums):
    return ''.join(chr(n + ord('A')) for n in nums)

def vigenere_encrypt(plaintext, key):
    p = text_to_num(plaintext)
    k = text_to_num(key)
    c = []
    for i in range(len(p)):
        val = (p[i] + k[i % len(k)]) % 26
        c.append(val)
    return num_to_text(c)

def vigenere_decrypt(ciphertext, key):
    c = text_to_num(ciphertext)
    k = text_to_num(key)
    p = []
    for i in range(len(c)):
        val = (c[i] - k[i % len(k)]) % 26
        p.append(val)
    return num_to_text(p)

if __name__ == "__main__":
    plaintext = "ASPRAKGANTENG"
    key = "FADHLI"

    cipher = vigenere_encrypt(plaintext, key)
    print("Ciphertext:", cipher)

    result = vigenere_decrypt(cipher, key)
    print("Decrypted:", result)
