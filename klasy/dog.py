class Dog():
    """prosta próba modelowania psa"""
    def __init__(self, name, age):
        """inicjalizacja atrybutów name i age"""
        # zmienn z prefix self jest dostepna dla każdej metody w klasie
        self.name = name
        self.age = age
    def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecenia."""
        print(f"{self.name.title()} teraz siedzi.")
    def roll_over(self):
        """Symulacja że pies kładzie sie na plecy po otrzymaniu polecenia."""
        print(f"{self.name.title()} teraz położy sie na plecy")
    
my_dog = Dog('galgan', 10)
my_dog.sit()
my_dog.roll_over()