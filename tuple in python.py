#tuple

'''*tuples are used to store multiple items in a single variable

*tuples are written with round brackets-()

*tuples items are ordered ,unchangeable ,and allow duplicate values

*tuple items are indexed \the first item has index [0],the second item has index
[1]etc.
*tuples are unchangeable ,meaning that you cannot change,add or remove items
once the tuples is created.

    *change tuple values
    *once a tuple is created ,you cannot change its values.
    *tuples are unchangeable or immutable as it also is called.'''



#ordered

a=(1,2,3,4,5)

print('tuple is order:',a)
print(type(a))

#unchangeable

a=(1,2,3,4,5)
#a[0]=122
print('tuple unchangeable:',a)
print(type(a))

#allow duplicate value

a=(1,2,3,4,4,2,3,5)
print('allow duplicate value:',a)

#see data types dir
#print(dir(tuple))
#print(dir(set))
#print(dir(dict))
#print(dir(list))


#index

#0,1,2,3,4-->index

a=(6,32,4343,535,35,
   35,35,35,35,35,35,35,353,35,5,35,4)
print(a[0:5:])#[start:end:step]
print(a[0:1:2])#  n-1 default-1


