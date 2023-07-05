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
    
def register():
    user = {}
    username = input('Enter a username :')
    
    password = input('Enter password :')
    

    if username in user:
        print('username already taken')
        
    else:
        user[username] = password
        print('regestration sucessful')
        

    return user

def login(user):
    x = input('Enter Username :')
    

    if(x not in user):
        print('enter a valid user ID')
        

        login(user)
        return 0
    password = input('Enter password :')
    if(password not in user[x]):
        print('enter valid password')
        
        return -1
    else:
        print('login Successful')
        
        return 1

def proceed():
    print('press 1 to continue for login.......')
    
    x = int(input())
    return x

if __name__ == '__main__':
    if(display() == 2):
        a = register()
        if(proceed() == 1):
            x = login(a)
            while True:
                if(x == 0 or x == -1):
                    x = login(a)
                else:
                    break
