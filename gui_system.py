import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk  # To handle images

# Initialize CustomTkinter
ctk.set_appearance_mode("light")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (default), "green", "dark-blue"

# Function to handle login logic
def login():
    role = role_var.get()
    username = username_entry.get()
    password = password_entry.get()

    # Simple role-based login
    if username == "admin" and password == "admin123" and role == "Admin":
        open_admin_dashboard()
    elif username == "manager" and password == "manager123" and role == "Manager":
        open_manager_dashboard()
    elif username == "user" and password == "user123" and role == "User":
        open_user_dashboard()
    else:
        messagebox.showerror("Login Error", "Invalid login credentials.")

# Function to open Admin Dashboard
def open_admin_dashboard():
    login_frame.pack_forget()  # Hide the login frame
    heading_label.configure(text="Admin Dashboard")
    admin_dashboard_frame.pack(fill="both", expand=True)

# Function to open Manager Dashboard
def open_manager_dashboard():
    login_frame.pack_forget()  # Hide the login frame
    heading_label.configure(text="Manager Dashboard")
    manager_dashboard_frame.pack(fill="both", expand=True)

# Function to open User Dashboard
def open_user_dashboard():
    login_frame.pack_forget()  # Hide the login frame
    heading_label.configure(text="User Dashboard")
    user_dashboard_frame.pack(fill="both", expand=True)

# Function to handle logout
def logout():
    heading_label.configure(text="Car Database")  # Reset heading label
    login_frame.pack(fill="both", expand=True)  # Show login frame

# Admin Dashboard Functions
def add_user():
    messagebox.showinfo("Add User", "User added successfully!")

def delete_user():
    messagebox.showinfo("Delete User", "User deleted successfully!")

def generate_sales_report():
    messagebox.showinfo("Sales Report", "Sales report generated!")

# Manager Dashboard Functions
def add_product():
    messagebox.showinfo("Add Product", "Product added successfully!")

def view_orders():
    messagebox.showinfo("View Orders", "Viewing orders!")

# User Dashboard Functions
def search_cars():
    messagebox.showinfo("Search Cars", "Searching cars by name or fuel type!")

def view_order_history():
    messagebox.showinfo("Order History", "Viewing order history!")

# Create the main window
root = ctk.CTk()
root.title("System GUI")
root.geometry("800x600")

# Add a heading label for all pages
heading_label = ctk.CTkLabel(root, text="Car Database", font=("Arial", 24))
heading_label.pack(pady=20)

# Add an image to the login page
image = Image.open("C:/Users/Krutik/adbm project/shopping.ico")  # Replace with your image path
image = image.resize((150, 150))  # Resize image as needed
photo = ImageTk.PhotoImage(image)

image_label = ctk.CTkLabel(root, image=photo, text="")
image_label.pack()

# Create a frame for login
login_frame = ctk.CTkFrame(root, border_color="black")
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

# Admin Dashboard Frame
admin_dashboard_frame = ctk.CTkFrame(root)
ctk.CTkButton(admin_dashboard_frame, text="Add User", command=add_user).pack(pady=10)
ctk.CTkButton(admin_dashboard_frame, text="Delete User", command=delete_user).pack(pady=10)
ctk.CTkButton(admin_dashboard_frame, text="Generate Sales Report", command=generate_sales_report).pack(pady=10)
ctk.CTkButton(admin_dashboard_frame, text="Logout", command=lambda: [admin_dashboard_frame.pack_forget(), logout()]).pack(pady=20)

# Manager Dashboard Frame
manager_dashboard_frame = ctk.CTkFrame(root)
ctk.CTkButton(manager_dashboard_frame, text="Add Product", command=add_product).pack(pady=10)
ctk.CTkButton(manager_dashboard_frame, text="View Orders", command=view_orders).pack(pady=10)
ctk.CTkButton(manager_dashboard_frame, text="Logout", command=lambda: [manager_dashboard_frame.pack_forget(), logout()]).pack(pady=20)

# User Dashboard Frame
user_dashboard_frame = ctk.CTkFrame(root)
ctk.CTkButton(user_dashboard_frame, text="Search Cars", command=search_cars).pack(pady=10)
ctk.CTkButton(user_dashboard_frame, text="View Order History", command=view_order_history).pack(pady=10)
ctk.CTkButton(user_dashboard_frame, text="Logout", command=lambda: [user_dashboard_frame.pack_forget(), logout()]).pack(pady=20)

# Start the GUI loop
root.mainloop()
