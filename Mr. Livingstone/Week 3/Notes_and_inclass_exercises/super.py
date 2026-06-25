class Animal:
    def __init__(self,name):
        self.name = name
    
    def info(self):
        print(f"Animal name: {self.name}")
        
        #define child class
class Dog(Animal):
    def __init__(self, name, breed):
        
        #using the super function
        super().__init__(name)
        self.breed = breed

    def details(self):
       # super().info()
        print(f"{self.name} is a {self.breed}")
        
z = Dog("Buddy", "Golden Retriever")
z.info()