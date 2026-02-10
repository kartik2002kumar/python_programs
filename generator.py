# WAP to extract all the integers fom a given list 
# a=[10,3.5,'hello',5.3,101]

# def ex_int(a):
#     for i in a:
#         if type(i)==int:
#             yield i
# print(list(ex_int(a)))



# WAp extract integer and also be palindrome 
# a=[111,12,'hello',7777,3.5]


# def ex_pal(a):
#     for i in a:
#         if type(i)==int:
#             a=str(i)
#             if str(i)==a[::-1]:
#                 yield i,len(a)
# print(list(ex_pal(a)))





# WAp take a number and print their 10 first multiple in tuple
# def multpl(n):
#     for i in range(1,11):
#         yield n*i
# print(tuple(multpl(5)))






# WAP to extrract prime numbers between the 1 to 1000 in the list
# def prime_numbers():
#     for num in range(2,1001):
#         is_prime=True
        
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             yield num
# print(list(prime_numbers()))


# def is_prime():
#     for i in range(2,num):
#         if num %i==0:
#             return 'not prime'
#     return 'prime'
# def prime():
#     for i in range(1,1001):
#         if is_prime(i)=='prime':
#             yield i
# print(list(prime()))


# WAP that a number is perfcet number or not
# WAP that a number is perfect number or not using generator

# def perfect_num(n):
#     for i in range(1, n):
#         if n % i == 0:
#             yield i


# num = int(input("Enter the number: "))

# if sum(perfect_num(num)) == num:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")




# def is_perefect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum+=i
#     if sum==num:
#         return 'perfect'
#     else:
#         return 'not perfect'
    
# def perfect():
#     for i in range(1,1001):
#         if is_perefect(i)=='perfect':
#             yield i
# print(list(perfect()))


# def s():
#     for i in range(1,6):
#         yield i
# print(list(s()))


a='Python is a language kkkkkkkk'.split()
max=0
out={}

for i in a:
    if len(i) > max:
        max=len(i)

out[max]=[]
for i in a:
    if len(i)==max:
        out[max]+=[i]
print(out) 














        


