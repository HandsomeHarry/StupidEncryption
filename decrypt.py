inFileName = input("Enter filename for encryption: ")
f = open(inFileName+".txt", "r")
file = f.read()
encryptedFile = ""
outFileName = input("Enter output filename: ")
g = open(outFileName+".encrypted", "w+")
tmp = 0

# ASCII Encryption
for i in range(len(file)):
    if ord(file[i])<=63 and ord(file[i])>=32:
        # 32~63: +63, becomes 95~126 (31)
        g.write(chr(ord(file[i]) +63))
    elif ord(file[i])<=79 and ord(file[i])>=64:
        # 64~79: +16, becomes 79~94 (15)
        g.write(chr(ord(file[i]) -15))
    elif ord(file[i])<=100 and ord(file[i])>=80:
        # 80~100: -22, becomes 58~78 (20)
        g.write(chr(ord(file[i]) +26))
    elif ord(file[i])<=126 and ord(file[i])>=101:
        # 101~126: -69, becomes 32~57 (25)
        g.write(chr(ord(file[i]) -53))
    else:
        # other crap
        g.write(file[i])
print("First stage of encryption completed")

# head-to-foot
goldilock = g.read()
for i in range(len(goldilock)):
    g.write(goldilock[len(goldilock)-i-1])

g.write("Get out! You shouldn't be here!")
g.close()
