class Person:

    def __init__(self, fullname, age, gender, interests):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.interests = interests

    def hello(self):
        # return "Hello, my name is % s and I am % d years old. My interests are % s" % (self.fullname, self.age, self.interests)
        return f"Hello, my name is {self.fullname} and I am {self.age} years old. My interests are {self.interests}"        

person = Person('Ryan', 30, 'male', 'being a hardarse, agile, ssd hard drives.')
        
greeting = person.hello()

print(greeting)


