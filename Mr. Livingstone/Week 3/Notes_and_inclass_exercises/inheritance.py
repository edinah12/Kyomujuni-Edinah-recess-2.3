class Animal:
    def __init__(self,name):
        self.name=name
        #self.breed=breed
        
    def info(self):
            
        print(f"Animal name: {self.name}")
        #print(f"Animal breed: {self.breed}")

        #creating child class
class Dog(Animal):
    def sound(self):
        print(self.name, "barks")
                
                
w= Dog("buddy")
w.info()
w.sound()
            
            
            
            
            
            
            
            