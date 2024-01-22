import os
expenses=[]
def add_expenses():
    os.system('cls')
    date=input("enter date in dd-mm-yyyy format:")
    expense=float(input("Enter your expenses:"))
    category=input("enter category type of expenses:")
    expenses.append({"date":date,"expense":expense,'category':category})
def view_spending_patterns():
    os.system('cls')
    for e in expenses:
        for k,v in e.items():
            print(k,":",v,end="  ")
        print("\n")
        
def categorise_expense():
    os.system('cls')
    f=0
    categ=input("Enter a category to categorise:")
    for e in expenses:
        if categ.lower()==e['category'].lower():
            f=1
            print("date:",e['date'],"expense:",e['expense'])
    if f==0:
        print('you enter wrong category')

while True:
    print("1.Add Expenses\n2.View spending patterns\n3.Categorise Expenses\n4.Exit")
    n= int(input("Enter your choice:"))
    if n==1:
        add_expenses()
    elif n==2:
        view_spending_patterns()
    elif n==3:
        categorise_expense()
    elif n==4:
        print("Goodbye!")
        break
    else:
        print("You enter invalid choice")
