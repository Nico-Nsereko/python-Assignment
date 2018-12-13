#Nsereko Nicodemus
#Question 0
def grades():
    my_list = [23,4,5,6,64,90,67,98,45,23,67,78,89]
    list1 = []   
    list2 =[]
    for num in my_list:
        if num>50:
            list1.append(num)
        else:
            list2.append(num)
            
        if 0 <= num < 20:
        	print("{}: Repeat!".format(num))
        elif 20 <= num < 40:
                print("{}: Very Poor!!".format(num))
        elif 40 <= num <= 59:
                print("{}: Poor!".format(num))
        elif 60 <= num <= 69:
                print("{}: Good".format(num))
        elif 70 <= num <= 89:
                print("{}: Very Good".format(num))
        elif 90 <= num <= 100:
                print("{}: Excellent".format(num))
        else:
            print('{}: Invalid mark'.format(num))

    print('Marks above 50: {}'.format(list1))
    print('Marks below 50: {}'.format(list2))
    


#Question 1
def seven_divisor():
    num=0
    print('Numbers between 2000 and 3200 that are divisible by 7 and not by 5')
    print(*[num for num in range(2000,3201) if num%7==0 and num%5!=0], sep=', ')       
    return num

#Question 2
def lines_to_upper():
    all_lines=[]
    boole = True
    while boole:
        line_input = input('Enter a line to convert to upper case: ')
        if line_input:
            if(type(line_input)==str):
                line_input = line_input.upper()
                all_lines.append(line_input)           
        else:
            break
    return all_lines

#Question 3
def divisibleByFive():    
    my_nums = input('Enter four digit binary numbers: ')
    all_nums=[]
    x = my_nums.split(',')
    for num in x:
        try:
            decimal_num = int(num,2)
            if decimal_num%5==0: 
                all_nums.append(num)
        except ValueError:
            print('Please only enter numbers containing digit 0-1')
    return all_nums

#Question 4
def accountBalance():
    balance = 0
    while True:
        user_input = input('Enter transaction type(D/W) and amount')
        if user_input:
            try:
                user_input = user_input.split()
                trans_type = user_input[0]
                amount = user_input[1]
            
                if trans_type.lower()== 'd':
                    balance += int(amount)
                elif trans_type.lower()== 'w':
                    balance -= int(amount)
                else:
                    print('Please enter the transaction type correctly.')
                    
            except ValueError:
                print('The amount should contain only digits')
            except IndexError:
                print('Please seperate the transaction type(D/W) from the amount')
        else:
            return balance

#question 5
def printList():
    my_list = []
    for num in range(1,21):
        my_list.append(num**2)
    print(my_list[0:5])


grades()
seven_divisor()
print(*lines_to_upper(), sep='\n')
print(*divisibleByFive(), sep=', ')
print(accountBalance())
printList()


