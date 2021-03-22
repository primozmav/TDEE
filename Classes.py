class Person:
    def __init__(self, name, sex, age, mass, height):
        self.name = name
        self.sex = sex
        self.age = age
        self.mass = mass
        self.height = height

    def greed(self):
        print(f"Hello {self.name}")

    def calc_BMR(self):
        sex_constant = 5 if self.sex == "M" else -161
        BMR = ((10*self.mass)+(6.25*self.height)-(5*-self.age)+sex_constant)
        return (BMR)


subjects = [Person("Matjaz", "M", 26, 85, 186),
            Person("Primoz", "M", 26, 79, 179)]

for person in subjects:
    person.greed()

# print(p1.calc_BMR())
