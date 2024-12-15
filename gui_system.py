import cx_Oracle
import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd

# Oracle Database Connection Function
def connect_to_database():
    try:
        # Replace these details with your database credentials
        connection = cx_Oracle.connect(
            user="system",
            password="12345",
            dsn="localhost/XE"  # Replace with your database host and service name
        )
        return connection
    except cx_Oracle.Error as e:
        messagebox.showerror("Database Connection Error", str(e))
        return None

# Function to fetch car data from the database
def fetch_car_data():
    connection = connect_to_database()
    if not connection:
        return []
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT CAR_ID, MAKE, MODEL, PRICE, YEAR, FUEL_TYPE, LOCATION,TRANSMISSION
            FROM CARDETAILS  -- Replace with your actual table name
        """)
        data = cursor.fetchall()  # Fetch all rows from the query result
        connection.close()
        return data
    except cx_Oracle.Error as e:
        messagebox.showerror("Database Query Error", str(e))
        return []

# Function to handle login logic
def login():
    role = role_var.get()
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password" and role == "Admin":
        configure_dashboard("Admin")
    elif username == "manager" and password == "password" and role == "Manager":
        configure_dashboard("Manager")
    elif username == "user" and password == "password" and role == "User":
        configure_dashboard("User")
    else:
        messagebox.showerror("Login Error", "Invalid login credentials.")

# Function to reset and show the login page
def show_login_page():
    heading_label.configure(text="Car Database")
    for frame in [admin_dashboard_frame, manager_dashboard_frame, user_dashboard_frame]:
        frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

# Function to configure dashboards dynamically
def configure_dashboard(role):
    login_frame.pack_forget()
    heading_label.configure(text=f"{role} Dashboard")

    if role == "Admin":
        frame = admin_dashboard_frame
    elif role == "Manager":
        frame = manager_dashboard_frame
    else:
        frame = user_dashboard_frame

    for child in frame.winfo_children():
        child.destroy()  # Clear previous widgets

    # Add common widgets
    ctk.CTkButton(frame, text="Search", command=lambda: search_data(frame)).pack(pady=10)
    search_entry = ctk.CTkEntry(frame, placeholder_text="Search by Make or Model")
    search_entry.pack(pady=10)
    create_table_view(frame, ["CAR_ID", "MAKE", "MODEL", "PRICE", "YEAR", "FUEL_TYPE", "LOCATION", "TRANSMISSION"])
    ctk.CTkButton(frame, text="Generate Report", command=lambda: generate_report(fetch_car_data())).pack(pady=10)
    ctk.CTkButton(frame, text="Logout", command=show_login_page).pack(pady=10)
    frame.search_entry = search_entry
    frame.pack(fill="both", expand=True)

# Function to search and display data in a table
def search_data(frame):
    query = frame.search_entry.get().lower()
    data = fetch_car_data()

    # Filter data based on query
    filtered_data = [row for row in data if query in row[1].lower() or query in row[2].lower()]

    # Clear previous treeview data
    for row in frame.tree.get_children():
        frame.tree.delete(row)

    # Insert new data into treeview
    for row in filtered_data:
        frame.tree.insert("", "end", values=row)

# Function to add treeview for displaying data
def create_table_view(frame, columns):
    frame.tree = ttk.Treeview(frame, columns=columns, show='headings')
    for col in columns:
        frame.tree.heading(col, text=col)
        frame.tree.column(col, width=150)
    frame.tree.pack(fill="both", expand=True)

# Function to generate an Excel report
def generate_report(table_data, filename="Car_Report.xlsx"):
    df = pd.DataFrame(table_data, columns=["CAR_ID", "MAKE", "MODEL", "PRICE", "YEAR", "FUEL_TYPE", "LOCATION", "TRANSMISSION"])
    try:
        df.to_excel(filename, index=False, engine="openpyxl")
        messagebox.showinfo("Report Generated", f"Report has been saved as {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")

# Create the main window
root = ctk.CTk()
root.title("Car Database System")
root.geometry("1000x700")

# Add a heading label for all pages
heading_label = ctk.CTkLabel(root, text="Car Database", font=("Arial", 24))
heading_label.pack(pady=20)

# Create a frame for login
login_frame = ctk.CTkFrame(root)
login_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Login Page Widgets
ctk.CTkLabel(login_frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
username_entry = ctk.CTkEntry(login_frame)
username_entry.grid(row=0, column=1)

ctk.CTkLabel(login_frame, text="Password").grid(row=1, column=0, padx=10, pady=10)
password_entry = ctk.CTkEntry(login_frame, show="*")
password_entry.grid(row=1, column=1)

ctk.CTkLabel(login_frame, text="Select Role").grid(row=2, column=0, padx=10, pady=10)
role_var = ctk.StringVar()
role_dropdown = ctk.CTkOptionMenu(login_frame, variable=role_var, values=["Admin", "Manager", "User"])
role_dropdown.grid(row=2, column=1)

login_button = ctk.CTkButton(login_frame, text="Login", command=login)
login_button.grid(row=3, columnspan=2, pady=20)

# Admin, Manager, and User Dashboard Frames
admin_dashboard_frame = ctk.CTkFrame(root)
manager_dashboard_frame = ctk.CTkFrame(root)
user_dashboard_frame = ctk.CTkFrame(root)

# Start the GUI loop
root.mainloop()
