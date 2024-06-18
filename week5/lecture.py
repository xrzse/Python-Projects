mylist = [1,23,3,4,5,6,7]

threelist = mylist * 3 #[1, 23, 3, 4, 5, 6, 7, 1, 23, 3, 4, 5, 6, 7, 1, 23, 3, 4, 5, 6, 7]
threelist = [mylist] * 3 #[[1, 23, 3, 4, 5, 6, 7], [1, 23, 3, 4, 5, 6, 7], [1, 23, 3, 4, 5, 6, 7]]
print(threelist)

a = [i**2 for i in range(11)] #list functions
print(a)

ads = "Hello World My name is curry curry curry curry curry curry"
ads = ads.split() # This is not like where for lists if i were to this with lets say sort() it would assign None to ads
print(ads)

ads = "-".join(ads)
print(ads)