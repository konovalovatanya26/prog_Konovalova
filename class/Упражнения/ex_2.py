class Mother:
    def eye_color(self):
        return "Голубые глаза"

    def print(self):
        print(self.eye_color())


class Daughter(Mother):
    def eye_color(self):
        return "Зеленые глаза"


d = Daughter()
d.print()

m = Mother()
m.print()