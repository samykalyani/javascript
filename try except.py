#try except
a=5
b='0'
try:
    print(a/b)
except:
    print('your input is wrong')
a=5
b=7
try:
    print(a+b)
except:
    print('your input is wrong')

a=5
b='7'
try:
    with open('python.txt','r')as file:
        print(file)
except:
    print('your file is not create')

try:
    #some code
except:
    #executed if error in the
    #try block
else:
    #execute if no exception
finally:
    #some code.....(always executed)
