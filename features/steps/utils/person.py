from time import time
from steps.utils.dates import get_future_date, get_month_from_date, get_year_from_date

class Person:
    
    def __init__(self):
        # Hardcoding days to get future date
        expiration_date = get_future_date(120)
        self.name = 'Seba Lanfranco'
        self.password = 'secret'
        self.username = 'slanfranco2'
        self.address = {
            'street': 'Lino Verri 162',
            'city': 'Ucacha',
            'country': 'Argentina'
        }
        self.credit_card = {
            'number': 4111111111111111,
            'expiration_month': get_month_from_date(expiration_date),
            'expiration_year': get_year_from_date(expiration_date)
        }

class RandomPerson(Person):
    
    def __init__(self):
        super().__init__()
        self.username = f'%s_%f' % (self.username, time())
