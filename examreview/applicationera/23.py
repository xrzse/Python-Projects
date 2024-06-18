def lefileop(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            counta = 0
            for line in file:
                data = line.lower().strip().split()
                for l in data:
                    if "spam" in l or "eggs" in l:
                        counta += 1
            return counta
    except FileNotFoundError:
        return False
    except UnicodeDecodeError:
        print("Error: Unable to decode the file. Please check the file encoding.")
        return False

filename = "examreview/applicationera/forthislifeicannotchange"
print(lefileop(filename))
