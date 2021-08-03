

name ="joseph"
class firstclass:
    def __init__(self,name,loc):
        self.name=name
        self.location=loc
    def adder(self):
        print(self.name)    
obj1=firstclass("jose","pala")
obj2=firstclass("joseph","palakkad")
obj1.adder()
print(obj1.name,obj1.location)      
print(obj2.name,obj2.location)     