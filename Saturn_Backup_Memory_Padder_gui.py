import tkinter as tk
from tkinter import filedialog, messagebox
import os

def expand_save(input_file, output_file, pad_byte):
    # Expand a 32KB raw save to a 64KB format (alternating 0xFF padding)
    try:
        with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
            data = f_in.read()
            for byte in data:
                # Write the byte and its padding byte in Big Endian order
                f_out.write(bytes([pad_byte, byte]))
        messagebox.showinfo("Success", f"Expanded save written to: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def contract_save(input_file, output_file, pad_byte):
    # Contract a 64KB byte-expanded save to a 32KB
    try:
        with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
            data = f_in.read()
            for i in range(0, len(data), 2):
                if data[i] == pad_byte:
                    f_out.write(bytes([data[i + 1]]))
                else:
                    messagebox.showwarning("Warning", "Unrecognized padding byte encountered.")
                    break
        messagebox.showinfo("Success", f"Contracted save written to: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_input_file():
    # Open file dialog to select input file
    input_file = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    if input_file:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_file)

def select_output_file():
    # Open file dialog to select output file
    output_file = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary Files", '*.bin'), ("MiSTer Save", "*.sav")])
    if output_file:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_file)

def on_convert():
   # Handle the convert button click
    input_file = input_entry.get()
    output_file = output_entry.get()
    pad_byte = 0xFF

    if not os.path.exists(input_file):
        messagebox.showerror("Error", "Input file does not exist.")
        return

    if operation_var.get() == "expand":
        if os.path.getsize(input_file) != 32 * 1024:
            messagebox.showerror("Error", "Input file must be 32KB for expansion.")
            return
        expand_save(input_file, output_file, pad_byte)
    elif operation_var.get() == "contract":
        if os.path.getsize(input_file) != 64 * 1024:
            messagebox.showerror("Error", "Input file must be 64KB for contraction.")
            return
        contract_save(input_file, output_file, pad_byte)
    else:
        messagebox.showerror("Error", "Invalid operation selected.")

# Create the main window
root = tk.Tk()
root.title("Saturn Backup Memory Padder")

# Input file selection
input_label = tk.Label(root, text="Input File:")
input_label.grid(row=0, column=0, padx=10, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=5)
input_button = tk.Button(root, text="Browse", command=select_input_file)
input_button.grid(row=0, column=2, padx=10, pady=5)

# Output file selection
output_label = tk.Label(root, text="Output File:")
output_label.grid(row=1, column=0, padx=10, pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=5)
output_button = tk.Button(root, text="Browse", command=select_output_file)
output_button.grid(row=1, column=2, padx=10, pady=5)

# Operation selection
operation_label = tk.Label(root, text="Operation:")
operation_label.grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar(value="expand")
expand_radio = tk.Radiobutton(root, text="Expand (32KB to 64KB)", variable=operation_var, value="expand")
expand_radio.grid(row=2, column=1, padx=10, pady=5)
contract_radio = tk.Radiobutton(root, text="Contract (64KB to 32KB)", variable=operation_var, value="contract")
contract_radio.grid(row=2, column=2, padx=10, pady=5)

# Convert button
convert_button = tk.Button(root, text="Execute", command=on_convert)
convert_button.grid(row=4, column=0, columnspan=3, pady=20)

# Start the GUI event loop
root.mainloop()
