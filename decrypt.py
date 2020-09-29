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
        # 32~63: +74
        g.write(chr(ord(file[i]) +74))
    elif ord(file[i])<=79 and ord(file[i])>=64:
        # 64~79: -15
        g.write(chr(ord(file[i]) -15))
    elif ord(file[i])<=100 and ord(file[i])>=80:
        # 80~100: +26
        g.write(chr(ord(file[i]) +26))
    elif ord(file[i])<=126 and ord(file[i])>=101:
        # 101~126: -53
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
