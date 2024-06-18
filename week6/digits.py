filename = "C:/Users/ibenc/OneDrive/Desktop/compsci1md3/digits"
file = open(filename)
linesum = []
for line in file:
    data = line.strip().split()
    data = [int(s) for s in data]
    avg = sum(data)/len(data)
    linesum.append(avg)

print(f"Overall average: {sum(linesum)/len(linesum):.2f}")

file.close()
