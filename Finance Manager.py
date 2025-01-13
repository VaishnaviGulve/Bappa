import pandas as pd
import matplotlib.pyplot as plt

class FinanceManager:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Category', 'Amount'])
        print("Initialized empty transactions DataFrame")

    def add_transaction(self, date, category, amount):
        print(f"Adding transaction - Date: {date}, Category: {category}, Amount: {amount}")
        new_transaction = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)
        print("Current transactions DataFrame:")
        print(self.transactions)

    def view_transactions(self):
        print("Viewing all transactions:")
        print(self.transactions)

    def plot_expenses(self):
        expense_data = self.transactions[self.transactions['Amount'] < 0]
        if not expense_data.empty:
            print("Plotting expenses...")
            expense_data.groupby('Category')['Amount'].sum().plot(kind='bar')
            plt.title('Expenses by Category')
            plt.xlabel('Category')
            plt.ylabel('Amount')
            plt.show()
        else:
            print("No expense data to plot.")

manager = FinanceManager()
manager.add_transaction('2025-01-01', 'Groceries', -500)
manager.add_transaction('2025-01-02', 'Salary', 3000)
manager.add_transaction('2025-01-03', 'Entertainment', -200)
manager.view_transactions()
manager.plot_expenses()
