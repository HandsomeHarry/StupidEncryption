file = open(input("Enter filename for encryption (.txt file): ")+".txt", "r").read()
outFileName = input("Enter output filename: ")
g = open(outFileName+".encrypted", "w+")

# ASCII Encryption
for i in range(len(file)):
    if ord(file[i])<=63 and ord(file[i])>=32:
        # 32~63: +63, becomes 95~126 (31)
        g.write(chr(ord(file[i]) + 63))
    elif ord(file[i])<=79 and ord(file[i])>=64:
        # 64~79: +15, becomes 79~94 (15)
        g.write(chr(ord(file[i]) + 15))
    elif ord(file[i])<=100 and ord(file[i])>=80:
        # 80~100: -22, becomes 58~78 (20)
        g.write(chr(ord(file[i]) - 22))
    elif ord(file[i])<=126 and ord(file[i])>=101:
        # 101~126: -69, becomes 32~57 (25)
        g.write(chr(ord(file[i]) - 69))
    else:
        # other crap (unchanged)
        g.write(file[i])

g.write("Get out! You shouldn't be here!")
print("Encryption completed, file", outFileName + ".encrypted", "has been created!")
g.close()
