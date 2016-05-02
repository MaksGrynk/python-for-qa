# Write a program to calculate the number of times that the string 'hi' appears anywhere in the given string and change 'hi' to 'bye'. 
# Case should be ignored.

string = " hi hi bi hihih"

print "original string : ", string
print "count Hi : ", string.count("hi")
print "replace Hi with by : ", string.replace('hi', 'bye', 1)

# Unite three lists to one and print it in reverse order
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

List = list1+list2+list3
print "List : ", List
List.reverse();
print "Reverse List : ", List
