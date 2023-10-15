employees = [
    {"id": "1784", "name": "Albert", "surname": "Goff", "job_title": "sales manager", "salary": 1350},
    {"id": "1594", "name": "Karlos", "surname": "Kondori", "job_title": "brigade chief", "salary": 1450},
    {"id": "1274", "name": "Ashley", "surname": "Gobs", "job_title": "accountant", "salary": 1640},
    {"id": "1954", "name": "Ewa", "surname": "Brown", "job_title": "chief engineer", "salary": 1350},
    {"id": "1834", "name": "Rozie", "surname": "Lewandowska", "job_title": "engineer", "salary": 1200}
]

def displey_records (list_of_employees):
    """Отобразить все записи о сотрудниках"""
    for employee in list_of_employees:
        for employee_ in employee: # Отображает значение отдельно от ключа
            print(employee_, '-', employee[employee_])
        print('\t')


def search_employee_by_id (list_of_employees):
    """Найти сотрудника по ID"""
    count = 0
    employee_id = str(input("Enter employee ID: "))
    for employee in list_of_employees:
        if employee['id'] == employee_id:
            print (employee)
            count+=1
    if count == 0: print ('Here is no employee with this ID')


def add_employee (list_of_employees):
    """Добавить сотрудника"""
    new_employee = {}
    new_employee['id'] = str(input("Enter an ID of a new employee: "))
    for employee in list_of_employees:
        if new_employee['id'] == employee['id']:
            act = str(input("Employee with the same ID is already exist\n"
                            "If you want to return to the menu press Enter "))
            if act == '': main()
            else : add_employee(list_of_employees)
    new_employee['name'] = str(input("Enter a name of a new employee: "))
    new_employee['surname'] = str(input("Enter an surname of a new employee: "))
    new_employee['salary'] = int(input("Enter an salary of a new employee: "))
    new_employee['job_title'] = str(input("Enter an job title of a new employee: "))
    list_of_employees.append(new_employee)
    # print(list_of_employees)
    return list_of_employees


def calculate_average_salary(list_of_employees):
    """Посчитать среднюю зп всех сотрудников"""
    sum_salaries = 0
    for employee in list_of_employees:
        sum_salaries += employee.get("salary")
    average_salary = sum_salaries/len(list_of_employees) # Делит сумму зп на кол-во записей
    print(f"Average salary = {average_salary}")


def find_highest_lowest_salary(list_of_employees):
    """Вывести наименьшю и наибольшую зп сотрудников"""
    salaries = []
    for employee in list_of_employees:
        salaries.append(employee.get('salary')) # Добавляет все зп в отдельный список
    salaries.sort() # Сортировка списка
    for employee in list_of_employees:
        # Условие необходимо для того, чтобы к зп "вытащить" из списка сотрудников данные сотрудников с такой зп
        if employee.get('salary') == salaries[0]:
            print(f"Lowest salary = {salaries[0]}, name and surname of employee - {employee.get('name')}"
                  f" {employee.get('surname')}, job title - {employee.get('job_title')}")
        elif employee.get('salary') == salaries[len(salaries)-1]:
            print(f"Highest salary = {salaries[len(salaries)-1]}, name and surname of employee - {employee.get('name')}"
                  f" {employee.get('surname')}, job title - {employee.get('job_title')}")


def remove_employee_by_id(list_of_employees):
    """Удалить запись о сотруднике"""
    employee_id = str(input("Enter employee ID: "))
    count = 0
    for employee in list_of_employees:
        if employee.get('id') == employee_id:
            print(f"an employee's record has been expunged {employee}")
            list_of_employees.remove(employee)
            count += 1
    if count == 0 : print("Here is no employee with this ID")
    #print(f"{list_of_employees}")


def update_employee_by_id(list_of_employees):
    """Обновить запись/записи о сотруднике"""
    employee_id = str(input("Enter employee ID you want to update: "))
    count = 0
    for employee in list_of_employees:
        if employee['id'] == employee_id:
            count += 1
            while (True):
                key_num = str(input('Enter what you want to change\n 1. name\n 2. surname\n 3. salary\n 4. job_title'
                ' (empty enter - exit)\n '))
                if key_num == '1':
                    print('Enter name: ')
                    employee['name'] = input()
                elif key_num == '2':
                    print('Enter surname: ')
                    employee['surname'] = input()
                elif key_num == '3':
                    print('Enter salary: ')
                    employee['salary'] = input()
                elif key_num == '4':
                    print('Enter job_title: ')
                    employee['job_title'] = input()
                elif key_num == '':
                    break
    if count == 0: print("Here is no employee with this ID")
    #print(f"{list_of_employees}")


def main():
    while (True):
        action = str(
            input("\n Hi, it`s Employee Managment System\n Сhoose an action\n 1. Display of all employee records\n "
                  "2. Search for employee data by ID \n 3. Add a new employee\n "
                  "4. Find out the average salary for all employees\n "
                  "5. Display of the employee/employees with the highest and lowest salaries\n "
                  "6. Delete an employee by ID\n "
                  "7. Update employee information\n (empty enter - exit)\n"))

        if action == '1':
            displey_records(employees)
        elif action == '2':
            search_employee_by_id(employees)
        elif action == '3':
            add_employee(employees)
            #print(employees)
        elif action == '4':
            calculate_average_salary(employees)
        elif action == '5':
            find_highest_lowest_salary(employees)
        elif action == '6':
            remove_employee_by_id(employees)
            #print(employees)
        elif action == '7':
            update_employee_by_id(employees)
            #print(employees)
        elif action == '':
            break


if __name__ == '__main__':
    main()

