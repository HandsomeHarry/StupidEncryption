f = open(input("Enter filename for decryption (.encrypted file): ")+".encrypted", "r").read()
outFileName = input("Enter output filename: ")
g = open(outFileName+".txt", "w+")

# ASCII Decryption
print("Decrypting...")
for i in range(len(f)-31):
    if ord(f[i])<=126 and ord(f[i])>=95:
        # 32~63: +63, becomes 95~126 (31)
        g.write(chr(ord(f[i]) - 63))
    elif ord(f[i])<=94 and ord(f[i])>=79:
        # 64~79: +15, becomes 79~94 (15)
        g.write(chr(ord(f[i]) - 15))
    elif ord(f[i])<=78 and ord(f[i])>=58:
        # 80~100: -22, becomes 58~78 (20)
        g.write(chr(ord(f[i]) + 22))
    elif ord(f[i])<=57 and ord(f[i])>=32:
        # 101~126: -69, becomes 32~57 (25)
        g.write(chr(ord(f[i]) + 69))
    else:
        # other crap (unchanged)
        g.write(f[i])

g.close()
print("Decryption completed, file", outFileName + ".txt", "has been created!")
