# AUTHOR: JOSEPH GREGORY Z. CABINTA
# DATE CREATED: 2023-11-28
# DATE UPDATE: 2023-12-03
# purpose: log cashflow

from transaction import Transaction
from tabulate import tabulate
import os
import itertools
import calendar
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# =================================================
# ------------- DEFINE MAIN FUNCTION --------------
# =================================================

def main():
    print("\n..........🔎💵..........")
    print("Welcome to Cash Flow Tracker!")
    transaction_file_path = "cashflow.csv"
    main_user = "Iggy"

    while True:
        print("\n........................")
        print("Select an option")
        action_prompt = "  1. 🖊️ Log a transaction?\n" \
                        "  2. 📑 View transaction summary?\n" \
                        "  3. 🗑️ Delete transaction log/s?\n" \
                        "  4. 🔴 Exit "
        action_values = ['1','2','3','4']
        action = validate_input(action_prompt,action_values) 

        if action == str(1): # Log a transaction
            transaction = get_user_transaction(main_user)
            save_transaction_to_file(transaction, transaction_file_path)

        elif action == str(2) or action == str(3): # View transaction summary
            try:
                if os.path.getsize(transaction_file_path) > 2: 
                    if action == str(2): # View transaction summary
                        summarize_transaction(transaction_file_path)
                    elif action == str(3): # Delete transaction summary
                        delete_transaction(transaction_file_path)
                else: # size of below 2 is too small to be an entry
                    print("\n❗ No transactions have been logged")
            except OSError:
                    print("\n❗ No transaction log created")


        elif action == str(4): # Exit
            exit()

# =================================================
# ------- ACTION FUNCTION: USER TRANSACTION -------
# =================================================

def get_user_transaction(main_user):
    print("\n........................")
    print("Getting User Transaction")

    transaction_date = input("\nEnter transaction date (YYYY-MM-DD): ") # Point. figure out how to remember last input date, or to add multiple transaction at a date input and how to filter by day,month,year
    transaction_kind = select_kind() 
    transaction_category = select_category(transaction_kind)
    transaction_name = input("\nEnter transaction remarks (e.g. \"siomai\"): ")
    
    if transaction_kind == "Expense" or transaction_kind == "Income":
        # for expense and income, flow of question is:
        # date -> type -> category -> name -> **amount -> account**
        transaction_account = input("Transaction is accountable to? (e.g. Iggy): ")

        prompt_amount = float(input("Enter transaction amount (in ₱, e.g. \"300\"): "))
        if transaction_kind == "Expense":
            prompt_amount = prompt_amount*-1
        transaction_amount = prompt_amount

    elif transaction_kind == "Borrow" or transaction_kind == "Repay":
        # for borrow and repay, flow of question is:
        # date -> type -> category -> name -> **account -> amount** 

        if transaction_kind == "Borrow":
            parties = input("Parties involved? (Lender,Borrower) \n").split(',')
        else:
            parties = input("Parties involved? (Payor,Recepient) \n").split(',')
        p_label = ['_'.join(parties)][0]
        transaction_account = p_label

        prompt_amount = float(input("Enter transaction amount (in ₱, e.g. \"300\"): "))
        if transaction_account.split('_')[0] == main_user:
            prompt_amount = prompt_amount*-1
        transaction_amount = prompt_amount

    new_transaction = Transaction(
                    date=transaction_date,
                    kind=transaction_kind,
                    category=transaction_category, 
                    name=transaction_name, 
                    amount=transaction_amount,
                    account=transaction_account
                    ) # Point. convert this to dataframe?
    return new_transaction

# =================================================
# --------------- SELECT FUNCTIONS ----------------
# =================================================

def select_kind():
    kind_categories = [
            "💸 Expense",
            "💰 Income", 
            "⏱️ Borrow", 
            "🔁 Repay" # Point. add payment protocol
            ]
    while True:
        print("\nSelect a transaction type: ")
        for i, kind_name in enumerate(kind_categories):
            print(f"{i+1: 2d}. {kind_name}")

        value_range = f"[ 1 - {len(kind_categories)} ]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        
        if i in range(len(kind_categories)):
            selected_kind = kind_categories[selected_index][2:]
            return selected_kind
        else:
            print("\n❗ Invalid category. Please try again!") # Point. Streamline invalid reports into the invalid function?

