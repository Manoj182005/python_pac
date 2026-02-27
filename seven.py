word = "manoj"

with open("word.txt", "r") as f:
    content = f.read()
contentnew = content.replace(word, "patel")

with open("word.txt", "w")as f:
    f.write(contentnew)
