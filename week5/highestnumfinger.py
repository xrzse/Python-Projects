nums = [1,2,3,4,5,4,53,534,54,5,4]

bignum = 0
for i in nums:
    if i > bignum:
        bignum = i

print(bignum)



word = "hey"

print(word[-1])


words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for word in words:
    if word[-1] == "e":
        past_tense.append(word + "d")
    else:
        past_tense.append(word+"ed")
print(past_tense)