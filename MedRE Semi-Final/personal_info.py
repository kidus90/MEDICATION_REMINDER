import ttkbootstrap as ttk
from ttkbootstrap.tooltip import ToolTip

def create_personal_info(personal_info_frame):
    # Create a style object for placeholder text in entry widgets
    style = ttk.Style()
    style.map('Placeholder.TEntry',
              foreground=[('!focus', 'grey'), ('focus', 'black')])

    # Name
    name_label = ttk.Label(personal_info_frame, text="Name:", style='TLabel')
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    name_entry = ttk.Entry(personal_info_frame, style='Placeholder.TEntry')
    name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(name_entry, text="Enter the patient's name")

    # Phone Number
    phone_label = ttk.Label(personal_info_frame, text="Phone Number:", style='TLabel')
    phone_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
    phone_entry = ttk.Entry(personal_info_frame, style='Placeholder.TEntry')
    phone_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(phone_entry, text="Enter the patient's phone number")

    emergency_contact_name_label = ttk.Label(personal_info_frame, text="Emergency Contact Name:", style='TLabel')
    emergency_contact_name_label.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
    emergency_contact_name_entry = ttk.Entry(personal_info_frame, style='Placeholder.TEntry')
    emergency_contact_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(emergency_contact_name_entry, text="Enter the emergency contact's name")

    emergency_contact_phone_label = ttk.Label(personal_info_frame, text="Emergency Contact Phone:", style='TLabel')
    emergency_contact_phone_label.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
    emergency_contact_phone_entry = ttk.Entry(personal_info_frame, style='Placeholder.TEntry')
    emergency_contact_phone_entry.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
    ToolTip(emergency_contact_phone_entry, text="Enter the emergency contact's phone number")

    return {
        'name_entry': name_entry,
        'phone_entry': phone_entry,
        'emergency_contact_name_entry': emergency_contact_name_entry,
        'emergency_contact_phone_entry': emergency_contact_phone_entry
    }