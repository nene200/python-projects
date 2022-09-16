import time

database = {}

class EmptyInputError(Exception):
    pass

while True:
    try:
        while True:
            
            command = input('Enter a command: ')

            if command == 'login':

                username_input = input('username: ')
                password_input = input('passord: ')

                if database[username_input] == password_input:
                    print('Access granted')
                    print('Please wait')
                    time.sleep(5)
                    print('Ok....Loading....')
                    time.sleep(1)
                    print('Alright you have security clearance. Pulling up the secret mainframe.')

                elif username_input == 'username' and password_input != 'password':
                    print('password incorrect!')

                elif username_input != 'username' and password_input == 'password':
                    print('username incorrect!')

                else:
                    print('you might  wanna check both fields....')  


            elif command == 'signup':
                username_input = input('username: ')
                password_input = input('password: ')
                if password_input == '' or username_input == '':
                    raise EmptyInputError
                        
                database[username_input] = password_input
                print(database)    
    except EmptyInputError:
        print("cant leave value blank")          
    except: 
        print('invalid data')            