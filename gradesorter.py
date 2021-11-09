#list challenge 6 grade sorter program

print("\nWelcome to the grade sorter program")
grades = []
grade = int(input("\nWhat is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your second grade (0-100): "))
grades.append(grade)
grade = int(input("What is your third grade (0-100): "))
grades.append(grade)
grade = int(input("What is your fourth grade (0-100): "))
grades.append(grade)

#output
print("\nYour grades are: " + str(grades))

#sort from highest to lowest
grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: " + str(grades))

#drop the lowest two grades
print("\nThe last two grades will now be removed")
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))
removed_grade = grades.pop()
print("Removed grade " + str(removed_grade))

#recap remaining grade
print("\nYour remaining grade is : " + str(grades))
print("Nice work! Your highest grade is a " + str(grades[0]))





