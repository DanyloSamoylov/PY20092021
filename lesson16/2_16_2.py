class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id_ = id_
        self.name = name
        self.company = company
        self.workers_ = []

    def __repr__(self):
        return f'Boss: {self.name}. Workers: {self.workers_}'


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id_ = id_
        self.name = name
        self.company = company
        self.boss = boss
        self.boss.workers_.append(self)

    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.boss.workers_.remove(self)
            self.boss = new_boss
            self.boss.workers_.append(self)

    def __repr__(self):
        return f'{self.id_} - {self.name}, company: {self.company}'


Dany = Boss(666, 'Dany', 'Beetroot')
Maxim = Boss(911, 'Maxim', 'Beetroot')
Vovka = Worker(1, 'Vovka', 'Beetroot', Dany)
Katyka = Worker(2, 'Katyka', 'Beetroot', Dany)

print(Dany.workers_)
