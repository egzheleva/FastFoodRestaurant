import sqlite3


def add_employee(cursor, employee):
    id_ = employee['id']
    name = employee['name']
    monthly_salary = employee['monthly_salary']
    yearly_bonus = employee['yearly_bonus']
    position = employee['position']

    insert_query = "INSERT INTO employees VALUES(?, ?, ?, ?, ?)"

    cursor.execute(insert_query,
                  (id_, name, monthly_salary, yearly_bonus, position))
    return "employee {0} was added to the database".format(name)


def list_employees(cursor):
    employees = cursor.execute("SELECT id, name, position FROM employees")
    result = ["{0} - {1} - {2}".format(id_, name, position)
              for id_, name, position in employees]

    return "\n".join(result)


def delete_employee(cursor, employee_id):
    delete_query = "DELETE FROM employees WHERE id=?"
    cursor.execute(delete_query, (str(employee_id)))
    return "employee with id {0} was removed from the DB".format(employee_id)


def update_employee(cursor, employee_id):
    name = input("new name: ")
    monthly_salary = input("new monthly salary: ")
    yearly_bonus = input("new yearly bonus: ")
    position = input("new position: ")

    update_query = '''UPDATE employees
                      SET name=?, monthly_salary=?, yearly_bonus=?, position=?
                      WHERE id is ?'''
    cursor.execute(update_query, (name,
                                  monthly_salary,
                                  yearly_bonus,
                                  position,
                                  employee_id))
    return "employee with id {0} was updated".format(employee_id)


def monthly_spending(cursor):
    salaries = cursor.execute("SELECT monthly_salary FROM employees")
    return sum(map(lambda salary: salary[0], salaries))


def yearly_spending(cursor):
    salaries = cursor.execute('''SELECT monthly_salary, yearly_bonus
                                 FROM employees''')
    return sum(map(lambda salary: salary[0] * 12 + salary[1], salaries))
