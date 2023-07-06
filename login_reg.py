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
    
def register(filename='info.json'):
    user = {}
    with open(filename,'r') as f:
        data = json.load(f)
    username = input('Enter a username :')
    phoneno = input('Enter phone number :')
    id = user_id()
    password = input('Enter password :')
    

    if username in user:
        print('username already taken')
        
    else:
        user['Username'] = username
        user['password'] = password
        user['id'] = id
        user['phoneNum'] = phoneno
        data.append(user)
        with open(filename,'w') as f:
            json.dump(data,f)
            f.write("\n")

    
        
        print('regestration sucessful')
        

    return user

def login(filename='info.json'):
    with open(filename,'r') as f:
        data = json.load(f)
    x = input('Enter Phone Number :')
    for a in data:
        if a['phoneNum'] == x:
            id = a['id']
    

        if(x not in a['phoneNum']):
            print('Enter a Phone Number')
        

            login()
            return 0
    password = input('Enter password :')
    for a in data:
        if(password not in a['password']):
            print('enter valid password')
            login()
        
            return -1
        else:
            print('login Successful')
        
            return 1

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

# login()
register()

