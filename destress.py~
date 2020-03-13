

intro = '''
Welcome to the automated thingy
===============================
1. balance
2. withdraw
3. deposit
4. goodbye
: '''
dict_of_users = {
        'example': ['example password', 0]
        }
class User:
    def __init__(self, balance=0, power_switch=1):
        self.balance = balance
        self.power_switch = power_switch
    power_switch = 1
    balance = 0
    
    def menu(self):
        while self.power_switch == 1:
            try:
                input_user = input(intro)
                dict_of_action[input_user]()
            except KeyError:
                print('please take another look at the main menu\n')
   

name = input('what is your name')       
name = User

def balance():
    print(User.balance) 
    return

def withdraw():
    wolo = input('amount: ')
    User.balance = User.balance - int(wolo)
    return

def deposit():
    wolo = input('amount: ')
    name.balance = User.balance + int(wolo)
    return

def goodbye():
    User.power_switch = 0
    return

def easter_egg():
    print(r'''
                            There are no eggs here. . .


                                      .-~-.
                                    .,     ,.
                                   /         \ 
                            .-~-.  |         |
                          .'     '.:         :
                         /         \         /
                         :          ; .-~""~-,
                         |          /`        `'.
                         :         |             \
                          \        |             /
                           `.    .' \          .'
                             `~~`    '-.____.-'
                             Nope, nothing to see here''')

dict_of_action = {
        '1': balance,
        '2': withdraw,
        '3': deposit,
        '4': goodbye,
        'easter egg': easter_egg
        }

if __name__ == '__main__':
    User.menu(name)
