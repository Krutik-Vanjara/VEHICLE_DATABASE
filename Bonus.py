import cx_Oracle
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

# Connection parameters
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='XE')
connection = cx_Oracle.connect(user='C##admin_user', password='password', dsn=dsn_tns)

print("Connected to the database successfully!")


# Create a cursor object
cursor = connection.cursor()

# Execute a query to count cars based on location and fuel type
location = 'Pune'
fuel_type = 'Petrol'
query = """
    SELECT COUNT(*) 
    FROM C##car_schema.CarDetails 
    WHERE Location = :location AND Fuel_Type = :fuel_type
"""

cursor.execute(query, {'location': location, 'fuel_type': fuel_type})

# Fetch the result
result = cursor.fetchone()
print(f"Number of cars in {location} with {fuel_type}: {result[0]}")

# Close the cursor and connection
cursor.close()
connection.close()

# Function to connect to the database and fetch query results
def fetch_results():
    try:
        # Get multiple inputs from the user
        locations = location_entry.get().split(",")  # e.g., "Pune,Mumbai"
        fuel_types = fuel_type_entry.get().split(",")  # e.g., "Petrol,Diesel"

        # Convert lists to a comma-separated string for the query
        locations_str = ", ".join([f"'{loc.strip()}'" for loc in locations])
        fuel_types_str = ", ".join([f"'{ft.strip()}'" for ft in fuel_types])

        # Connect to the database
        connection = cx_Oracle.connect(user='C##admin_user', password='password', dsn='XE')
        cursor = connection.cursor()

        # Updated query with dynamic IN clause
        query = f"""
            SELECT Location, Fuel_Type, COUNT(*) AS Car_Count
            FROM C##car_schema.CarDetails
            WHERE Location IN ({locations_str}) AND Fuel_Type IN ({fuel_types_str})
            GROUP BY Location, Fuel_Type
            ORDER BY Car_Count DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()

        # Display results in GUI
        result_text = "\n".join([f"{row[0]} ({row[1]}): {row[2]} cars" for row in results])
        result_label.config(text=result_text or "No data found!")

        cursor.close()
        connection.close()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch results: {e}")

# Function to generate a report in CSV format
def generate_report():
    try:
        # Connect to the database
        connection = cx_Oracle.connect(user='C##admin_user', password='password', dsn='XE')
        cursor = connection.cursor()

        # Execute the report query
        query = """
            SELECT Fuel_Type, Location, COUNT(*) AS Car_Count
            FROM C##car_schema.CarDetails
            GROUP BY Fuel_Type, Location
            ORDER BY Car_Count DESC
        """
        cursor.execute(query)

        # Save results to a CSV file
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")],
                                                 title="Save Report As")
        if file_path:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([desc[0] for desc in cursor.description])  # Column headers
                writer.writerows(cursor.fetchall())  # Data rows

            messagebox.showinfo("Success", "Report generated successfully!")

        # Close the connection
        cursor.close()
        connection.close()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")

# GUI Application
app = tk.Tk()
app.title("Car Database Management")
app.geometry("400x300")

# Location Input
tk.Label(app, text="Enter Location:").pack(pady=5)
location_entry = ttk.Entry(app)
location_entry.pack(pady=5)

# Fuel Type Input
tk.Label(app, text="Enter Fuel Type:").pack(pady=5)
fuel_type_entry = ttk.Entry(app)
fuel_type_entry.pack(pady=5)

# Fetch Results Button
fetch_button = ttk.Button(app, text="Fetch Results", command=fetch_results)
fetch_button.pack(pady=10)

# Result Label
result_label = tk.Label(app, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Generate Report Button
report_button = ttk.Button(app, text="Generate Report", command=generate_report)
report_button.pack(pady=10)

# Run the GUI
app.mainloop()