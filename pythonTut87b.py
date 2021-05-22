import re

# Regular expression with Metacharacter symbol

myStr="harry is good boy in the world and harry is code with harry"
# myStr="hrry is hadry"
# myStr="hsdfghfghrry is hadry"
myStr="harry"
myStr="h*rry"
# myStr="harrjt"

regex=re.compile(r'^h')                     # ^ means starts with character
regex=re.compile(r'^harr')
regex=re.compile(r'ry$')                    # $ means ends with
regex=re.compile(r'pip')
regex=re.compile(r'h.rry')                  # . (dot) means anyone character will come
regex=re.compile(r'ha?rryi?')               # ? is used is there any optional character
# regex=re.compile(r'ha?rryi?t')
regex=re.compile(r'h*rry')                  # * means any 0 or more character
regex=re.compile(r'h\*rry')                 # \* means exact match only * character

result=regex.finditer(myStr)
for match in result:
    print("The matches is",match)

