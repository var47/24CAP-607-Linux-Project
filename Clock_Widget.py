import tkinter as tk 
from time import strftime 

# Create a window 
root = tk.Tk() 
root.title("Clock Widget") 
root.geometry("250x100") 
root.resizable(False, False) 

# Define a function to update the time 
def update_time(): 
    current_time = strftime("%H:%M:%S %p")  # Format: Hour:Minute:Second AM/PM 
    time_label.config(text=current_time) 
    time_label.after(1000, update_time)  # Update every second 

# Create and configure the time label 
time_label = tk.Label(root, font=("Helvetica", 40), background="black", foreground="cyan") 
time_label.pack(anchor="center", expand=True) 

# Start updating time and run the main loop 
update_time() 
root.mainloop()