# Python Project: Command-Line Budget Tracker

#     1: Define the Problem Clearly (What are we trying to solve, and why?)
#        -> Giving users a way to manage income and expenses from the command line.

#     2: Gather Requirements (What features must this program have to be considered “done”?)
#        -> Add an expense(name, amount, notes)
#        -> Add income(paycheck)
#        -> See remaining balance (as expenses are entered)
#        -> Track each expense as time goes on

#     3: Break It into Functional Units (Divide the features into tasks/modules.)

#        -> Task 1: User Input Handler
#            def get_user_choice():
#                """
#                Show menu and return user selection
#                """

#        -> Task 2: Add income / Add monthly expense
#            def add_income(budget_data):
#                """
#                Prompts user to enter income amount and adds it to income list.
#                Updates the total balance.
#                """
#                # Ask for amount
#                # Validate it's a number
#                # Append to income list
#                # Update running total
#                # Validate for which month

#        -> Task 3: See remaining balance
#            def display_balance(budget_data):
#                """
#                Calculate and show current total income, total expenses, and remaining balance.
#                """
#                # Sum income
#                # Sum expenses
#                # Print totals and difference

#        -> Task 4: Track each expense
#            def show_expense_history(budget_data):
#                """
#                Prints a list of all expenses, including timestamp, name, amount, category, and notes.
#                """
#                # Loop through all expenses
#                # Show each entry in a readable format

#     4: Choose the Data Structures (Decide how to store the data in memory.)
#     5: Plan the User Interaction (What will the user see, and how will they interact with it?)
#     6: Outline the Program Flow (Write out the logic in plain English or pseudocode.)
#     7: Design for Future Expansion (What if this needs to save data to a file or support multiple users later?)
#     8: Document Before You Build (Jot down your plan: what each function does, what inputs it takes, what it returns.)

import os

months = {
    "january": {"person1": [], "person2": []},
    "february": {"person1": [], "person2": []},
    "march": {"person1": [], "person2": []},
    "april": {"person1": [], "person2": []},
    "may": {"person1": [], "person2": []},
    "june": {"person1": [], "person2": []},
    "july": {"person1": [], "person2": []},
    "august": {"person1": [], "person2": []},
    "september": {"person1": [], "person2": []},
    "october": {"person1": [], "person2": []},
    "november": {"person1": [], "person2": []},
    "december": {"person1": [], "person2": []},
}




# function to clear screen
def clear_screen():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac or linux
    else:
        os.system('clear')

# function to display menu and return user selection
def get_user_choice():
    clear_screen()
    print('==============================================================')
    print('|                   Budget Calculator                        |')
    print('|        1. Add income                                       |')
    print('|        2. Add expense                                      |')
    print('==============================================================')
    selection = int(input('Enter a selection (1 or 2)\n>> '))
    return selection

#function to add income
def add_income():
    clear_screen()
    print('Enter the first name of the person the paystub we are about to enter belongs to.')
    person1 = str(input('>> '))
    print('Enter the month we need to access (Ex: "february")')
    month = str(input('>> '))

selection = get_user_choice()


