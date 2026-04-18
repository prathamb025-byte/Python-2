import csv
f=open("Student.csv","w",newline='')
writer=csv.writer(f)
writer.writerow(["Name","Marks"])
writer.writerow(["Amit","85"])
writer.writerow(["Riya","90"])

f.close()
f=open("Student.csv","r")
reader=csv.reader(f)
for row in reader:
   print(row)
f.close()
