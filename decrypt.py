def vigenere_decrypt(ciphertext, key):
    def letter_to_num(letter):
        return ord(letter.upper()) - ord('A')
    def num_to_letter(num):
        return chr((num % 26) + ord('A'))

    decrypted = ""
    key_length = len(key)
    for i, c in enumerate(ciphertext):
        c_num = letter_to_num(c)
        k_num = letter_to_num(key[i % key_length])
        p_num = (c_num - k_num) % 26
        decrypted += num_to_letter(p_num)
    return decrypted

# Example use:
ciphertext = "OBKRUOXOGHULBSOLIFBWFLRVQQPRNGKSNSRKZWTGAAOSPWUOIYRFSGVNLINNLKWHLKDMR"
key = "GONSCTGB"
print(vigenere_decrypt(ciphertext, key))
