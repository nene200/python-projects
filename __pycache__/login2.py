import time

database = {}

class EmptyInputError(Exception):
    pass

while True:
    try:
        while True:

            command = input('Enter command: ')
            
            if command == 'signup':

                username_input = input('username: ')
                password_input = input('password: ')

                if password_input == '' or username_input == '':
                    raise EmptyInputError
                    
                database[username_input] = password_input
                print(database)    

            elif command == 'login':

                username_input = input('Enter username: ')
                password_input = input('Enter password: ')

                if database[username_input] == password_input:
                    print('Access granted')
                    time.sleep(1)
                    print('Please wait')
                    time.sleep(5)
                    print('ok....loading....')
                    time.sleep(5)
                    print('Alright you have security clearance. Pulling up the secret mainframe.')

                elif username_input == 'username' and password_input != 'password':
                    print('password incorrect!')

                elif username_input != 'username' and password_input == 'password':
                    print('username incorrect!')
                 
                else:
                    print('kindly check both data(username\password)')

                if password_input == '' or username_input == '':
                    raise EmptyInputError

    except EmptyInputError:
        print("cant leave value blank")

    except: 
        print('invalid data')            