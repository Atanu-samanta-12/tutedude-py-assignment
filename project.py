emp_details = {}

def main_menu(c=0):
    print(f"📋 Main menu:\n 1.➕ Add employee\n 2.👥 View all employee\n 3.🔍 Search for employee\n 4.❌ Exit")


def view_employee(h=0):
    if len(emp_details) != 0:
        for i in emp_details:
            print(f'{"-"*25}| Id:{i} |{"-"*25}')
            for k,m in emp_details[i].items():
                print(f"{k} | {m}")
        print('-'*60)
    else:
        print("There is no employee name register!😅")

def add_empployee(x=0):
    emp_id = int(input('Employee id No: '))
    if emp_details.get(emp_id) == None:
        add_details = {
            emp_id  : {
            "👤 Name" : input("👤 Name: "),
            "🪪 Age" : int(input("🪪 Age: ")),
         "🏢 Department":  input("🏢 Department: "),
            "💵 Salary" : float(input("💵 Salary: ")),},
            }
        return emp_details.update(add_details)
    else:
        print("Please enter the unique id no. ⚠️")

def search_employee(y=0):
    l = int(input("Enter the Employee id : ", ))
    if emp_details.get(l) != None:
        for key,value in emp_details[l].items():
            print(f"{key} | {value}")
    else:
        print("Employee id not found. ⚠️")






print(f'{"-"*25} Welcome! To Employee Management System {"-"*25}\n{" "*40} 📋 Main Menu  ❌ Exit {" "*20}')

in_put = (input("Choose any one option from the above: ", ))

while True:
    
    if in_put in ["Main Menu","main menu","mainmenu","Main menu"]:
        main_menu()
        in_put2 = input("Choose any one option or serial no from the above: ", )
        while True:
            if  in_put2 in ["Add employee","add employee","Addemployee","addemployee","1"]:
                add_empployee()
                main_menu()
                in_put2 = str(input("Choose any one option from the above: ", ))
            elif in_put2 in ["View all employee","view all employee","Viewallemployee","viewallemployee","2"]:
                view_employee()
                main_menu()
                in_put2 = str(input("Choose any one option from the above: ", ))
            elif in_put2 in ["Search for employee","search for employee","searchforemployee","3"]:
                search_employee()
                main_menu()
                in_put2 = str(input("Choose any one option from the above: ", )) 
            elif in_put2 in ["exit","Exit","4"]:
                print("Thank you for visiting 🙏 We look forward to seeing you again 👋😊")
                break
            else:
                print("syntax error!🚫")
                break 
    elif in_put in ["exit","Exit"]:
        print("Thank you for visiting 🙏 We look forward to seeing you again 👋😊")
        break
    else:
        print("syntax error!🚫")
        print(f'{"-"*25} Welcome! To Employee Management System {"-"*25}\n{" "*40} Main Menu   Exit {" "*20}')
        in_put = str(input("Choose any one option from the above: ", ))
