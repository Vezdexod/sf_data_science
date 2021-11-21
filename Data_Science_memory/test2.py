class User():
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance
        self.dict = {email:password,}
        
    def login(self, email, password):
        if self.dict[email] == password:
            #print(self.dict[email], 'and', password)
            return True
        else:
            #print(self.dict[email], 'and', password)
            return False
    def update_balance(self, count):        
        self.balance += count
        return self.balance
            
            
user = User("gosha@roskino.org", "qwerty", 20_000)
user.login("gosha@roskino.org", "qwerty123")
# => False
user.login("gosha@roskino.org", "qwerty")
# => True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# => 19700