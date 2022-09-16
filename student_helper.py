import pickle  


expenses = dict()
expenses["food"] = []
expenses["home"] = []
expenses["fun"] = []
expenses["other"] = []
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
def read():
    global expenses
    file = open("helper.bin", "rb")
    expenses = pickle.load(file)
    file.close
def saving():
    file = open("helper.bin", "wb")
    pickle.dump(expenses, file)
    file.close()
def show_expense(month):
    for key in expenses: 
        monthly = []
        print(key + ":")
        for i in expenses[key]:
            if i[1] == month:
                monthly.append(i[0])
                print("\t" + str(i[0]) + "zł") 
        print(f"\t {key} cost u {sum(monthly)}zł a month")
def add_expense(month):
    print()
    expense_amount = int(input("Amount: "))
    expense_type = input("(food, home, fun, other)?: ")

    expense = (expense_amount, month)
    expenses[expense_type].append(expense)

while True:
    print()
    month = int(input("Choose month 1,12: "))
    if month > 12 or month < 1:
        print("Wrong value")
        continue
    while True:
        print()
        print("0. Choose other month: ")
        print("1. Show expenses: ")
        print("2. Add expense: ")
        print("3. Save file: ")
        print("4. Restore notes: ")
        choise = int(input("Choose your option: "))

        if choise == 0:
            break
        if choise == 1:
            show_expense(month)
        if choise == 2: 
            add_expense(month)
        if choise == 3:
            saving()
            print("file saved!")
            break
        if choise == 4:
            read()