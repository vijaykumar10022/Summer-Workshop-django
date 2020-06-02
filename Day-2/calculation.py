class Mydata:
         def __init__(self,a,b):
                  self.a=a
                  self.b=b
         def mysum(self,c):
                  self.c=c
                  return self.a+self.b+c
         def mymul(self):
                  return self.a*self.b
         def mycal(self):
                  return self.c

a=int(input("Enter Your Value"))
b=int(input("Enter Your Value"))
obj=Mydata(a,b)
c=int(input("Enter Another value to caluculate sum"))
print(obj.mysum(c))
print(obj.mymul())
print(obj.mycal())
