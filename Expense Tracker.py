import os
import pandas as pd
import matplotlib.pyplot as plt

EXPENSE_FILE = "expenses.csv"

def initialize_file():
    if not os.path.exists(EXPENSE_FILE):
        df = pd.DataFrame(columns=["Date","Category","Description","Amount"])
        df.to_csv(EXPENSE_FILE,index=False)

def add_expense():
    date = input("Enter date (YYYY-MM-DD):")
    category = input("Enter category(e.g., Food, Travel, Bills): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    new_expense = {"Date":date, "Category":category, "Description":description, "Amount":amount}
    df = pd.api
    