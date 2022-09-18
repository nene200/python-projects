import time

class EmptyInputError(Exception):
    pass

database = {}

while True:
    try:
        while True:
    
            command = input('Enter comand: ')
            if command == 'Create an account':

                First_name = input('Enter First_name: ')
                Surname = input('Enter surname: ')
                Birthday = input("What is your B'day? (in DD/MM/YYYY): ")
                Username = input('Enter username: ')
                Password = input('Enter new password: ')
                Confirm_password = input('confirm new password: ')

                if Password == '' or Username == '' or First_name == '' or Surname == '' or Birthday == '' or Confirm_password == '':
                    raise EmptyInputError

                database[First_name] = Surname = Birthday = Username = Password = Confirm_password
                print(database)

            elif command == 'Login':
                Username = input('Enter username: ')
                Password = input('Enter password: ')

                if database[Username] == Password:
                    print('Access granted')
                    time.sleep(1)
                    print('Please wait')
                    time.sleep(5)
                    print('ok....loading....')
                    time.sleep(5)
                    print('Alright you have security clearance. Pulling up the secret mainframe.')

                elif Username == 'username' and  Password!= 'password':
                    print('password incorrect!')

                elif  Username != 'username' and  Password == 'password':
                    print('username incorrect!')
                        
                else:
                    print('kindly check both data(username\password)')

                if  Password == '' or  Username == '':
                    raise EmptyInputError


    except EmptyInputError:
        print("cant leave value blank")

    except: 
        print('invalid data')