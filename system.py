class information:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
    def info(self):
        o=open('app_info.txt','r')
        x=o.read()
        print(x)
    def premium(self):
        o=open('premium.txt','r')
        x=o.read()
        print(x)
    def bank(self,username,password,date,discount,fname):
        print('Enter your account details')
        user=input('Enter username :- ')
        pas=input('Enter password :- ')
        if user==username and pas==password:
            print('Enter your bank details')
            bankaccount=input('Enter you bank accounnt number :- ')
            while True:
                upi_id = input('Enter your upi_id :- ')
                if '@' in upi_id:
                    break
                else:
                    print('@ must be there in upi_id')
            inbal=int(input('Enter your initial balance :- '))
            subscription=2000
            discount=discount/100
            if discount!=0:
                final_amount=subscription-(subscription*discount)
                print('You will get discount of ',(subscription*discount),' on your final amount')
                print('Final amount = ',final_amount)
            else:
                final_amount=subscription
            print('Current balance :- ',inbal)
            check=False
            if inbal>subscription:
                inbal-=final_amount
                print('Dear upi user :- ',upi_id,' from bank account number :- ',bankaccount,' on date :- ',date,' ',final_amount,' has been debited from your bank account.')
                print('Remmaining balance :- ',inbal)
                check=True
            else:
                print('Not sufficient balance')
            if check==True:
                print()
                print('Username = ',username)
                print('Full name = ',self.name)
                print('Mobile number = ',self.mobile)
                print('Upi id = ',upi_id)
                print('You have subscribed successfully')
                ff=open(fname,'a')
                ff.write(f'\nUpi-id :- {upi_id}')
                ff.write('\nYou have subscribed to our premium account.\n')
                ff.write('\n**************BILL**************')
                ff.write(f'''
SUBSCRIPTION AMOUNT = {subscription}
LUCKY COUPOUN (IF GET ANY) = {'will'}
LUCKY COUPOUN DISCOUNT = {discount*100}%
TOTAL BILL = {final_amount}
**************BILL**************
''')
                ff.close()
        else:
            print('username and password did not matched')
    def lucky(self):
        import random 
        f=open('lucky_draw.txt','r')
        x=f.readlines()
        f.seek(0)
        length=len(x)
        ran=random.randint(1,length)
        for i in range(1,length+1):
            x=f.readline()
            if i==ran:
                code=x
        dis=''
        print('You have got lucky coupoun voucher = ',code)
        for i in code:
            if i=='@':
                print('You have not get any lucky coupoun')
                return 0
            elif i.isdigit():
                dis+=i
        if dis!='':
            dis=int(dis)
            return dis
    def calculate_details(self,age,weight,height,gender,fname):
        bmi=weight/((height*height)/(100*100))
        if bmi < 18.5:
            bmi_range="Underweight"
        elif 18.5 <= bmi < 25:
            bmi_range="Normal weight"
        elif 25 <= bmi < 30:
            bmi_range="Overweight"
        else:
            bmi_range="Obesity"
        if gender=='Male':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        protein=weight+weight*0.8
        ff=open(fname,'a')
        ff.write(f'\nBMI = {bmi}')
        ff.write(f'\nBMI_RANGE = {bmi_range}')
        ff.write(f'\nBMR = {bmr}')
        ff.write(f'\nPROTEIN REQUIREMENT PER DAY = {protein}')
        ff.close()
        print('\nYour details added successfully to your file')
        return bmi,bmi_range,bmr,protein
    def diet(self,bmi,bmi_range,bmr,protein,fname):
        ff=open(fname,'a')
        ff.write('\n********************************')
        ff.write('\nDIET SCHEDULE')
        ff.write('\nThis a diet schedule based on your health records')
        ans=input('Do you want VEG or NON-VEG diet?(veg or non-veg)')
        if ans=='veg':
            ff.write(f'\nYour BMI is {bmi} and the range of bmi is {bmi_range} \nYour BMR is {bmr} which means you have to take that much calorie per day')
            ff.write(f'\nYour protein requirement is {protein} per day\n')
            vege=open('veg_bmi.txt','r')
            x=vege.read()
            ff.write(x)
            ff.close()
            print('Diet added successfully to your file')
        elif ans=='non-veg':
            ff.write(f'\nYour BMI is {bmi} and the range of bmi is {bmi_range} \nYour BMR is {bmr} which means you have to take that much calorie per day')
            ff.write(f'\nYour protein requirement is {protein} per day\n')
            vege=open('non_veg_bmi.txt','r')
            x=vege.read()
            ff.write(x)
            ff.close()
            print('Diet added succesfully to your file')
    def workout(self,fname):
        ff=open('workout_plan.txt','r')
        x=ff.read()
        ff.close()
        work=open(fname,'a')
        work.write('\n************************************************')
        work.write('\nWORKOUT SCHEDULE\n')
        work.write(x)
        work.close()
        print('workout plan added successfully to your file')
    def calorie(self):
        import numpy as np
        import matplotlib.pyplot as mpl
        calorie_intake=eval(input('Enter your daily calorie intake (in list form) :- '))
        print('The daily calorie intake = ',calorie_intake)
        calorie_burned=eval(input('Enter your daily calorie burned (in list form) :- '))
        print('The daily calorie burned = ',calorie_burned)
        calorie_burned=np.array(calorie_burned)
        calorie_intake=np.array(calorie_intake)
        mpl.subplot(1,2,1)
        mpl.plot(calorie_burned,marker='o',color='black',mec='blue',mfc='red',ms=10)
        mpl.title('CALORIES-BURNED')
        mpl.xlabel('No of calories')
        mpl.ylabel('calories')
        mpl.subplot(1,2,2)
        mpl.plot(calorie_intake,marker='o',color='black',mec='red',mfc='blue',ms=10)
        mpl.title('CALORIES-INTAKE')
        mpl.xlabel('No of calories')
        mpl.ylabel('calories')
        mpl.show()
        product_protein = {
            "Chicken breast": 31,
            "Salmon": 20,
            "Tofu": 8,
            "Greek yogurt": 10,
            "Eggs": 13,
            "Quinoa": 14,
            "Almonds": 21,
            "Black beans": 21,
            "Chickpeas": 19,
            "Whey protein powder": 80,
            "Paneer ": 18,
            "Lentils": 9,
            "Peanut butter": 25,
            "Cottage cheese": 11,
            "Soy milk": 3,
            "Chia seeds": 16,
            "Hemp seeds": 31,
            "Broccoli": 2.8,
            "Spinach": 2.9,
            "Tempeh": 19,
            "Edamame": 11,
            "Seitan": 75,
            "Chick'n strips": 15,
            "Protein bars": 20, 
        }
        product=[]
        protein=[]
        for u,v in product_protein.items():
            product.append(u)
            protein.append(v)
        protein=np.array(protein)
        mpl.figure(figsize=(10,10))
        mpl.pie(protein,labels=product,autopct='%.1f%%')
        mpl.title('Protein per 100g in various products.')
        mpl.legend(title='Protein products')
        mpl.show()
    def end(self):
        print()
        print('************Thanks for visiting************')        
        