f = open(input("Enter filename for encryption (.txt file): ")+".txt", "r").read()
outFileName = input("Enter output filename: ")
g = open(outFileName+".encrypted", "w+")

# ASCII Encryption
print("Encrypting...")
for i in range(len(f)):
    if ord(f[i])<=63 and ord(f[i])>=32:
        # 32~63: +63, becomes 95~126 (31)
        g.write(chr(ord(f[i]) + 63))
    elif ord(f[i])<=79 and ord(f[i])>=64:
        # 64~79: +15, becomes 79~94 (15)
        g.write(chr(ord(f[i]) + 15))
    elif ord(f[i])<=100 and ord(f[i])>=80:
        # 80~100: -22, becomes 58~78 (20)
        g.write(chr(ord(f[i]) - 22))
    elif ord(f[i])<=126 and ord(f[i])>=101:
        # 101~126: -69, becomes 32~57 (25)
        g.write(chr(ord(f[i]) - 69))
    else:
        # other crap (unchanged)
        g.write(f[i])

g.write("Get out! You shouldn't be here!")
g.close()
print("Encryption completed, file", outFileName + ".encrypted", "has been created!")
