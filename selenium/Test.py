xinzi="18-20K"
print(int(xinzi.split("-")[1].replace("K",""))>18)
print(xinzi!="面议" and int(xinzi.split("-")[1].replace("K",""))>18)