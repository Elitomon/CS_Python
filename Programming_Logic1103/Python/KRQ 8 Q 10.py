# quiz 8
# fixing bad code

name = input('Enter student\'s name: ')

grade1 = float(input('Enter the 1st test grade: '))
grade2 = float(input('Enter the 2nd test grade: '))
grade3 = float(input('Enter the 3rd test grade: '))

sumGrades = grade1 + grade2 + grade3
avGrade = (float(sumGrades) / 3)
print('The average test score for', name, 'is', round(avGrade, 2))
