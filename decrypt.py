inFileName = input("Enter filename for decryption (.encrypted file): ")
f = open(inFileName+".encrypted", "r")
file = f.read()
decryptedFile = ""
outFileName = input("Enter output filename: ")
g = open(outFileName+".txt", "w+")

# ASCII Decryption
def decrypt(h):
    for i in range(len(file)):
        if ord(file[i])<=126 and ord(file[i])>=95:
            # 32~63: +63, becomes 95~126 (31)
            h.write(chr(ord(file[i]) - 63))
        elif ord(file[i])<=94 and ord(file[i])>=79:
            # 64~79: +15, becomes 79~94 (15)
            h.write(chr(ord(file[i]) - 15))
        elif ord(file[i])<=78 and ord(file[i])>=58:
            # 80~100: -22, becomes 58~78 (20)
            h.write(chr(ord(file[i]) + 22))
        elif ord(file[i])<=57 and ord(file[i])>=32:
            # 101~126: -69, becomes 32~57 (25)
            h.write(chr(ord(file[i]) + 69))
        else:
            # other crap (unchanged)
            h.write(file[i])

decrypt(h)
print("Decryption completed, file", outFileName + ".txt", "has been created!")
# How can the last line be deleted?
g.close()
