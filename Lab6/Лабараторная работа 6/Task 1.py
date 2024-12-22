class UserAcount:

    def __init__ (self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password (self,new_password):
        self.__password = new_password
    
    def check_password(self,x):
        if x == self.__password:
            return True
        else:
            return False
    
    def info(self):
        print(self.username, self.email, self.__password)

a = UserAcount('gay_name', 'gay_mail', 'gay_password123')

print(a.check_password('11'))
a.set_password('11')
print(a.check_password('11'))