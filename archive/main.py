class Animal:
    type = "Животное"
    name = ""
    say_text = ""

    def say(self): # cow1, dog1
        print(f'{self.type} "{self.name}" говорит {self.say_text}!')

class Cow( Animal ):
    type = "Корова"
    say_text = "Муу"

class Dog( Animal ):
    type = "Собака"
    say_text = "Гав"

class Fish(Animal):
    def say(self):
        print("А рыба не говорит")

cow1 = Cow( )
cow1.name = "Бурёнка"

dog1 = Dog()
dog1.name = "Шарик"

dope_fish = Fish()

cow1.say()
dog1.say()
dope_fish.say()

