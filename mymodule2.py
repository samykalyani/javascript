import mymodule as myd
myd.greeting('python')

myd.add(20,15)

myd.sub(15,10)

myd.multi(5,20)

from mymodule import add
add(10,10)

from mymodule import add,sub
add(40,60)
sub(50,3)

from mymodule import*
add(10,15)
sub(40,13)
multi(30,5)

print(dir(myd))
