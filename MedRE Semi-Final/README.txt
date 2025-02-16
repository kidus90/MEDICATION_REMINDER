Medication Reminder Application Documentation

----------------------------------------------------------------------------------------------------------------------------
Introduction
----------------------------------------------------------------------------------------------------------------------------

This application is a comprehensive medication reminder tool that allows users to manage their medication schedules, 
receive reminders, and track their medication usage. It features a user-friendly graphical interface, input validation, 
a sortable table for viewing reminders, and customizable notifications.

----------------------------------------------------------------------------------------------------------------------------
Features
----------------------------------------------------------------------------------------------------------------------------
* User-Friendly GUI: Utilizes the ttkbootstrap library for a modern and intuitive graphical user interface.
* Medication Reminder Management: Add, delete, and clear medication reminders.
* Input Validation: Validate user input for critical fields, including medication name, time, frequency, dosage amount, and dosage type.
* Table Display: Display medication reminders in a sortable table for easy viewing and selection.
* Refill Reminder: Calculate medication duration and send a refill reminder when the refill day approaches.
* Tooltips: Provide helpful guidance and explanations for each button.
* Keyboard Shortcuts: Support keyboard shortcuts for common actions (add, delete, clear).

----------------------------------------------------------------------------------------------------------------------------
Installation and Usage
----------------------------------------------------------------------------------------------------------------------------
1. Install the required Python libraries (ttkbootstrap and mysql.connector).
2. Download the application code and unzip the files.
3. Open the downloaded folder and locate the .py file.
4. Run the .py file to launch the application.
5. Follow the on-screen instructions to add and manage your medication reminders.

-----------------------------------------------------------------------------------------------------------------------------
User Interface
-----------------------------------------------------------------------------------------------------------------------------
The application features a simple and intuitive user interface. The main window is divided into three sections:

*Prescription Details: Contains fields for entering medication details, such as the medication name, time, frequency, dosage amount, and dosage type.
*Personal Information: Contains fields for entering the user's name, phone number, emergency contact name, and emergency contact phone number.
*Medication Reminder List: A sortable table that displays the added medication reminders.

-----------------------------------------------------------------------------------------------------------------------------
Adding a Medication Reminder
-----------------------------------------------------------------------------------------------------------------------------
To add a medication reminder, simply fill in the fields in the "Prescription Details" section and click the "Add" button. The 
application will validate your input and add the reminder to the table.

##Deleting a Medication Reminder

To delete a medication reminder, select it in the table and click the "Delete" button. The reminder will be removed from the table.

##Clearing All Reminders

To clear all medication reminders from the table, click the "Clear" button.

## Refilling Medication

The application will calculate the medication duration based on the information you entered and send a reminder when the refill day approaches.

------------------------------------------------------------------------------------------------------------------------------
Keyboard Shortcuts
------------------------------------------------------------------------------------------------------------------------------
The following keyboard shortcuts are available:

* Ctrl+A: Add a medication reminder
* Ctrl+D: Delete a medication reminder
* Ctrl+C: Clear all medication reminders

------------------------------------------------------------------------------------------------------------------------------
Additional Notes

* The application uses a MySQL database to store the medication reminder data so no data is lost.
* The application is designed to run on Windows, macOS, and Linux operating systems.