class Dog:
    def Speak(self):
        print("woof woof!")

class Cat:
    def Speak(self):
        print("meow meow!")

class AnimalSound:
    def Sound(self, animal):
        animal.Speak()

dog = Dog()
cat = Cat()
sound = AnimalSound()

sound.Sound(dog)
sound.Sound(cat)