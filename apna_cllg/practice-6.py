#give employ record in the form of a test of tuply where each tuple contain 
#(employ ID, employee name , salary)
#example (101, "alice",50000)  (102, "bob", 65000) (103, "charlie", 45000)
#ask user to enter employ id and search it inside record

detail = (
    (101, "alice", 50000),
    (102, "bob", 65000),
    (103, "charlie",45000)
)
emp_id = int(input("enter the employ id to search: "))

found = False

for employ in detail:
    if detail[0] == emp_id:
        print("Employee found :")
        print("Employee id", detail[0])
        print("employ name", detail[1])
        print("salary", detail[2])
        found = True
        break


if not found:
    print("Employee id not found")   




# employees = (
#     (101, "Alice", 50000),
#     (102, "Bob", 65000),
#     (103, "Charlie", 45000)
# )

# emp_id = int(input("Enter employee ID to search: "))

# found = False

# for employee in employees:
#     if employee[0] == emp_id:
#         print("Employee found:")
#         print("ID:", employee[0])
#         print("Name:", employee[1])
#         print("Salary:", employee[2])
#         found = True
#         break

# if not found:
#     print("Employee ID not found.")