"""
def initiate_borrow()
     print("Parties involved? (Lender,Borrower)")
     parties = input() #(Iggy,Aly)
     if parties[0] == main_user:
         amount =
"""

def select_category(transaction_kind):
    expense_categories = [
            "🥩 Food",
            "💊 Health",
            "🧼 Hygiene",
            "💄 Beauty",
            "👕 Apparel",
            "🏡 Home",
            "🧽 Kitchen",
            "🚽 Bathroom",
            "🧺 Laundry",
            "🔨 Hardware",
            "📱 Gadgets",
            "🏫 Education",
            "📝 Office",
            "📃 Government",
            "🚗 Car",
            "🚅 Transportation",
            "🎁 Gift",
            "🎀 Donation",
            "🎪 Admission",
            "🏧 Transaction"
            ]

    income_categories = [
            "👔 Salary",
            "🧧 Allowance",
            "🪙 Stipend"
            ]
    borrow_categories = [
            "🙋 Personal",
            "🏦 Commercial",
            ]

    if transaction_kind == "Expense":
        transaction_categories = expense_categories
    elif transaction_kind == "Income":
        transaction_categories = income_categories
    else:
        transaction_categories = borrow_categories

    while True:
        print("\nSelect a category: ")
        for i, category_name in enumerate(transaction_categories):
            print(f"{i+1: >2d}. {category_name}")

        value_range = f"[ 1 - {len(transaction_categories)} ]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        
        if i in range(len(transaction_categories)):
            selected_category = transaction_categories[selected_index][2:]
            return selected_category
        else:
            print("\n❗ Invalid category. Please try again!")

"""
def entry_amount(transaction_kind):
    prompt_amount = float(input("Enter transaction amount (in ₱, e.g. \"300\"): "))
    if transaction_kind == "Expense":
        sign_amount = float(prompt_amount*-1)
    elif transaction_kind == "Income":
        sign_amount = prompt_amount
    elif transaction_kind == "Borrow"
        temp_parties
        parties = input() #(Iggy,Aly)
        
    elif transaction_kind == "Repay"
    return sign_amount
        
def detail_borrow()
    if transaction_kind == "Borrow"
        print("Parties involved? (Lender,Borrower)")
        parties = input().split(',') #(Iggy,Aly)
        p_label = ['_'.join(p) for p in parties]
        return p_label
#        if parties[0] == main_user:
#            assign_borrow = "Lender"
#        else:
#            assign_borrow = "Borrower"
"""

# =============================================
# --- ACTION FUNCTION: SAVE EXPENSE TO FILE ---
# =============================================

def save_transaction_to_file(transaction: Transaction, transaction_file_path):
    print(f"\n📝 Saving User Transaction: {transaction} to {transaction_file_path}")
    with open(transaction_file_path, "a") as f:
        f.write(f"{transaction.date},"+
                f"{transaction.kind},"+
                f"{transaction.category},"+
                f"{transaction.name},"+
                f"{transaction.amount},"+
                f"{transaction.account}\n") # Point. add option to delete or modify entry

# =============================================
# ------- ACTION FUNCTION: VIEW SUMMARY -------
# =============================================

def delete_transaction(transaction_file_path):
    print("\n........................")
    print(f"Delete User Transaction\n")

    cols = [
            'date',
            'type',
            'category',
            'name',
            'amount',
            'account'
            ] # Point. add method (credit card, gcash, physical wallet, paymaya, beep)

    df_file = pd.read_csv("cashflow.csv", names=cols, header=None)
    while True:
        print(tabulate(df_file,headers='keys',tablefmt='psql'))

        print("\nSelect range of rows to delete ")
        drop_1 = int(input("  Row start: "))
        drop_2 = int(input("  Row end:   "))+1
        print(" ")
        df_drop = df_file.drop(df_file.index[drop_1:drop_2]).reset_index()
        print(df_drop)
    
        drop_prompt = ("\nSave changes? (y/n) ")
        drop_values = ['y','n']
        drop_choice = validate_input(drop_prompt, drop_values)
        
        if drop_choice == 'y':
            df_final = df_drop.drop(['index'],axis=1) 
            df_final.to_csv('cashflow.csv', header=None,index=False)
            break
        else:
            print("\n⏪ Repeat selection of rows\n")

