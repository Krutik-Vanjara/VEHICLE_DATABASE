import cx_Oracle
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='XE')
connection = cx_Oracle.connect(user='C##admin_user', password='password', dsn=dsn_tns)

# Create a cursor object
cursor = connection.cursor()

# Execute a query to fetch all car details
query = """
    SELECT Car_ID, Make, Model, Price, Year, Fuel_Type, Location, Transmission
    FROM C##car_schema.CarDetails
"""
cursor.execute(query)
car_details = cursor.fetchall()

# Function to fetch columns for filtering
def fetch_columns_for_filtering(event=None):
    try:
        cursor.execute("""
            SELECT COLUMN_NAME 
            FROM ALL_TAB_COLUMNS 
            WHERE TABLE_NAME = 'CARDETAILS' 
            AND OWNER = 'C##CAR_SCHEMA'
        """)
        columns = cursor.fetchall()
        
        if not columns:
            messagebox.showinfo("No Data", "No columns found to fetch.")
            return

        column_names = [column[0] for column in columns]
        
        # Update comboboxes with column names
        column_filter_combobox_1['values'] = column_names
        column_filter_combobox_2['values'] = column_names
        column_filter_combobox_3['values'] = column_names
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch columns: {e}")

def fetch_column_values(column_name, value_combobox):
    try:
        query = f"SELECT DISTINCT {column_name} FROM C##car_schema.CarDetails"
        cursor.execute(query)
        values = cursor.fetchall()
        
        value_list = [value[0] for value in values]
        value_combobox['values'] = value_list
        value_combobox.set('')
        
        if not value_list:
            messagebox.showinfo("No Data", f"No values found for {column_name}.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch values: {e}")

# Function to fetch values automatically when a column is selected for filtering
def on_column_select(event, column_combobox, value_combobox):
    selected_column = column_combobox.get()
    if selected_column:
        fetch_column_values(selected_column, value_combobox)

# Function to apply filters and fetch filtered data
def fetch_filtered_data():
    try:
        filter_conditions = []
        
        # Build filter conditions based on selected values in comboboxes
        if column_filter_combobox_1.get() and value_filter_combobox_1.get():
            filter_conditions.append(f"{column_filter_combobox_1.get()} = '{value_filter_combobox_1.get()}'")
        
        if column_filter_combobox_2.get() and value_filter_combobox_2.get():
            filter_conditions.append(f"{column_filter_combobox_2.get()} = '{value_filter_combobox_2.get()}'")
        
        if column_filter_combobox_3.get() and value_filter_combobox_3.get():
            filter_conditions.append(f"{column_filter_combobox_3.get()} = '{value_filter_combobox_3.get()}'")
        
        # Construct the WHERE clause for the query based on selected filters
        where_clause = " AND ".join(filter_conditions) if filter_conditions else ""
        query = f"""
            SELECT Car_ID, Make, Model, Price, Year, Fuel_Type, Location, Transmission
            FROM C##car_schema.CarDetails
            {"WHERE " + where_clause if where_clause else ""}
        """
        
        cursor.execute(query)
        filtered_data = cursor.fetchall()
        
        # Clear the current treeview
        for row in treeview.get_children():
            treeview.delete(row)
        
        # Insert the filtered data into the treeview
        for row in filtered_data:
            treeview.insert("", "end", values=row)
        
        if not filtered_data:
            messagebox.showinfo("No Data", "No data found for the applied filters.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch filtered data: {e}")

# Function to generate a CSV report
def generate_report():
    try:
        # Ask the user for a location to save the report
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        
        if not file_path:
            return  # If no file path is selected, exit the function
        
        # Get all rows from the treeview
        rows = treeview.get_children()
        
        # Write the rows to a CSV file
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            
            # Write the column headings
            writer.writerow(columns)
            
            # Write the data rows
            for row in rows:
                writer.writerow(treeview.item(row)["values"])
        
        messagebox.showinfo("Report Generated", f"Report has been saved to {file_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate the report: {e}")

# GUI Application
app = tk.Tk()
app.title("Car Database Management")
app.geometry("800x600")

# Grid layout for better structure
tk.Label(app, text="Select Column 1 to Filter by:").grid(row=0, column=0, padx=10, pady=10)
column_filter_combobox_1 = ttk.Combobox(app, state="readonly")  # Column filter 1
column_filter_combobox_1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Select Column 2 to Filter by:").grid(row=0, column=2, padx=10, pady=10)
column_filter_combobox_2 = ttk.Combobox(app, state="readonly")  # Column filter 2
column_filter_combobox_2.grid(row=0, column=3, padx=10, pady=10)

tk.Label(app, text="Select Column 3 to Filter by:").grid(row=1, column=0, padx=10, pady=10)
column_filter_combobox_3 = ttk.Combobox(app, state="readonly")  # Column filter 3
column_filter_combobox_3.grid(row=1, column=1, padx=10, pady=10)

# Column filter value comboboxes
tk.Label(app, text="Select Value for Filter 1:").grid(row=1, column=2, padx=10, pady=10)
value_filter_combobox_1 = ttk.Combobox(app, state="readonly")
value_filter_combobox_1.grid(row=1, column=3, padx=10, pady=10)

tk.Label(app, text="Select Value for Filter 2:").grid(row=2, column=0, padx=10, pady=10)
value_filter_combobox_2 = ttk.Combobox(app, state="readonly")
value_filter_combobox_2.grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="Select Value for Filter 3:").grid(row=2, column=2, padx=10, pady=10)
value_filter_combobox_3 = ttk.Combobox(app, state="readonly")
value_filter_combobox_3.grid(row=2, column=3, padx=10, pady=10)

# Fetch Columns Button
fetch_columns_button = ttk.Button(app, text="Fetch Columns", command=fetch_columns_for_filtering)
fetch_columns_button.grid(row=3, column=0, columnspan=4, pady=10)

# Apply Filter Button
filter_button = ttk.Button(app, text="Apply Filter", command=fetch_filtered_data)
filter_button.grid(row=4, column=0, columnspan=4, pady=10)

# Treeview to show filtered data
columns = ("Car_ID", "Make", "Model", "Price", "Year", "Fuel_Type", "Location", "Transmission")
treeview = ttk.Treeview(app, columns=columns, show="headings")
treeview.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Define column headings
for col in columns:
    treeview.heading(col, text=col)

# Generate Report Button
report_button = ttk.Button(app, text="Generate CSV Report", command=generate_report)
report_button.grid(row=6, column=0, columnspan=4, pady=20)

# Function to bind events for each combobox after they are defined
def bind_column_filter_events():
    column_filter_combobox_1.bind("<<ComboboxSelected>>", lambda event: on_column_select(event, column_filter_combobox_1, value_filter_combobox_1))
    column_filter_combobox_2.bind("<<ComboboxSelected>>", lambda event: on_column_select(event, column_filter_combobox_2, value_filter_combobox_2))
    column_filter_combobox_3.bind("<<ComboboxSelected>>", lambda event: on_column_select(event, column_filter_combobox_3, value_filter_combobox_3))

# Call the bind function to activate the events after creating the comboboxes
bind_column_filter_events()

# Run the GUI
app.mainloop()

# Close the cursor and connection after finishing
cursor.close()
connection.close()
