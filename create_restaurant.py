import sqlite3


def create_employee(id_, name, monthly_salary, yearly_bonus, position):
    return {"id": id_, "name": name, "monthly_salary": monthly_salary,
            "yearly_bonus": yearly_bonus, "position": position}


def create_table(cursor):
    cursor.execute('''CREATE TABLE employees
(id int, name text, monthly_salary int, yearly_bonus int, position text)''')


def insert(item, cursor):
    id_ = item["id"]
    name = item["name"]
    monthly_salary = item["monthly_salary"]
    yearly_bonus = item["yearly_bonus"]
    position = item["position"]

    insert_query = "INSERT INTO employees VALUES(?, ?, ?, ?, ?)"
    cursor.execute(insert_query,
                  (id_, name, monthly_salary, yearly_bonus, position))


def main():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    create_table(cursor)

    elena = create_employee(1, "Elena", 5000, 10000, "Manager")
    velyana = create_employee(2, "Velyana", 500, 100, "Cashier")
    konchita = create_employee(3, "Konchita", 200, 100, "cleaner")

    employees = [elena, velyana, konchita]
    for employee in employees:
        insert(employee, cursor)
        conn.commit()

    conn.close()


if __name__ == '__main__':
    main()
