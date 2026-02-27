word = "manoj"

with open("lorem.txt", "r")as f:
    content = f.read()
if("fdkfksd" in content):
    print("word is present in the file")
else:
    print("word is not present in the file")