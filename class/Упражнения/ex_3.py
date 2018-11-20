class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type


class Zebra(Animal):
    
    def description(self):
        description = 'Я ' + self.type + ', ' + 'меня зовут ' + self.name + ', ' + 'мой возраст ' + self.age + '.'
        return description


class Dolphin(Animal):

    def description(self):
        description = 'Я ' + self.type + ', ' + 'меня зовут ' + self.name + ', ' + 'мой возраст ' + self.age + '.'
        return description


z = Zebra("Марина", "8", "зебра")
print(z.description())

d = Dolphin("Даня", "18", "дельфин")
print(d.description())
