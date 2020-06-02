class Student:
	address="vijayawada"
	collegename="VRSEC"
	def ECE(name,roll):
		return "my name is "+ name+ "and roll number is  "+str(roll)



name=input("Enter Your Name")
roll=int(input("Enter Roll Number"))
obj=Student
print(obj.ECE(name,roll))
