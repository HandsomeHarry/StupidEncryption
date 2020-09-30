# Initialize
f = open(input("Enter filename for encryption (.txt file): ")+".txt", "r").read()
outFileName = input("Enter output filename: ")
g = open(outFileName+".encrypted", "w+")
arr = []

# Ask for input
print("Now you're going to enter 3 numbers to be the encryption key, between 0 and 66")
arr.append(int(input("Enter the first number: ")) + 33)
arr.append(int(input("Enter the second number: ")) + 33)
arr.append(int(input("Enter the third number: ")) + 33)

# Bubble sort the inputs
for i in range(1, len(arr)):
    for j in range(0, len(arr)-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# Make variables
a = arr[0]
b = arr[1]
c = arr[2]

# Check input
if a>99 or a<33 or b>99 or b<33 or c>99 or c<33:
    print("Invalid input!")
    exit(0)

# Put code in front of outFileName.encrypted
g.write(str(a))
g.write(str(b))
g.write(str(c))

# ASCII Encryption
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

g.write("Get out! You shouldn't be here!")
g.close()
print("Encryption completed, file", outFileName + ".encrypted", "has been created!")
