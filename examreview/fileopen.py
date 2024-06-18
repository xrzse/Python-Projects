filename = "examreview/myfile"
file = open(filename, "r")

data = file.readline()
print(data)
file.close()