inFileName = input("Enter filename for encryption: ")
f = open(inFileName+".txt", "r")
file = f.read()
encryptedFile = ""
outFileName = input("Enter output filename: ")
g = open(outFileName+".txt", "w")
tmp = 0
# ASCII-32, ASCII+62
for i in range(len(file)):
    if ord(file[i])<=126 and ord(file[i])>=64:
        g.write(chr(ord(file[i]) - 32))
    elif ord(file[i])<=63 and ord(file[i])>=32:
        g.write(chr(ord(file[i]) + 62))
    else:
        g.write(file[i])
print("First stage of encryption completed")
# head-to-foot
h = g
for i in range(len(file)):
    h.write(file[len(file)-i-1])
print("Second stage of encryption completed")
# Save file
