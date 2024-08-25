class registration:
    def sign_up(self):
        print('Welcome to sign up for your account')
        print('Enter username')
        while True:
            user=input('Enter your username : - ')
            if len(user)<8:
                print('Username must have a length of 8 char')
            else:
                user1=user
                break
        print('Enter password as per the validation')
        cc=True
        while cc:
            print('''
Validation for password
1 min 8 char
2 at least one uppercase
3 at least 1 digit
4 at least 1 special char from !,#,_,@,$
                ''')
            cc+=1
            pas=input('Enter your password :- ')
            if len(pas)>=8:
                digit=False
                upper=False
                sc=False
                for i in pas:
                    if i.isupper():
                        upper=True
                    elif i.isdigit():
                        digit=True
                    elif i=='_' or i=='@' or i=='$' or i=='!' or i=='#':
                        sc=True
                if upper and digit and sc:
                    pass1=pas
                    cc=False
                    break   
                elif upper==False:
                    print('pass must contain at least one uppercase letter')
                elif digit==False:
                    print('pass must contain at least one uppercase digit')
                elif sc==False:
                    print('pass must contain one char from _,@,$')
            else:
                print('pass must contain 8 letter') 
        print('Sign-up has been done successfully')
        return user1,pass1

    def log_in(self,user1,pas1):
        user_c=0
        pas_c=0
        print('Welcome to sign in for your account')
        print('Enter username and password to log in')
        while user_c<3:
            user_c+=1
            user2=input('Enter username to log in :- ')
            if user1==user2:
                while pas_c<3:
                    pas_c+=1
                    pas2=input('Enter password to log in :- ')
                    if pas1==pas2:
                        final_pass=pas2
                        final_user=user2
                        break
                    elif pas_c==3:
                        print('You have entered wrong username')
                        print('you have exceeded the limit')
                        break
                    else:
                        print('You have entered wrong username')
                break
            elif user_c==3:
                print('You have entered wrong username')
                print('you have exceeded the limit')
                break
            else:
                print('You have entered wrong username')
        if user_c==3 or pas_c==3:
            print('log-in unsuccessful')
        else:
            print('Log-in successfull')
            return final_user,final_pass