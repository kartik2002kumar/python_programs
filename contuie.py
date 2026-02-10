# wap to extract all even number between 1 to hundred using contuie
# for i in range(1,101):
#     if i%2!=0:
#         continue
#     print(i)

    # wap to extract upper case from given string
# s = input("Enter a string: ")
# upper_chars = ""

# for ch in s:
#     if ch.isupper():
#         upper_chars += ch

# print("Uppercase characters:", upper_chars)

# WAP  to extract keyword from list and it shoukd be integer,it shoukld be on even index,palindrome
a= [111,2112,'hello',[1,2,3],4+5j]
out=[]


for i in range(0,len(a),2):
    if not(type(a[i])==int and str(a[i])==str(a[i])[::-1]):
        continue
    out+=[a[i]]
print(out)
    
