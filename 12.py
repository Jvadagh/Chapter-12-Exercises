"""
12. For the next set of questions show what each program will print when the user supplies the indicated
input text.
"""

# (a)
"""
i. User enters 22  ==> 22
ii. User enters ZZ ==> ValueError: invalid literal for int() with base 10
"""
# print('Begin')
# x = int(input())
# print(x)
# print('End')

# ValueError will occur
# we can handle this error :

try:
    print('Begin')
    x = int(input())
    print(x)
except ValueError:
    print('can not change string to int! please run this code again and insert a number')
print('End')
"----------------------------------------------------------------------------------------------------------------------"
# (b)
"""
i.User enters 22  ==> 22
ii.User enters ZZ ==> Wrong!
"""
# any error Won't happen

print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
print('End')
"----------------------------------------------------------------------------------------------------------------------"
# (c)
"""
i. User enters 22  ==> 22
ii. User enters ZZ ==> ValueError: invalid literal for int() with base 10
"""
# we should use "except ValueError:" not "except IndexError:"

print('Begin')
try:
    x = int(input())
    print(x)
# except IndexError: it's wrong
except ValueError:
    print('Wrong!')
print('End')
"----------------------------------------------------------------------------------------------------------------------"
# (d)
"""
i. User enters 22  ==> 22
ii. User enters ZZ ==> Wrong!
"""
# there is noting to change!

print('Begin')
try:
    x = int(input())
    print(x)
except Exception:
    print('Wrong!')
print('End')
"----------------------------------------------------------------------------------------------------------------------"
# (e)
"""
i. User enters 22  ==> 22
                       wow
ii. User enters ZZ ==> Wrong!
"""
# there is noting to change!

print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
else:
    print('Wow')
print('End')
"----------------------------------------------------------------------------------------------------------------------"
# (f)
"""
i. User enters 22  ==> 22
                       Done
ii. User enters ZZ ==> Wrong!
                       Done
"""
# there is noting to change!

print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
finally:
    print('Done')
print('End')
"----------------------------------------------------------------------------------------------------------------------"
# (g)
"""
i. User enters 22  ==> 22
                       Wow
                       Done 
ii. User enters ZZ ==> Wrong!
                       Done
"""
# there is noting to change!

print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
else:
    print('Wow')
finally:
    print('Done')
print('End')
