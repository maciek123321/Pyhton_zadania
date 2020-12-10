fin = open("/Users/maciejnawrocki/Desktop/python/text_files/biology/Arachnology.txt")
fout = open("/Users/maciejnawrocki/Desktop/python/Arachnology_new.txt", "w+")

to_delete = ["Arachnology", "arachnology", "spiders", "spider"]
replace = ["Nauka o pająckach", "nauka o pająckach", "pająki", "pająk"]

#option = "delete"
option = "replace"

if (option == "delete"):
    for x in fin:
        for y in to_delete:
            x = x.replace(y, "")
        fout.write(x)
    fin.close()
    fout.close()

elif (option == "replace"):
    for x in fin:
        for y in to_delete:
            x = x.replace(y, replace[to_delete.index(y)])
        fout.write(x)
    fin.close()
    fout.close()

else:
    print("error")
