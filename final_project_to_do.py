import csv
from datetime import datetime
KEY_ID = 0
VALUE_ID = 1

def main():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("4. Delete task")
    print("Enter to do list \n")
    
    menu = ""
    while menu != "3":
        menu = input("Enter menu choice: ")
        if menu == "1":   
            add_items() 
        elif menu == "2":            
            product_dict = view_task("todo_list.csv")
            current_date_and_time = datetime.now()       
            print("---------------------\n")
            print(f"{current_date_and_time:%A %B %d %Y %I:%M:%S}\n")
            for key, value in product_dict.items():
                print(f"{key}: {value}")             
            print("---------------------")
        elif menu == "3":
            print("Exiting...")
            break
        elif menu == "4":            
            delete_task("todo_list.csv")

# Function to add text to the todo-list to the CSV file.
def add_items():    
    try:
        current_date_and_time = datetime.now() 
        print(f"\n{current_date_and_time:%A %B %d %Y %I:%M:%S}")
        date_of_week = input("Enter the day of the week to add the task: ")
        user_input = input("Enter the task you want to add: ")
        with open("todo_list.csv", "r", newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)                
                # Loop through rows to find the matching date
                for row in rows:
                    if date_of_week == row[0]:
                        # Update the task for the matched date
                        row[1] = user_input
                        break  # Exit loop once updated
                print("task has been added successfully!\n")

    # Write updated data to the CSV file
        with open("todo_list.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    except ValueError as error:
        print(f"Did not find the file {error}")

# Function to view the todo-list from the CSV file.    
def view_task(filename):  
    view_dict = {}
    # This function will view only when the user enter a selection from the menu, and will display to view from the todo list according the day of the week.
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        for key in reader: 
            day_of_week = key[KEY_ID] 
            day_of_task = key[VALUE_ID]
            view_dict[day_of_week] = day_of_task 
    return view_dict
        

# Function to delete the todo-list was entered by the user from the CSV file.
def delete_task(filename):
    date_of_week = input("Enter the week day to add the task: ")
    
    with open(filename, "r", newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            # Loop through rows to find the matching date of the week
            for row in rows:
                user_input = row[1]
                if date_of_week == row[0]:
                    # Update the task for the matched date of the week
                    row[1] = user_input[:0]
                    break  # Exit loop once updated
            print("task has been deleted successfully!\n")

    # Write updated data to the CSV file
    with open("todo_list.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

if __name__ == "__main__":
    main()