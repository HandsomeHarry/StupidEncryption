fileName = input("Enter file name for encryption: ")
f = open(fileName, "r")
file = f.read()
encryptedFile = ""
g = open("out.txt", "w")
for i in range(len(file)):
    g.write(file[len(file)-i-1])
print("Write success!")
