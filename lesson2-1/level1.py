
# 1 Write a program to calculate expression:
#  1 + 2a    4(b + c)(5 - d - e)     7     2
# ------  + ------------------- - 6(- + h)
#   3               f               g
  
a = 32
b = 37.2
c = -102.345
d = 45
e = 11
f = 3
g = 0.002
h = 11

print ((1+2*a)/3)+((4*(b+c)*(5-d-e))/f)-(6*(7/g+h)**2)

# 2 Print this ASCII graphic using 4 different string literal types:

#   _-_-_-_-_-_-_
#   \           /
#   |  ^_____^  |
#   /  (.) (.)  \
#   |  ( t   )  |  Miaowww
#   \    ==/    /
#   |           |
#   '"'"'"'"'"'"'

print "_-_-_-_-_-_-_"
print "\           /"
print "|  ^_____^  |"
print "/  (.) (.)  \ "
print "|  (  t   ) | Miaowww"
print "\    ==/    /"
print "|           |"
print " '"'"'"'"'"'"'""'"'"'"'"''"'"'"'"'"'"'"' "

# combine few different solutions in one set
a = 'Miaowww'
b = "_-"
s = "||"
list = "\    ==/    /"
print (b*6)+"_"
print "\           /"
print """|  ^_____^  |"""
print "/  (.) (.)  \ "
print "|  (  t   ) |  "+a
print list
print("           ".join(s))
print "%c%c"%("'",'"') *6
print u'\u0022\u0027\u0022\u0027\u0022\u0027\u0022\u0027\u0022\u0027\u0022\u0027\u0022\u0027\u0022'

# a little beet tricky solution because i've been changed one \ to | :), but looks at most simple
print """
   _-_-_-_-_-_-_
   \           /
   |  ^_____^  |
   /  (.) (.)  |
   |  ( t 1  )  |  Miaowww
   \    ==/    /
   |           |
   '"'"'"'"'"'"'
"""

# Print unique elements from any given list or tuple.
