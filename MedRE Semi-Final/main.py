import ttkbootstrap as ttk
from ttkbootstrap.tooltip import ToolTip
from prescription_details import create_prescription_details
from personal_info import create_personal_info
from buttons import create_buttons,on_add_click
from table import create_table
import datetime
from tkinter import messagebox, PhotoImage
import sqlite3  # Import SQLite3 for database operations

# Initialize the main window with padding
root = ttk.Window(themename="solar")
root.title("Medication Reminder")

# Configure styles for various widgets
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 14), padding=(10, 5))
style.configure('Heading.TLabel', font=('Helvetica', 30, 'bold'))
style.configure('TEntry', font=('Helvetica', 14), padding=(10, 5))
style.configure('Success.TButton', foreground='white', background='green', font=('Helvetica', 14), padding=(10, 5))
style.configure('TCombobox', font=('Helvetica', 14), padding=(10, 5))
style.configure('Custom.Treeview', font=('Helvetica', 12))
style.configure('Custom.Treeview.Heading', font=('Helvetica', 14, 'bold'))

# Database connection setup
connection = sqlite3.connect('patients.db')
cursor = connection.cursor()

# Create the table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_name TEXT PRIMARY KEY,
        medication_name TEXT,
        time TEXT,
        frequency TEXT,
        dosage_amount TEXT,
        dosage_type TEXT
    )
""")

def retrieve_all_times():
    current_time = datetime.datetime.now().strftime("%H:%M %p")  # Lowercase for case-insensitive comparison
    cursor = connection.cursor()
    search_query = "SELECT time FROM patients"
    cursor.execute(search_query)
    print(current_time)
    time_results = cursor.fetchall()
    for time in time_results:
        if time[0] == current_time:  # Assuming time is stored as a tuple in the database
            messagebox.showinfo("reminder",f"Times up, take your medicine")
    root.after(60000, retrieve_all_times)  # calls this function every 60000 millisecond (1min)

# Add a search bar with placeholder text
search_entry = ttk.Entry(root)
search_entry.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

# Define the add_placeholder function
def add_placeholder(entry_widget, placeholder_text):
    def on_focus_in(event):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, "end")
            entry_widget.config(style='')  # Revert to default style on focus

    def on_focus_out(event):
        if not entry_widget.get():
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(style='Placeholder.TEntry')  # Apply custom style

    entry_widget.insert(0, placeholder_text)
    entry_widget.config(style='Placeholder.TEntry')  # Apply custom style initially
    entry_widget.bind("<FocusIn>", on_focus_in)
    entry_widget.bind("<FocusOut>", on_focus_out)

# Define a new style for the Entry widget that has grey text for the placeholder
style.map('Placeholder.TEntry',
          foreground=[('!focus', 'grey'), ('focus', 'black')])

# Assuming you have a ttk.Entry widget named search_entry
search_entry = ttk.Entry(root)
search_entry.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
add_placeholder(search_entry, 'Search by patient name or use " /ALL " function to list all')

# Load the search icon
search_icon = PhotoImage(file='MedRE Semi-Final/search_icon.png').subsample(4, 4)

# Modify the search button creation to include the icon and adjust width
search_button = ttk.Button(root, text="Search", image=search_icon, compound='left',command=lambda: search_patient())
search_button.image = search_icon  # Keep a reference to prevent garbage collection
search_button.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

# Optionally, adjust the button's width by configuring its style
style.configure('TButton', width=8)  # Adjust the width as needed

# Function to search patient
def search_patient():
    search1=search_entry.get()
    cursor=connection.cursor()
    if search1=="/ALL":
        search_query = "SELECT * FROM patients"
        cursor.execute(search_query)
        search_results = cursor.fetchall()
    else:
        search_query = "SELECT * FROM patients WHERE patient_name LIKE ?"
        cursor.execute(search_query, ("%" + search1 + "%",))
        search_results = cursor.fetchall()

    if search_results:
        # Assuming 'table' is your Treeview widget for displaying search results
        for item in table.get_children():
            table.delete(item)  # Clear existing entries in the table
        for result in search_results:
            table.insert('', 'end', values=result)  # Populate the table with search results
    else:
        messagebox.showinfo("Search Results", "No results found.")

# Create the "Prescription Details" section
prescription_details_frame = ttk.LabelFrame(root, text="Prescription Details", padding=(10, 10))
prescription_details_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
prescription_details_frame.grid_columnconfigure(1, weight=1)

# Create the "Personal Information" section
personal_info_frame = ttk.LabelFrame(root, text="Personal Information", padding=(10, 10))
personal_info_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew', rowspan=3)
personal_info_frame.grid_columnconfigure(1, weight=1)

# Initialize UI components for prescription details and personal information
prescription_entries = create_prescription_details(prescription_details_frame)
personal_info_entries = create_personal_info(personal_info_frame)

# Initialize the table for displaying data
table = create_table(root)

# Initialize the frame for action buttons
button_frame = ttk.Frame(root)
button_frame.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky='ew')

# Create action buttons
create_buttons(root, button_frame, prescription_entries, table)

add_icon = PhotoImage(file='MedRE Semi-Final/add_icon.png').subsample(4,4)
save_changes_button = ttk.Button(button_frame, command=lambda: save_changes(personal_info_entries,prescription_entries),text="Register", image=add_icon, compound='left', style='Success.TButton')
save_changes_button.image = add_icon
save_changes_button.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
ToolTip(save_changes_button, text="Register new medication reminder")

# Function to save changes to the database (modified to create new entries)
def save_changes(entries_per,entries):
    # Retrieve updated values from entries
    updated_name = entries_per['name_entry'].get()
    medication_name = entries['medication_entry'].get()
    time = entries['time_entry'].get()
    frequency = entries['frequency_picker'].get()
    dosage_amount = entries['dosage_amount_entry'].get()
    dosage_type = entries['dosage_type_picker'].get()
    on_add_click(entries_per,entries, table)

    insert_query = """INSERT INTO patients (patient_name, medication_name, time, frequency, dosage_amount, dosage_type) VALUES (?, ?, ?, ?, ?, ?)"""
    cursor.execute(insert_query, (updated_name, medication_name, time, frequency, dosage_amount, dosage_type))

    connection.commit()

# Display a status message to the user
status_message = ttk.Label(root, text="Please fill in the medication details and click 'Add'.", style='TLabel')
status_message.grid(row=10, column=0, columnspan=4, padx=5, pady=5, sticky='ew')
retrieve_all_times()
# Start the main application loop
root.mainloop()

# Close the database connection when the application is closed
connection.close()