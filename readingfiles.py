
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)                              # Opening text files

employee_file.close()