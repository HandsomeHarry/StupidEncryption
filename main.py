fileName = input("Enter file name for encryption: ")
f = open(fileName, "r")
file = f.read()
encryptedFile = ""
g = open("out.txt", "w")
tmp = 0
# head-to-foot
for i in range(len(file)):
    g.write(file[len(file)-i-1])
print("First stage of encryption completed")
# ASCII-20
h = g
for i in range(len(file)):
    h.write(file[len(file)-i-1])
