"""
F-Strings & String Formatting In Python
"""
# me="Harry"
#
# a= "this is % s"%mee
# print(a)

# me="Harry"
# a1=3
# a="this si {} {}"
# b=a.format(me,a1)
# print(b)

import math
me = "Harry"
a1=3
a=f"this is {me} {a1}"
a=f"this is {me} {a1} {65*4}"
a=f"this is {me} {a1} {65*4} {math.cos(60)}"
print(a)