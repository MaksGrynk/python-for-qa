# Write a function which takes a string and returns its first 10 words concatenated with the last 10 characters.
def lines():
    str_end = strin[-1::-1]
    print strin[0:10]+str_end[0:10]
lines()
#----------------------------------------
# Write a function that takes a list and returns a new list that contains all the elements of the first list
# minus all the duplicates: [1, 2, 3, 4, 4, 6, 2] -> [1, 3, 6]

list1 = [1, 2, 3, 4, 4, 6, 2]
def rem_dublic():
    output = []
    for i in list1:
        if not i in output:
            output.append(i)
        elif i in output:
            output.remove(i)
        print output
rem_dublic()
#-----------------------------------------
Write a function that takes a comma-separated string and returns the last element (separated by the last comma) or the entire string, if there is no comma in it.

def endstring():
    if str3.find(str4) > 0:
        ite = str3.rfind(str4)
        for g in str4:
            if g == str4:
                print "Only end of string after '' : ", str3[ite:]
    else:
        print "Whole string : ", str3
endstring()


#---------------------------------------

# a function which takes a string and returns all words concatenated with the last 7 characters
def lens():
    for w in words[:]:
        if len(w) > 10:
            print (w, len(w))
print lens()



