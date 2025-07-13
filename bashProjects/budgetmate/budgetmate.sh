#!/bin/bash

# File to store budget data
DATA_FILE="budget_data.txt"

# Budget values
income=0
bills=()

# Load saved data if file exists
load_data() {
    if [[ -f "$DATA_FILE" ]]; then
        source "$DATA_FILE"
        echo "Data loaded from $DATA_FILE."
    else
        echo "No saved data found."
    fi
}

# Save current income and bills to file
save_data() {
    {
        echo "income=$income"
        for i in "${!bills[@]}"; do
            echo "bills[$i]=\"${bills[$i]}\""
        done
    } > "$DATA_FILE"
    echo "Data saved to $DATA_FILE."
}

# Add paycheck income
enter_income() {
    read -p "Enter total paycheck amount: $" income
}

# Add a bill
add_bill() {
    read -p "Enter bill name: " name
    read -p "Enter amount for $name: $" amount
    bills+=("$name:$amount")
}

# Show summary
show_summary() {
    echo "------ Budget Summary ------"
    echo "Paycheck Income: $${income}"
    total_bills=0
    for bill in "${bills[@]}"; do
        name=$(echo "$bill" | cut -d':' -f1)
        amount=$(echo "$bill" | cut -d':' -f2)
        echo "- $name: $${amount}"
        total_bills=$(echo "$total_bills + $amount" | bc)
    done
    echo "Total Bills: $${total_bills}"
    balance=$(echo "$income - $total_bills" | bc)
    echo "Remaining Balance: $${balance}"
    echo "----------------------------"
}

# Main menu
while true; do
    echo ""
    echo "===== BudgetMate ====="
    echo "1. Enter Paycheck Income"
    echo "2. Add a Bill"
    echo "3. View Budget Summary"
    echo "4. Save to File"
    echo "5. Load from File"
    echo "6. Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1) enter_income ;;
        2) add_bill ;;
        3) show_summary ;;
        4) save_data ;;
        5) load_data ;;
        6) echo "Goodbye!"; break ;;
        *) echo "Invalid option. Try again." ;;
    esac
done