def summarize_transaction(transaction_file_path):
    print("\n........................")
    print(f"Summarizing User Transaction\n")

    cols = [
            'date',
            'type',
            'category',
            'name',
            'amount',
            'account'
            ] # Point. add method (credit card, gcash, physical wallet, paymaya, beep)

    df_file = pd.read_csv("cashflow.csv", names=cols, header=None)

    sieve_prompt = "📦 Prepare a filtered summary? (y/n) "
    sieve_values = ['y','n']
    sieve_choice = validate_input(sieve_prompt, sieve_values)
    
    # proceed to filter
    if sieve_choice == 'y':
        sieve = {}

        scheme_prompt = "\nFilter by: date,type,account (y/n)(y/n)(y/n)\n"\
                       "(e.g. yyy or nnn or yny) "
        permutations = list(itertools.product(['y','n'], repeat=3))
        scheme_values = [''.join(p) for p in permutations]
        scheme_choice = validate_input(scheme_prompt, scheme_values)
       
        scheme_list = list(scheme_choice)

        if scheme_list[0] == 'y':
            c_date = input('\nFilter by date: ')
            sieve['date'] = c_date
        if scheme_list[1] == 'y':
            c_kind = select_kind() 
            sieve['type'] = c_kind
        if scheme_list[2] == 'y':
            c_account = input("\nFilter by account: ")
            sieve['account'] = c_account

       # compare sieve dictionary and df_file data frame
       # prepare tables
       # t_format = "headers='keys',tablefmt='psql',showindex=False"

        print("\n📑 Complete list of transactions\n")
        df_filter = df_file.loc[(df_file[list(sieve)] == pd.Series(sieve)).all(axis=1)]
        df_sieved = df_filter.sort_values('date')
        print(tabulate(df_sieved,headers='keys',tablefmt='psql',showindex=False))

        print("\n📑 Total amount per account, type, category\n")
        df_group1 = df_sieved.groupby(['account','type','category'])['amount'].sum().reset_index()
        print(tabulate(df_group1,headers='keys',tablefmt='psql',showindex=False))

        print("\n📑 Total amount per account, type\n")
        df_group2 = df_sieved.groupby(['account','type'])['amount'].sum().reset_index()
        print(tabulate(df_group2,headers='keys',tablefmt='psql',showindex=False))

    # don't filter
    elif sieve_choice == "n":
        
        # prepare tables
        # t_format = "headers='keys',tablefmt='psql',showindex=False"

        print("\n📑 Complete list of transactions\n")
        df_sieved = df_file.sort_values('date') # Point. How to add emoji in table without ruining alignment
        print(tabulate(df_sieved,headers='keys',tablefmt='psql',showindex=False))

        print("\n📑 Total amount per year, month, account, type, category\n")
        df_sieved[['year','month','date']] = df_sieved['date'].str.split('-',n=2,expand=True)
        df_group0 = df_sieved.groupby(['year','month','account','type','category'])['amount'].sum().reset_index()
        print(tabulate(df_group0,headers='keys',tablefmt='psql',showindex=False))
#        plotdata.plot(kind="bar")
#        df_group0.plot(x="type",y="amount", kind="bar")

        # df_sieved.hist(column='account',by='type', figsize=[12, 8], bins=15)
        # plt.show()

        print("\n📑 Total amount per account, type, category\n")
        df_group1 = df_sieved.groupby(['account','type','category'])['amount'].sum().reset_index()
        print(tabulate(df_group1,headers='keys',tablefmt='psql',showindex=False))

        print("\n📑 Total amount per account, type\n")
        df_group2 = df_sieved.groupby(['account','type'])['amount'].sum().reset_index()
        print(tabulate(df_group2,headers='keys',tablefmt='psql',showindex=False))

"""
    # Point. add budget data 
    remaining_budget = budget - total_spent
    print(f"Budget remaining ₱{remaining_budget:.2f}\n")

    #Get the current date
    now = datetime.datetime.now()
    #Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    #Calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day
    print("Remaining days in the current month:", remaining_days)

    try:
        daily_budget = remaining_budget / remaining_days
        print(f"Budget Per Day: ₱{daily_budget:.2f}\n")
    except ZeroDivisionError:
        print("This is the last day of the month")
"""

# =============================================
# --------- FUNCTION TO VALIDATE INPUT --------
# =============================================

def validate_input(prompt, values):
    while True:
        x = input(prompt) 
        if x in values:
            return x
        print("\n❗ Invalid value, options are " + str(values) + "\n")

# =============================================
# ------------------- END ---------------------
# =============================================

if __name__ == "__main__":
    main()

