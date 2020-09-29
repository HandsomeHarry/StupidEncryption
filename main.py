inFileName = input("Enter filename for encryption: ")
f = open(inFileName+".txt", "r")
file = f.read()
encryptedFile = ""
outFileName = input("Enter output filename: ")
g = open(outFileName+".txt", "w+")
goldilock = g.read()
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
g.write("Get out! You shouldn't be here!")
print("First stage of encryption completed")

# head-to-foot
for i in range(len(file)):
    g.write(goldilock[len(file)-i-1])
print("Second stage of encryption completed")

g.close()
