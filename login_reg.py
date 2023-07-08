from functions import user_id
import json
def display():
    print('Welcome to The app')
    print('---------------------------')
    print('enter 1 for sign in')
    print('Enter 2 for sign up')
    num = input('Enter Your Choice')
    if(int(num) == 1):
        print('please Sign IN')
    if(int(num) == 2):
        print('Sign UP')
    if(int(num) !=1 and int(num)!=2):
        print('enter valid number')
    
    return(int(num))
    
def register_user(username, password, phone_num):
    with open('info.json', 'r') as f:
        data = json.load(f)

    for user in data:
        if user['phoneNum'] == phone_num:
            return False

    with open('info.json', 'r') as f:
        data = json.load(f)
        last_id = data[-1]['id'] if data else '0'
        new_id = str(int(last_id) + 1).zfill(len(last_id))

    new_user = {
        'id': new_id,
        'Username': username,
        'password': password,
        'phoneNum': phone_num
    }
    data.append(new_user)

    with open('info.json', 'w') as f:
        json.dump(data, f, indent=4)

    return True

def verify_credentials(phone_num, password):
    with open('info.json', 'r') as f:
        data = json.load(f)

    for user in data:
        if user['phoneNum'] == phone_num and user['password'] == password:
            return user['id']

    return None

def proceed():
    print('press 1 to continue for login.......')
    
    x = int(input())
    return x

# if __name__ == '__main__':
#     if(display() == 2):
#         a = register()
#         if(proceed() == 1):
#             x = login(a)
#             while True:
#                 if(x == 0 or x == -1):
#                     x = login(a)
#                 else:
#                     break

# register()


