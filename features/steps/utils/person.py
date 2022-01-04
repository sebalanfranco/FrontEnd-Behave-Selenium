from time import time
class Person:
    
    def __init__(self):
        self.password = 'secret'
        self.username = 'slanfranco2'
        self.invalid_password = 'no-secret'

class RandomPerson(Person):
    
    def __init__(self):
        super().__init__()
        self.username = f'%s_%f' % (self.username, time())
