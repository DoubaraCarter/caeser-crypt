import tkinter as tk
from tkinter import messagebox
from utils.cipher import caesar_cipher_encode, caesar_cipher_decode

def encode():
    try:
        shift = int(shift_entry.get())
        text = text_entry.get("1.0", tk.END).strip()
        encoded_text = caesar_cipher_encode(text, shift)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, encoded_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the shift.")

def decode():
    try:
        shift = int(shift_entry.get())
        text = text_entry.get("1.0", tk.END).strip()
        decoded_text = caesar_cipher_decode(text, shift)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, decoded_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the shift.")

# Create main window
root = tk.Tk()
root.title("Caesar Cipher Encoder/Decoder")

# Create frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create labels
text_label = tk.Label(frame, text="Enter Text:")
text_label.grid(row=0, column=0, sticky="w")

shift_label = tk.Label(frame, text="Shift:")
shift_label.grid(row=1, column=0, sticky="w")

result_label = tk.Label(frame, text="Result:")
result_label.grid(row=3, column=0, sticky="w")

# Create entry fields
text_entry = tk.Text(frame, height=5, width=40)
text_entry.grid(row=0, column=1, columnspan=2, padx=5)

shift_entry = tk.Entry(frame, width=10)
shift_entry.grid(row=1, column=1, padx=5)

result_entry = tk.Text(frame, height=5, width=40)
result_entry.grid(row=3, column=1, columnspan=2, padx=5)

# Create buttons
encode_button = tk.Button(frame, text="Encode", command=encode)
encode_button.grid(row=2, column=1, pady=5)

decode_button = tk.Button(frame, text="Decode", command=decode)
decode_button.grid(row=2, column=2, pady=5)

# Run the application
root.mainloop()
