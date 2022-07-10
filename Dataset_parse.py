file = open("./datas/data-tone/1.txt")  # open file
arr = file.read().split("\n")  # read file
tone = arr[0]  # get Tonality
print(tone)
melody = arr[1].strip("[]").split(",")  # get melody
print(melody)
chord = arr[2].lstrip("[").rstrip("]").split("],[")  # get chord
print(chord)
