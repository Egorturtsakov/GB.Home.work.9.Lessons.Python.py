class Worker:

    def __init__(self, name='Petr', surname='Vasechkin', position='singer', wage=100, bonus=20):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


v_pet = Position('Vasilii', 'Petechkin', 'dancer', 110, 30)
print(f'New attributes are: {v_pet.name}, {v_pet.surname}, {v_pet.position}, {v_pet._income}')
print(f'Total salary of {v_pet.get_full_name()} is {v_pet.get_full_salary()}')