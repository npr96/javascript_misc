import requests
from flask import jsonify

intro = '''
Welcome!
--------
press 1 to sign up,
press 2 to log in,
'''


def menu():
    power = 1
    while power == 1:
        user_input = input(intro)
        try:
            dict_of_intro[user_input]()
            continue
        except KeyError:
            print('please input 1 or 2')
            continue

def sign_up():
    d_username = input('what is your desired username?\n')
    d_pword = input('what is your desired password?\n')
    #output = '{\n    "username": "' + d_username + '"\n    "password": "' + d_pword + '"\n    "id": 1\n}'  
    output = {'username': d_username, 'password': d_pword}
    r = requests.post('http://127.0.0.1:5000/guide', json = output)
    print('thank you for signing up')
    return

def log_in():
    r = requests.get('http://127.0.0.1:5000/guide')
    user_input = input('username?\n')
    if user_input in r.text.split():
        pass
    else:
        print('that is not a valid username')
        return
    user_pw = input('password?\n')
    if user_pw in r.text.splet():
        pass
    else:
        print('that is not a valid password')
        return
    

dict_of_intro = {
        '1': sign_up,
        '2': log_in
        }



if __name__ == '__main__':
    menu()
