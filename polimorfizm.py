class Mammal:
    def move(self):
        print('Двигается')

class Hare(Mammal):
    def move(self):
        print('Прыгает')

animal = Mammal()
animal.move() # Двигается
hare = Hare()
hare.move() # Прыгает

#Можно получить и доступ к методам класса-предка либо по прямому обращению, 
# либо с помощью функции super:

class Parent():
    def __init__(self):
        print('Parent init')

    def method(self):
        print('Parent method')

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def method(self):
        super(Child, self).method()

child = Child() # Parent init
child.method() # Parent method

#Одинаковый интерфейс с разной реализацией могут иметь и классы, не связанные родственными узами:

class English:
  def greeting(self):
    print ("Hello")

class French:
  def greeting(self):
    print ("Bonjour")

def intro(language):
  language.greeting()

Alik = English()
Jakshybek = French()
intro(Alik) # Hello
intro(Jakshybek) # Bonjour