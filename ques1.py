# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str

# s = "PunjabEnggCollege"

# print ("The original string is : ",end="")
# print (s)

# print ("The reversed string(using loops) is : ",end="")
# print (reverse(s))

string="hello ! world "
for i in string:
    string[int(i)]=string[int(-i)]
    
print(string)