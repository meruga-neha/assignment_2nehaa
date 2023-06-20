x = (2, 3, 4, 5, 6, 89, 45, 67, 68, 24, 46)
num1odd == 0
num2even == 0
for i in x:
    if not x % 2:
        num1even += 1
    else:
        num2odd += 1
print("num1 is even :"num1even)
print("num2 is odd :", num2odd)        
        

