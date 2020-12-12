class Worker:
    name = []
    surname = []
    position = []
    _income = {'wage': [], 'bonus': []}


class Position(Worker):
    def get_full_name(self):
        self.name = input('Enter your name: ')
        Worker.name.append(self.name)
        self.surname = input('Enter your surname: ')
        Worker.surname.append(self.surname)
        self.position = input('Enter your position: ')
        Worker.position.append(self.position)

    def get_total_incomr(self):
        self.wage = float(input('Enter wage: '))
        Worker._income['wage'] = self.wage
        self.bonus = float(input('Enter bonus: '))
        Worker._income['bonus'] = self.bonus


worker = Position()
worker.get_full_name()
worker.get_total_incomr()
print(''.join(Worker.name), ''.join(Worker.surname), ''.join(Worker.position), Worker._income)

