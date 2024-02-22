a={1,2,3,4}
print(a)
print(type(a))

#unorder

name={'apple','boy','good'}
print(name)


#not allow duplicate
name={'apple','boy','good','boy'}
print(name)

#unchangeable

'''name={'apple','boy','good'}
print(name[0]='0')'''

#addused to add single value

name={'apple','boy','good'}
name.add('0')
print(name)

#update used to store mutiple values

name.update((7,6,8,0))
print(name)

#remove
a={7,8,9,8,22,44}
'''a.remove(22)
print(a)'''

#discard

a.discard(12)
print(a)

#pop

a.pop()
print(a)

#clear()

a.clear()
print(a)

#union

a={1,2,3,4}
b={1,2,9,}
print(a.union(b))

#intersection
print(a.intersection(b))

#difference

print(a.difference(b))

#symmetric difference

print(a.symmetric_difference(b))

#issubset

a={1,2,3,4,5,6}
b={1,2,}
print(b.issubset(a))

#issuperset

a={13,3,4,5}
b={13,4,6,7}
print(a.issuperset(b))

#sum

a={13,40,60,70}
print('sum:',sum(a))

#min
a={12,4,5,0}
print('min',min(a))

#max

a={12,4,5,60}
print('max',max(a))



