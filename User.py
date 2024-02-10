class User:
    def __init__(self, name, surname, email, password, balance, portfel):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.balance = balance
        self.portfel = portfel

    def setName(self, name):
        self.name = name

    def setSurname(self, surname):
        self.surname = surname

    def setEmail(self, email):
        self.email = email
        # перевірка на уже наявний в бд

    def setPassword(self, password):
        self.password = password
        # перевірка на уже наявний в бд

    def setBalance(self, balance):
        self.balance = balance

    def setPortfel(self, portfel):
        self.portfel = portfel

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getBalance(self):
        return self.balance

    def getPortfel(self):
        return self.portfel

    def __dict__(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'balance': self.balance,
            'portfel': self.portfel
        }

    def to_dict(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'balance': self.balance,
            'portfel': self.portfel
        }