import os 



file = open('./directory/file.txt', 'w')
students_list = [
    {'name': 'hamid', 'age': 45},
    {'name': 'hamid 2', 'age': 4},
    {'name': 'hamid 3', 'age': 5},
]

file.write(','.join(str(item) for item in students_list[0].keys())+'\n')

for student in students_list:
    file.write(','.join(str(item) for item in student.values())+'\n')

exist = os.path.exists('./directory')
print(exist)
