#list challenge 7 Different Types of Lists Program

print("\n\t\t\tSummary Table")

#Define list
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [4.5, 10.5, 16.3, 34.3]
num_lists = [[1,2,3],[4,5,6],[7,8,9]]

# A summary of each variable (or list)
print("\nThe variable num_strings is a " +  str((type(num_strings))))
print("It contains the elements: " + str(num_strings))
print("The element 15 is a " + str(type(num_strings[0])))

print("\nThe variable num_ints is a " + str(type(num_ints)))
print("It contains the elements: " + str(num_ints))
print("The element 15 is a " + str(type(num_ints[0])))

print("\nThe variable num_floats is a " + str(type(num_floats)))
print("It contains the elements: " + str(num_floats))
print("The element 4.5is a " + str(type(num_floats[0])))

print("\nThe variable num_lists is a " + str(type(num_lists)))
print("It contains the elements: " + str(num_lists))
print("The element[1, 2, 3] is a " + str(type(num_lists[0])))

#Permanently sort num_strings and num_ints.
print("\nNow sorting num_strings and num_ints...")
num_strings.sort()
num_ints.sort()
print("Sorted num_strings: " + str(num_strings))
print("Sorted num_ints:  " + str(num_ints))

print(num_ints)
print("\nStrings are sorted alphabeticaly while integers are sorted numericaly!!!")


