class Account:
    def __init__(self, ano, owner, balance):
        self.ano = str(ano)
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount >+ 10000000:
            print('일천만원 이상의 금액은 입금하실 수 없습니다. ')
            return
        self.__balance += amount
        print(f'당신의 잔액은 {self.__balance}입니다.')

    def withdraw(self, amount):
        if self.__balance < 0:
            print('당신의 현재 잔액이 없습니다.')
            return
        self.__balance -= amount
        print('당신의 현재 잔액은 {self.__balance}입니다.') 

    def __str__(self):
        return f'계좌번호 {self.ano}   계좌이름 {self.owner} 계좌잔액 {self.__balance}'