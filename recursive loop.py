# def upper(a,out=' ',i=0):
#     if i>=len(a):
#         return out
#     if 'A'<=a[i]<='Z':
#         out+=a[i]
#     return upper(a,out,i+1)
# print(upper('pYThOn'))



# WAp to extract number from the string
# def extract_num(a,i=0):
#     if i==len(a):
#         return ""
#     if a[i].isdigit():
#         return a[i]+extract_num(a,i+1)
#     else:
#         return extract_num(a,i+1)
# print(extract_num('ka4rh0hg787'))


# WAP a=[2,3.5,'hello',8,7,[1,2]]
# oup=[4,3.5,'hello',64,7,[1,2]]

# def modify(a,out=[],i=0):
#     if i>=len(a):
#         return out
#     if type(a[i])==int and a[i]%2==0:
#         out+=[a[i]**2]
#     else:
#         out+=[a[i]]
#     return modify(a,out,i+1)
# print(modify([2,3.5,'hello',8,7,[1,2]]))







# WAP a='11001000111001'
#     b='00110111000000'
# out=2
# def dif(a,b,out=0,c=0,c1=0,i=0):
#     if i>=len(a)or i>=len(b):
#         return out
#     if a[i]=='1':
#         c+=1
#     if b[i]=='1':
#         c1+=1
#     out= c-c1
#     return dif(a,b,out,c,c1,i+1)
# print(dif(a='11001000111001',b='00110111000000'))



# WAP 
# a=['one','nine','four]
#  b=['seven','zero','one]
#  out=895

# def sum(a):
   

#     d={'zero':'0' , 'one':'1' , 'two':'2' , 'three':'3' , 'four':'4' , 'five':'5' , 'six':'6' , 'seven':'7' , 'eight':'8' , 'nine':'9'   }

#     out=''
#     for i in a:
#         out+=d[i]
#     return int(out)
# # print(sum(['one','nine','four']))
# a=['one','nine','four']
# b=['seven','zero','one']
# print(sum(a)+sum(b))
      




# WAP
# take number list and find there all factorial using recursion :

# def fact(n)6:
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)


# def factorial_list(a, i=0):
#     if i == len(a):
#         return []

#     return [fact(a[i])] + factorial_list(a, i+1)


# nums = [3, 4, 6]
# print(factorial_list(nums))





def ex_fact(a,out=[],i=0):
    def fact(n):
        if n==0 or n==1:
            return 1
        return n*fact(n-1)
    if i>=len(a):
        return out
    else:
        out+=[fact(a[i])]
    return ex_fact(a,out,i+1)
print(ex_fact([3, 4, 6]))

    
# WAp if starting 10 number fact
# def fact(n):
#     if n==0 or n==1:
#     return n*fact(n-1)
# def ex_fact():
#     out=[]
#     for i in range(1,11):
#         out+=[fact(i)]
#     return out 
# print(ex_fact())




   
    
    


    
    















    
    