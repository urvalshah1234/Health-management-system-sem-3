class details:
    def __init__(self):
        pass
    def get(self):
        print('Enter the following details')
        full_name = input('Enter your full name :- ')
        num = True
        while num:
            mobile = input('Enter your 10 digit mobile num (it must be starting from 9,8,7) :- ')
            if len(mobile) == 10:
                if mobile[0] in ['9', '8', '7']:
                    num = False
                else:
                    print('num must be starting from 9,8,7')
            else:
                print('Enter 10 digit mobile number')
        while True:
            email = input('Enter your email :- ')
            if '@' in email and '.' in email:
                break
            else:
                print('@ and . must be there in email')
        while True:
            gender = input('Enter your gender(Male or Female) :- ')
            if gender=='Male' or gender=='Female':
                break
            else:
                print('choose from given option only')
        age = int(input('Enter your age :- '))
        weight = float(input('Enter your weight(in kg) :- '))
        height = float(input('Enter your height(in cm) :- '))
        print('Details entered successfully')
        return full_name, mobile, email, gender, age, weight, height