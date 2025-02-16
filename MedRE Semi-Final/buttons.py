import ttkbootstrap as ttk
from tkinter import messagebox
import re
from ttkbootstrap.tooltip import ToolTip
from tkinter import PhotoImage
from tkinter import ttk
import datetime

def on_add_click(entries_per, entries, table):
    try:
        # Perform validation
        updated_name = entries_per['name_entry'].get()
        medication_name = entries['medication_entry'].get()
        time = entries['time_entry'].get()
        frequency = entries['frequency_picker'].get()
        dosage_amount = entries['dosage_amount_entry'].get()
        dosage_type = entries['dosage_type_picker'].get()

        # Additional validation code
        if not medication_name:
            raise ValueError("Medication name cannot be empty")
        if not time:
            raise ValueError("Time cannot be empty")
        if not frequency:
            raise ValueError("Frequency must be selected")
        if not dosage_amount:
            raise ValueError("Dosage amount cannot be empty")
        if not dosage_type:
            raise ValueError("Dosage type must be selected")
        if not dosage_amount.isdigit():
            raise ValueError("Dosage amount must be a number")
        if not re.match(r'^\d{2}:\d{2} (AM|PM)$', time):
            raise ValueError("Time must be in HH:MM format")

        # Add the medication reminder to the table
        table.insert('', 'end', values=(updated_name, medication_name, time, frequency, dosage_amount + ' ' + dosage_type))
        messagebox.showinfo("Success", "Medication reminder added successfully!")
    except ValueError as ve:
        messagebox.showwarning("Validation Error", ve)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def refill_day(entries):
    medication_duration = int(entries['medicine_entry1'].get())
    # Get the current date
    current_date = datetime.datetime.now()
    # Get the number of days to add
    num_days = int(medication_duration)-1

    # Add the days to the current date
    new_date = current_date + datetime.timedelta(days=num_days)
    
    # # Create an alert message
    if current_date==new_date:
        message = f"1 day left if needed please refill your medicine"
        # Display the alert message       
        messagebox.showinfo("refill medication", message)

def delete_click(table):
    # Get the selected item from the table
    selected = table.selection()[0]
    # Delete the selected item
    table.delete(selected)

def clear_click(table):
    # Clear the table
    table.delete(*table.get_children())

def on_clear_click(entries):
    # Clear all entry fields
    entries['medication_entry'].delete(0, 'end')
    entries['time_entry'].delete(0, 'end')
    entries['frequency_picker'].delete(0, 'end')
    entries['dosage_amount_entry'].delete(0, 'end')
    entries['dosage_type_picker'].delete(0, 'end')

def create_buttons(root, button_frame, entries, table):
    # Load icons
    
    delete_icon = PhotoImage(file='./delete_icon.png').subsample(4,4)
    clear_icon = PhotoImage(file='./clear_icon.png').subsample(4,4)
    edit_icon = PhotoImage(file='./edit_icon.png').subsample(4,4)  
    # Create buttons with icons and apply the success style
    
    delete_button = ttk.Button(button_frame, text="Delete", image=delete_icon, compound='left', command=lambda: delete_click(table), style='Success.TButton')
    clear_button = ttk.Button(button_frame, text="Clear Table", image=clear_icon, compound='left', command=lambda: clear_click(table), style='Success.TButton')
    clear_button = ttk.Button(button_frame, text=" X ", image=clear_icon, compound='left', command=lambda: on_clear_click(entries), style='Success.TButton')

    # Keep a reference to the images to prevent garbage collection
    delete_button.image = delete_icon
    clear_button.image = clear_icon

    # Position the register, delete, and clear buttons above the table to the left of the search bar
    delete_button.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
    clear_button.grid(row=3, column=2, padx=5, pady=5, sticky='ew')
    clear_button.grid(row=3, column=3, padx=5, pady=5, sticky='ew')

    # Bind keyboard shortcuts to the buttons
    root.bind('<Control-a>', lambda event: on_add_click(entries, table))
    root.bind('<Control-d>', lambda event: delete_button.invoke())
    root.bind('<Control-c>', lambda event: clear_button.invoke())

    # Edit button moved to buttons.py
    edit_button = ttk.Button(button_frame, text="Edit", image=edit_icon, compound='left', command=lambda: edit_details(table), style='Success.TButton')
    edit_button.image = edit_icon
    edit_button.grid(row=3, column=3, padx=5, pady=5, sticky='ew')

    def edit_details(table):
        selected_item = table.selection()[0]  # Get the ID of the selected item
        item_values = table.item(selected_item, 'values')  # Fetch the values of the selected item
        
        # Assuming 'entries' is a dictionary containing the entry widgets for editing
        entries['medication_entry'].delete(0, 'end')
        entries['medication_entry'].insert(0, item_values[1])  # Medication Name
        
        entries['time_entry'].delete(0, 'end')
        entries['time_entry'].insert(0, item_values[2])  # Time
        
        entries['frequency_picker'].set(item_values[3])  # Frequency
        
        entries['dosage_amount_entry'].delete(0, 'end')
        entries['dosage_amount_entry'].insert(0, item_values[4])  # Dosage Amount
        
        # Assuming there's a dosage type in the values and an entry for it
        entries['dosage_type_picker'].set(item_values[5])  # Dosage Type

    # Adding tooltips to all entry areas and buttons
    ToolTip(entries['medication_entry'], text="Enter the name of the medication")
    ToolTip(entries['time_entry'], text="Enter the time for the medication reminder in HH:MM AM/PM format")
    ToolTip(entries['frequency_picker'], text="Select the frequency of the medication")
    ToolTip(entries['dosage_amount_entry'], text="Enter the amount of dosage")
    ToolTip(entries['dosage_type_picker'], text="Select the type of dosage")

    # ToolTip(add_button, text="Register new medication reminder")
    ToolTip(delete_button, text="Delete selected medication reminder")
    ToolTip(clear_button, text="Clear all medication reminders from the table")
    ToolTip(edit_button, text="Edit selected medication reminder details")
