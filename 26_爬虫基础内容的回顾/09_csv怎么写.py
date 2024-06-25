f = open("xxxx.csv", mode="w", encoding="utf-8")
f.write("1")
f.write(",")
f.write('"樵夫"')
f.write(",")
f.write("18")
f.write(",")
f.write("500")
f.write("\n")

f.write("2")
f.write(",")
f.write("alex")
f.write(",")
f.write("18")
f.write(",")
f.write("500")
f.write("\n")

id = 1
name = "wusir"
age = 18
money = 999
f.write(f"{id},{name},{age},{money}\n")
