
import practice

print(practice.Dog().f(123,'abc', defaultArgs='tyu'))
print(practice.helloWorld('Tester'))

from practice import Dog
from practice import helloWorld

print(Dog().f(123,'abc', defaultArgs='tyu'))
print(helloWorld('Tester'))


# python has private heap space