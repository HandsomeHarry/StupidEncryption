# Initialize
inFileName = input("Enter filename for decryption (.encrypted file): ") #string
f = open(inFileName+".encrypted", "r").read().replace("Get out! You shouldn't be here!", '') #string
open(inFileName+".encrypted", "w").write(f)
f = open(inFileName+".encrypted", "r").read() #string
outFileName = input("Enter output filename: ") #string
g = open(outFileName+".txt", "w+") #file
arr = [] #array

# Ask for input
print("Please enter the decryption keys for this file")
arr.append(int(input("first key: ")) + 33)
arr.append(int(input("second key: ")) + 33)
arr.append(int(input("third key: ")) + 33)

# Bubble sort the inputs
for i in range(1, len(arr)):
    for j in range(0, len(arr)-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# Make variables
a = arr[0] #integer
b = arr[1]
c = arr[2]

# Check if key is correct
key1 = int(f[0:2]) #integer
key2 = int(f[2:4])
key3 = int(f[4:6])

if a!=key1 or b!=key2 or c!=key3:
    print("Invalid decryption key!")
    exit(0)
else:
    print("Decryption key accepted!")

# ASCII Decryption (Still working on it)
print("Decrypting...")
for i in range(len(f)):
    if ord(f[i])<=a and ord(f[i])>=32:
        # 32~a: +126-a, becomes 158-a~126 (a-32)
        g.write(chr(ord(f[i]) + 126 - a))
    elif ord(f[i])<=b and ord(f[i])>=a+1:
        # a+1~b: -b-a+157, becomes 158-b~157-a (b-a-1)
        g.write(chr(ord(f[i]) - b - a + 157))
    elif ord(f[i])<=c and ord(f[i])>=b+1:
        # b+1~c: c+b-157, becomes 158-c~157-b (c-b-1)
        g.write(chr(ord(f[i]) + c + b - 157))
    elif ord(f[i])<=126 and ord(f[i])>=c+1:
        # c+1~126: +31-c, becomes 32~157-c (126-c)
        g.write(chr(ord(f[i]) + 31 - c))
    else:
        # other crap (unchanged)
        g.write(f[i])

g.close()
print("Decryption completed, file", outFileName + ".txt", "has been created!")
