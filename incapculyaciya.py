#Одиночное подчеркивание в начале имени атрибута говорит о том, 
# что переменная или метод не предназначен для использования вне методов класса, 
# однако атрибут доступен по этому имени.

class A:
    def _private(self):
        print("Это приватный метод!")
 

a = A()
a._private()

#Двойное подчеркивание в начале имени атрибута 
#даёт большую защиту: атрибут становится недоступным по этому имени.
class B:
     def __private(self):
        print("Это приватный метод!")

b = B()
b.__private()
#Однако полностью это не защищает, 
# так как атрибут всё равно остаётся доступным под именем _ИмяКласса__ИмяАтрибута:
#b._B__private()
