# 3 Write a function that returns dictionary where keys are even numbers between 1 and n and values are keys in square, by default n = 100.
dict_res = lambda val: {key:key ** 2 for key in xrange(1, val+1)}
print "square dict  " , dict_res(10)

# ----------------------------------------
# 1 Write program to evaluate (a or not b) and (c or not a) expression for boolean varibles a, b, c showing result for all possible variables combinations.
values = (True, False)
def boolen():
    for a in values:
        for b in values:
            for c in values:
                print ((a or not b) and (c or not a))
boolen()
# ------------------------------------------
# 2 Write a function to return the sum of the numbers in the array, returning 0 for an empty array. Since the number 13 is very unlucky, it does not count, and numbers that come immediately after a 13 also do not count. Array could contain strings and boolean values (do not count them too):
def val(num):
    i = 13
    for n in num:
        if not isinstance(n,bool):
            if isinstance(n,int):
                if n == i:
                    break
                mor.append(n)
    return sum(mor)
    
    
