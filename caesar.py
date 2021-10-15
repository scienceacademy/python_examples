alpha = "abcdefghijklmnopqrstuvwxyz"

shift = int(input("Shift: "))
clear = input("Cleartext: ").lower()
cipher = ""
for char in clear:
    n = (alpha.find(char) + shift) % 26
    cipher = cipher + alpha[n]
print(f"Ciphertext: {cipher}")