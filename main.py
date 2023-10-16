class Potato:
    def __init__(self, number):
        self.number = number
        self.state = "Созревание"

    def grow(self):
        if self.state == "Созревание":
            self.state = "Росток"
        elif self.state == "Росток":
            self.state = "Зелёная"
        elif self.state == "Зелёная":
            self.state = "Зрелая"

    def is_ripe(self):
        return self.state == "Зрелая"

class PotatoField:
    def __init__(self, num_potatoes):
        self.potatoes = [Potato(i + 1) for i in range(num_potatoes)]

    def grow_potatoes(self):
        for potato in self.potatoes:
            potato.grow()

    def harvest(self):
        if all(potato.is_ripe() for potato in self.potatoes):
            return "Вся картошка созрела. Можно собирать!"
        else:
            return "Картошка ещё не созрела!"

field = PotatoField(5)

for i in range(3):
    field.grow_potatoes()
    print("Картошка прорастает!")
    for potato in field.potatoes:
        print(f"Картошка {potato.number} сейчас {potato.state}")
    print(field.harvest())
    print()