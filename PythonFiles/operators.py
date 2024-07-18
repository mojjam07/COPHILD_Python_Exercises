# # x = [1,2,3,4,5,6,7,8,9,10]
# # for z in x:
# #     if z % 2 == 1:
# #         print('Even: ', z)
# # else:
# #     print('Not Available')

# # x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
# # for z in x:
# #     if z % z == 0:
# #         print('prime: ',z)
# #     else:
# #         print('Im unavailable')

# # import math
# # x = int(input('Enter Number:'))
# # o = input('Enter Oprerator:')
# # y = int(input('Enter Number:'))
# # if o =='+':
# #     print(x+y)
# # elif o == '-':
# #     print('x-y')
# # elif o == '*':
# #     print(x*y)
# # elif o == '/':
# #     print(x/y)
# # elif o == '**':
# #     print(x**y)
# # elif o == '//':
# #     print(x//y)
# # elif o == '%':
# #     print(x%y)
# # elif o == 'pow()':
# #     print(pow(x,y))
    
# # elif o == 'root':

# #         print(math.sqrt(x))
# # else:
# #     print('Invalid Operator')

# user = ['Elliot', 'Honey', 'Omah', 'TJ']
# passkey = ['1111', '2222', '3333', '4444']
# username = input('Enter username:')
# password = input('Enter passkey:')
# for x in user:
#     if x== username and password == passkey[0]:
#         print(x , 'logged in successfully')
#         break
# else:
#         print('User not found')


# user = []
# passkey = []
# a=input('Enter an item:')
# b=input('Enter an item:')
# c=input('Enter an item:')
# d=input('Enter an item:')
# e=input('Enter an item:')
# # username = input('Enter username:')
# # password = input('Enter passkey:')
# x=[a,b,c,d,e]
# for n in x:
#     user.append(n)
#     print(x)
#     break
    
# user.append(username)
# passkey.append(password)

# for x in user:
#     if username == user[0] and password == passkey[0]:
#         print(x, 'created successfully')
#     else:
#         print('Not successful')


# grades = {'Joy':'CA: 3.55', 'Scott':'CA: 2.15', 'Elliot':'CA: 4.75', 'Ijeoma':'CA: 4.00', 'Flash':'1.65'}
# studentName = input('Enter student name: ')

# if studentName in grades:
#     print(f"The grade of {studentName} in the course is: {grades[studentName]}")
# else:
#     print(f"No information found for {studentName}")


#Admission system form
print('Welcome to the admission page')
Name = input('Enter Your Fullname: ')
YOB = int(input('Enter Birth Year: '))
Score = int(input('Enter Your Score: '))
School = input('Enter School: ')
Course = input('Enter Course: ')
Date = 2024
Age = Date - YOB

#Matriculation Number Generation
Mat_no = [School,'/',Age,'/',Course[0],Course[2],Course[3]]
c=''.join(map(str,Mat_no))
    


#Age qualification
if YOB >= 18 and Score >= 250:
    print(Name,"Congratulations, you've been offered provisional admission into", School,". Your Matriculation Number is", c)
else:
    print(Name,'Sorry you are not eligible for admission')