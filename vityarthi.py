### Bank Account Details (Dictionary)
Accounts = {
    "321321321":{
        "Name of the account holder":"Mahee Kotecha",
        "Balance":"21000",
        "Account_type":"current",
        "Pending_loans":"No",
        "Documents_attached":["Aadhar card","Ration card"]
    },
    "654654654":{
        "Name of the account holder":"Devansh Garg",
        "Balance":"70000",
        "Account_type":"saving",
        "Pending_loans":"Education_loan",
        "Documents_attached":["Aadhar card","Passport"]
    },
    "987987987":{
        "Name of the account holder":"Chirag Kunvar",
        "Balance":"34500", "Account_type":"salary",
        "Pending_loans":"House_loan",
        "Documents_attached":"Pan card"
    },
    "123456789":{
        "Nmae of the account holder":"Aarvi Kapoor",
        "Balance":"23007",
        "Account_type":"salary",
        "Pending_loans":"No",
        "Documents_attached":["Pan card","student ID"],
    }
}

#Input (Account number of the customer)
Acc_no = input("Enter Bank Account Number:")   

print("\n---Account Details---")

#We need to check whether the account exists or not .
if Acc_no in Accounts:
    details = Accounts[Acc_no]
    print("Account_Number:",Acc_no)
    print("Customer_Name:",details ["Name of the account holder"])
    print("Account_Balance:",details ["Balance"])
    print("Account_type:",details ["Account_type"])
    print("Loans:",details ["Pending_loans"])
    print("Documents:",details ["Documents_attached"])
else:
    print("No such account exists.Please check your account number again.")

#Eligibility for loan
Loan_stat=input("Loan_status:")

if Loan_stat == 'NO':
    print("Eligible")
    print("Required Documents:")
    print("Last 2 years ITR statement\nCresdit Score\nGovernmnet ID")
    print("Please submit this attested documents")

#For Loan Calculation
    Pri_amt=int(input("Enter the amount :"))
    Pri_time=int(input("Enter the time(in years):"))
    sim_rate=int(input("Enter rate(in %) :"))
    sim_int=((Pri_amt*sim_rate*Pri_time)/100)                  # Simple Interest = (Principal*Rate*Time)/100
    print("Simple Interest on the principal is :")
    print(sim_int)
# Total amount need to be repaid
    Total_amount = Pri_amt + sim_int
    print("Total amount need to be repaid:")
    print(Total_amount)

#Amount to be repaid per month for 2 years
    print("Amount to be paid (per month) for 2 years:")
    Amt_monthly = Total_amount / 24
    print(Amt_monthly)

if Loan_stat == 'YES' :
    print("Not Eligible")

    