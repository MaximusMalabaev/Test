class BaseClass(object):
        def test(self):
                return 'BaseClass'
 
class Mixin1(object):
        def test(self):
                return 'Mixin1'
 
class Mixin2(object):
        def test(self):
                return 'Mixin2'
 
class MyClass1(BaseClass, Mixin1, Mixin2):
        pass
 
class MyClass2(Mixin2, Mixin1, BaseClass):
        pass
 
print(MyClass1().test())
print(MyClass2().test()) 