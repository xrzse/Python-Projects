def countWords(lst):
    new = [i for i in lst if len(list(i)) == 5]
    return len(new)

print(countWords(["Heyth","Po","daywe"]))