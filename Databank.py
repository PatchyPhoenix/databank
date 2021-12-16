user = input("Hello, what can I do for you?\n1 : Add data\n2 : Read your data\n3 : Delete your data\n")
user = user.lower()
a = open("Enter the path of the text file here","r")
olddata = a.read()
a.close()


if user == "1":
    if olddata == "":
        data = input("Enter your data here.")
        f = open("Enter the path of the text file here","w")
        f.write(data)
        f.close()
        r1 = open("Enter the path of the text file here","r")
        print(f"Added the data")
        r1.close()
    else:
        data = input("Enter your data here.")
        f = open("Enter the path of the text file here","w")
        f.write(f"{olddata}\n{data}")
        f.close()
        r1 = open("Enter the path of the text file here","r")
        print(f"Added the data")
        r1.close()
elif user == "2":
        r = open("C://Users/Preetha/AppData/Local/Programs/Python/Python39/DataBank/data.txt","r")
        print(r.read())
        r.close()

elif user == "3":
        d = open("Enter the path of the text file here","w")
        d.write("")
        d.close()
        print("Deleted all the data.")
else:
    print("Enter 1, 2 or 3")
            




