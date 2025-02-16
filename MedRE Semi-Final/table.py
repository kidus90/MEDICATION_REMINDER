import ttkbootstrap as ttk

def create_table(root):
    # Define the columns for the table
    columns = ('Name','medication', 'time', 'frequency', 'dosage')

    # Create the table with a specific style if needed
    table = ttk.Treeview(root, columns=columns, show='headings', style='Custom.Treeview')

    # Configure the column headings
    for col in columns:
        table.heading(col, text=col.capitalize())
        table.column(col, anchor='center', width=100)  # Adjust the width as needed

    # Position the table in the grid
    table.grid(row=8, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

    # Add a scrollbar
    vscroll = ttk.Scrollbar(root, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=vscroll.set)
    vscroll.grid(row=8, column=4, sticky='ns')

    # Make the table and scrollbar expandable
    root.grid_rowconfigure(8, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)

    return table