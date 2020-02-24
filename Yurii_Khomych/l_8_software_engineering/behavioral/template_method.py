class ExampleBase:
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    def step_one(self):
        raise NotImplementedError()

    def step_two(self):
        raise NotImplementedError()

    def step_three(self):
        raise NotImplementedError()


class Example(ExampleBase):
    def step_one(self):
        print("step_one")

    def step_two(self):
        print("step_two")

    def step_three(self):
        print("step_three")


example = Example()
example.template_method()
