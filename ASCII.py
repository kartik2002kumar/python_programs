# a='hai hello'
# out=''
# i=0
# while i <len(a):
#     if 'a'<=a[i]<='z':
#         out+=chr(ord(a[i])-32)
#     else:
#         out+=a[i]
#     i+=1
# print(out)



# a = "How are you all"
# result = ""

# for ch in a:
#     if ch == " ":
#         result += "_"
#     else:
#         result += ch

# print(result)




# a= "aaabcbb"
# output = ""

# count = 1

# for i in range(len(a) - 1):
#     if a[i] == a[i + 1]:
#         count += 1
#     else:
#         output += a[i] + str(count)
#         count = 1


# print(output)




# a=['hai', 3+5j , 3 , 3 ,'hai', 9.8]
# out=['hai',3+5j',3,9.8]
# out=['hai',3]
#  out=[]
#  i=0
# while i<len(a):
#     if a[i] not in out:
        
#         out.append(a[i])
#     i+=1
# print(out)



# outp=[]
# i=0
# while i<len(a):
#     if type(a[i])=='str' or type(a[i])== 'num':
#         outp.append(a[i])
#     i+=1
# print(outp)



# a=['hello' , 10 , 'ab' , 'python' , 3+5j , 'star' , 'apple' , 10]
# "agar odd hai to double and Ulta"
# "even par double keval"'


# a = [1, 2, 3, 2, 1]

# rev = []
# i = len(a) - 1

# while i >= 0:
#     rev.append(a[i])
#     i = i - 1

# if a == rev:
#     print("Palindrome list")
# else:
#     print("Not a palindrome list")

# a='((()))('
# # output=1
# i=0

# c=0
# c1=0
# while i < len(a):
#     if a[i]=='(':
#         c+=1
#     elif a[i]==')':
#         c1+=1
#     i+=1
# print(c-c1)
    

# a='hai hello'.split()
# # output={'hai':['hai',6,'iah3'],'hello':['hello',10,'olleh5']}

# output={}
# i=0

# while i<len(a):
#     output[a[i]]=[a[i],len(a[i])*2,a[i][::-1]+str(len(a[i]))]
#     i+=1
# print(output)


# wap to check the number is perfect number or not
a=int(input("enter the number : "))
i=1
sum=0
while i<a:
    if a%i==0:
        sum+=i
    i+=1
if sum==a:
    print("Perfect number")
else:
    print("not a perfect number")





