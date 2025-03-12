name = "Deekshi"
Age = 29



print(type(name))
print(type(Age))



print(name.upper())
print(Age)

#CREATE CLASS

class Dog:
    def bark(self):
        print("whoof whoof")

dog1 = Dog()
dog1.bark()#method

dog2 =Dog()
dog2.bark()


#DEf INIT METHOD
class Dog:
    def __init__self(self,name,breed):
        self.name = firstname
        self.breed = breed


    def bark(self):
        print("whoof whoof")

class Owner:
    def __init__(self,name,address,contact_number):
        self.name=name
        self.address=address
        self.contact_number = contact_number



dog1 = Dog("bruck","pumerian")
dog1.bark()#method
print(dog1.name)
print(dog1.breed)

dog2 =Dog("huch","dashon")
dog2.bark()
print(dog2.name)
print(dog2.breed)
