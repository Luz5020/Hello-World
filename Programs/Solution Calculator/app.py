#  Copyright (c) 2022. luz5020
#  Approved for use in Open Source Projects
#  GNU General Public License v3.0
#  https://www.gnu.org/licenses/gpl-3.0.en.html
import tkinter as tk


# Methods
def Calculate():
    try:
        a = float(ent_input_a.get())
        b = float(ent_input_b.get())
        c = float(ent_input_c.get())
        if ((b ** 2 - (4 * a * c)) > 0) and ((2 * a) != 0):
            print("Solvable")
            x1 = (-b + (b ** 2 - (4 * a * c)) ** (1 / 2)) / (2 * a)
            x2 = (-b - (b ** 2 - (4 * a * c)) ** (1 / 2)) / (2 * a)
            lbl_output_1["text"] = x1
            lbl_output_2["text"] = x2
        else:
            print("Not Solvable")
            lbl_output_1["text"] = "Not Solvable"
            lbl_output_2["text"] = "Not Solvable"
    except ValueError:
        print("Not Solvable")
        lbl_output_1["text"] = "Value Error"
        lbl_output_2["text"] = "Value Error"

    # Graphical Initialization


# General
window = tk.Tk()
window.title("Solution Calculator")
frm_exp = tk.Frame(master=window)
frm_input = tk.Frame(master=window)
frm_btn = tk.Frame(master=window)
frm_output = tk.Frame(master=window)
for i in range(4):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)
lbl_exp = tk.Label(master=frm_exp, text="Enter a b c")
ent_input_a = tk.Entry(master=frm_input)
ent_input_b = tk.Entry(master=frm_input)
ent_input_c = tk.Entry(master=frm_input)
lbl_a = tk.Label(master=frm_input, text="a")
lbl_b = tk.Label(master=frm_input, text="b")
lbl_c = tk.Label(master=frm_input, text="c")
lbl_output_1 = tk.Label(master=frm_output, text="X1 Result will appear here")
lbl_output_2 = tk.Label(master=frm_output, text="X2 Result will appear here")
btn_btn = tk.Button(master=frm_btn, text="Calculate", command=Calculate)
# Placement
frm_exp.grid(row=0, column=0, sticky="sw")
lbl_exp.grid(row=0, column=0, sticky="sw")
frm_input.grid(row=1, column=0, padx=5)
frm_btn.grid(row=1, column=1, padx=5)
frm_output.grid(row=1, column=2, padx=5)
ent_input_a.grid(row=1, column=1)
lbl_a.grid(row=1, column=0)
ent_input_b.grid(row=1, column=3)
lbl_b.grid(row=1, column=2)
ent_input_c.grid(row=1, column=5)
lbl_c.grid(row=1, column=4)
lbl_output_1.grid(row=1, column=1)
lbl_output_2.grid(row=1, column=3)
btn_btn.grid(row=1, column=2)
# Draw
window.mainloop()
