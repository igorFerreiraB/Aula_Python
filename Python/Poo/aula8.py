class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user   

    def set_password(self, password):
        self.password = password      

connection = Connection()
connection.set_user("Igor Ferreira")
connection.set_password("1234")
print(connection.user)
print(connection.password)