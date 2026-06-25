#allows a child class to provide its own implementation of a method that already exists in the parent class

#parent class
class Animal:
  def sound(self):
    print("Animal makes a sound")
    
    #child class
    class Dog(Animal):
        def sound(self):
            print("Dog barks: Woof! Woof!")
            
            s = Dog()
            s.sound()