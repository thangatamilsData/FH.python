f=open("fruits.txt","a")
f.write("tamil\n")
f.write("optimus\n")
hi=f.write
f.close()


f=open("fruits.txt","r+")
con=f.read()
print(con)
