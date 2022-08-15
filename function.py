

#
#
# name_list=['puja','sambit','rahul','syam','lipika','raj']
#
# # print(len(name_list))
# # print(list(range(4)))
#
#
#
#
#
# def name_title(name,title):
#
#     for i in range(len(name_list)):
#         if name in name_list:
#             if name_list[i] == name:
#                 name_list[i] = name_list[i] + " " + title
#                 break
#         else:
#             ask=input('Name not in list  !! Do you want to add your name in the list ? please enter yes or no -- ')
#             if ask=='yes':
#                 full_name= name + " " +title
#                 name_list.append(full_name)
#                 break
#             else:
#                 print('Ok . visit again!!!')
#                 break
#
#
#
#
#
#
#
# print('before calling functiom',name_list)
# name=input('Enter any name to change : ')
# title=input('Enter title for the name : ')
# name_title(name,title)
# print('after calling functiom',name_list)


#2 arguments in function 1. odd 2.even ,even/2=ans ,print ---odd +ans
# odd odd =minus


def home_work(num1,num2):
    if num1%2==0:
        print((num1/2)+num2)
    else:
        print((num2 / 2) + num1)


home_work(100,50)











