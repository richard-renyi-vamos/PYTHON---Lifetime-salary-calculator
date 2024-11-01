import tkinter as tk
from tkinter import messagebox

# Function to calculate the final monthly salary
def calculate_salary():
    try:
        # Retrieve input values
        base_salary = float(entry_base_salary.get())
        bonus = float(entry_bonus.get())
        deductions = float(entry_deductions.get())
        exchange_rate = float(entry_exchange_rate.get())

        # Calculate final salary
        final_salary = (base_salary + bonus - deductions)
        
        # Apply exchange rate if not 1 (optional)
        if exchange_rate != 1:
            final_salary_converted = final_salary * exchange_rate
            result_label.config(text=f"Final Salary: {final_salary_converted:.2f}")
        else:
            result_label.config(text=f"Final Salary: {final_salary:.2f}")
            
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
app = tk.Tk()
app.title("Salary Calculator")
app.geometry("300x300")

# Input fields
tk.Label(app, text="Base Salary (HUF):").pack()
entry_base_salary = tk.Entry(app)
entry_base_salary.pack()

tk.Label(app, text="Monthly Bonus/Allowances (HUF):").pack()
entry_bonus = tk.Entry(app)
entry_bonus.pack()

tk.Label(app, text="Deductions (HUF):").pack()
entry_deductions = tk.Entry(app)
entry_deductions.pack()

tk.Label(app, text="Currency Exchange Rate (optional):").pack()
entry_exchange_rate = tk.Entry(app)
entry_exchange_rate.insert(0, "1")  # Default is 1 (no conversion)
entry_exchange_rate.pack()

# Calculate button
calculate_button = tk.Button(app, text="Calculate", command=calculate_salary)
calculate_button.pack(pady=10)

# Result display
result_label = tk.Label(app, text="Final Salary: ")
result_label.pack()

# Run the application
app.mainloop()
