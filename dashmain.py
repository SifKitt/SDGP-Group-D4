from tkinter import *

# --- MAIN WINDOW ---
dashboard = Tk()
dashboard.geometry("800x600")
dashboard.title("Paragon Apartment Management System - Tenant Dashboard")

# --- TITLE ---
title_label = Label(dashboard, text="Tenant Dashboard", font=("Arial", 20))
title_label.pack(pady=20)

# -------------------------------
# FUNCTION: OPEN MAINTENANCE PAGE
# -------------------------------
def open_maintenance():
    maintenance_window = Toplevel(dashboard)
    maintenance_window.geometry("400x400")
    maintenance_window.title("Maintenance Requests")

    Label(maintenance_window, text="Submit Maintenance Request", font=("Arial", 14)).pack(pady=10)

    entry = Entry(maintenance_window, width=40)
    entry.pack(pady=5)

    status = Label(maintenance_window, text="")
    status.pack(pady=5)

    requests = []

    def submit():
        text = entry.get()
        if text != "":
            requests.append(text)
            status.config(text="Request submitted!")
            entry.delete(0, END)
        else:
            status.config(text="Enter a request first")

    Button(maintenance_window, text="Submit", command=submit).pack(pady=5)


# -------------------------------
# FUNCTION: OPEN PAYMENTS PAGE
# -------------------------------
def open_payments():
    payments_window = Toplevel(dashboard)
    payments_window.geometry("400x400")
    payments_window.title("Payments")

    Label(payments_window, text="Payment Information", font=("Arial", 14)).pack(pady=10)

    Label(payments_window, text="Rent Due: £1200").pack(pady=5)
    Label(payments_window, text="Status: Unpaid").pack(pady=5)

    def pay():
        status_label.config(text="Payment Successful!")

    status_label = Label(payments_window, text="")
    status_label.pack(pady=10)

    Button(payments_window, text="Pay Now", command=pay).pack(pady=5)


# -------------------------------
# FUNCTION: OPEN PROFILE PAGE
# -------------------------------
def open_profile():
    profile_window = Toplevel(dashboard)
    profile_window.geometry("400x400")
    profile_window.title("My Profile")

    Label(profile_window, text="Tenant Profile", font=("Arial", 14)).pack(pady=10)

    Label(profile_window, text="Name: John Doe").pack(pady=5)
    Label(profile_window, text="Apartment: A12").pack(pady=5)
    Label(profile_window, text="Email: johndoe@email.com").pack(pady=5)


# -------------------------------
# DASHBOARD BUTTONS
# -------------------------------
Button(dashboard, text="Maintenance Requests", width=25, command=open_maintenance).pack(pady=10)

Button(dashboard, text="View Payments", width=25, command=open_payments).pack(pady=10)

Button(dashboard, text="My Profile", width=25, command=open_profile).pack(pady=10)


# --- RUN APP ---
dashboard.mainloop()