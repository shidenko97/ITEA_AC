class FruitVisitor:
    def draw(self, fruit):
        methods = {
            Apple: self.draw_apple,
            Pear: self.draw_pear,
        }
        draw = methods.get(type(fruit), self.draw_unknown)
        draw(fruit)

    def draw_apple(self, fruit):
        print("Apple")

    def draw_pear(self, fruit):
        print("Pear")

    def draw_unknown(self, fruit):
        print("Fruit")


class Fruit:
    def draw(self, visitor):
        visitor.draw(self)


class Apple(Fruit):
    pass


class Pear(Fruit):
    pass


class Banana(Fruit):
    pass


visitor = FruitVisitor()
apple = Apple()
apple.draw(visitor)

pear = Pear()
pear.draw(visitor)

banana = Banana()
banana.draw(visitor)
