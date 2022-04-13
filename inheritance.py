class Parent:
     def __init__(self , name, age):
          self.firstname = name
          self.age = age
     def view(self):
         print(self.firstname , self.age)
class Child(Parent):
     def __init__(self , name , age):
          Parent.__init__(self, name, age)
          self.lastname = "TeknikInformatika"
     def view(self):
          print("Pemrograman Visual" , self.firstname ,  self.age , self.lastname)
ob = Child("Wira Pratidina Iptu Tahang Palle" , '2019')
ob.view()
