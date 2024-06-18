filename = "C:/Users/ibenc/OneDrive/Desktop/compsci1md3/week6/Popular_Spotify_Songs.csv"
file = open(filename, "r")
tofilename = "C:/Users/ibenc/OneDrive/Desktop/compsci1md3/week6/dance.csv"
danceability = open(tofilename,"w")

for line in file:
    data = file.readline().strip().split(",") 
    danceability.write(str(data[0]+","+data[1]+","+data[17]+"\n"))

file.close()
danceability.close()