class person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):
        return repr('{:} is {:} years old and {:} cm tall').format(p.name, p.age, p.height)

p = person('Joe', 10, 150)
print(p)
