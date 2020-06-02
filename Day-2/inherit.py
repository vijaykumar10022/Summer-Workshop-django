class Person:
	def __init__(self,age,mailid):
		self.age=age
		self.mailid=mailid
	def getage(self):
		return self.age
	def getmailid(self):
		return self.mailid
class Emp(Person):
	def data():
		obj=Person(25,"vijay@gmail.com")
		print(obj.getage())
		print(obj.getmailid())
		
		
obj=Emp
obj.data()
