import ttkbootstrap as ttk
from ttkbootstrap.tooltip import ToolTip
from ttkwidgets.autocomplete import AutocompleteCombobox

def add_placeholder(entry, placeholder, color='grey'):
    style = ttk.Style()
    style.map('Placeholder.TEntry',
              foreground=[('!focus', color), ('focus', 'black')])

    def on_focusin(event):
        if entry.get() == placeholder:
            entry.delete(0, 'end')
            entry.config(style='')  # Reset to default style
    
    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(style='Placeholder.TEntry')  # Apply placeholder style
    
    entry.insert(0, placeholder)
    entry.config(style='Placeholder.TEntry')
    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")
    ToolTip(entry, text=f"Enter {placeholder.lower()}")  # Adding tooltip to entry

def load_medications(filename):
    with open(filename, 'r') as file:
        # This assumes one medication name per line
        return [line.strip() for line in file if line.strip()]

def create_prescription_details(prescription_details_frame):
    # Medication Details
    medication_label = ttk.Label(prescription_details_frame, text="Medication Name:", style='TLabel')
    medication_label.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    medication_names = load_medications('medications.csv')
    medication_entry = AutocompleteCombobox(prescription_details_frame, completevalues=medication_names)
    add_placeholder(medication_entry, 'Enter medication name')
    medication_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(medication_entry, text="Enter the name of the medication")  # Adding tooltip

    # Time Details
    time_label = ttk.Label(prescription_details_frame, text="Time:", style='TLabel')
    time_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
    time_entry = ttk.Entry(prescription_details_frame)
    add_placeholder(time_entry, 'HH:MM AM/PM')
    time_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(time_entry, text="Enter the time for the medication")  # Adjust tooltip as needed

    medicine_duration = ttk.Label(prescription_details_frame, text="medicine duration(in days):", style='Tlabel')
    medicine_duration.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
    medicine_entry1 = ttk.Entry(prescription_details_frame)
    add_placeholder(medicine_entry1, 'Enter total medicine duration')
    medicine_entry1.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(medicine_entry1, text="Enter the duration for the medication in days")  # Adding tooltip

    # Frequency
    frequency_label = ttk.Label(prescription_details_frame, text="Frequency:", style='TLabel')
    frequency_label.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
    frequency_picker = ttk.Combobox(prescription_details_frame)
    frequency_picker['values'] = ['Daily', 'Weekly', 'Monthly']
    frequency_picker.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(frequency_picker, text="Select the frequency of the medication")  # Adding tooltip

    # Dosage Type Details
    dosage_type_label = ttk.Label(prescription_details_frame, text="Dosage Type:", style='TLabel')
    dosage_type_label.grid(row=4, column=0, padx=5, pady=5, sticky='ew')
    dosage_type_picker = ttk.Combobox(prescription_details_frame)
    dosage_type_picker['values'] = ['Tablet', 'Liquid (ml)', 'Injection (ml)', 'Drops']
    dosage_type_picker.grid(row=4, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(dosage_type_picker, text="Select the type of dosage")  # Adding tooltip

    # Dosage Amount Details
    dosage_amount_label = ttk.Label(prescription_details_frame, text="Dosage Amount:", style='TLabel')
    dosage_amount_label.grid(row=5, column=0, padx=5, pady=5, sticky='ew')
    dosage_amount_entry = ttk.Entry(prescription_details_frame)
    add_placeholder(dosage_amount_entry, 'Enter dosage amount')
    dosage_amount_entry.grid(row=5, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(dosage_amount_entry, text="Enter the amount of dosage")  # Adding tooltip

    return {
        'medication_entry': medication_entry,
        'time_entry': time_entry,
        'medicine_entry1': medicine_entry1,
        'frequency_picker': frequency_picker,
        'dosage_amount_entry': dosage_amount_entry,
        'dosage_type_picker': dosage_type_picker
    }