import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        p = float(entry_principal.get())
        t = float(entry_time.get())
        r = float(entry_rate.get())

        si = (p * t * r) / 100
        ci = p * (pow((1 + r / 100), t)) - p

        label_si_res.config(text=f"Simple Interest: {si:.2f}")
        label_ci_res.config(text=f"Compound Interest: {ci:.2f}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

root = tk.Tk()
root.title("Interest Calculator App")
root.geometry("400x400")
root.config(bg="#f0f0f0")

tk.Label(root, text="Principal Amount:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Time (years):", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Rate of Interest (%):", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=1, padx=10, pady=10)

btn_calculate = tk.Button(root, text="Calculate", command=calculate_interest, bg="#4CAF50", fg="white", width=15)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=20)

label_si_res = tk.Label(root, text="Simple Interest: -", font=("Arial", 10, "bold"), bg="#f0f0f0", fg="#333")
label_si_res.grid(row=4, column=0, columnspan=2, pady=5)

label_ci_res = tk.Label(root, text="Compound Interest: -", font=("Arial", 10, "bold"), bg="#f0f0f0", fg="#333")
label_ci_res.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()