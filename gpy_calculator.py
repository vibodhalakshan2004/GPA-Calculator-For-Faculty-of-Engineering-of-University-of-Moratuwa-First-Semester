import tkinter as tk
from tkinter import ttk

class SubjectGrade:
    def __init__(self, master, subject_name, options):
        self.selected = tk.StringVar()
        self.selected.set(options[0])  # default value
        
        # Create label
        self.label = ttk.Label(master, text=subject_name)
        self.label.grid(row=self.get_row(master), column=0, padx=5, pady=5)
        
        # Create dropdown
        self.dropdown = ttk.OptionMenu(master, self.selected, options[0], *options)
        self.dropdown.grid(row=self.get_row(master), column=1, padx=5, pady=5)

    def get_row(self, master):
        # Count existing children to place next row
        return len(master.grid_slaves()) // 2
    
    def get_grade(self):
        return self.selected.get()

def calculate_gpa():
    '''Calculate GPA'''
    Total_gpa = 0
    credits = [3, 3, 2, 2, 2, 2]
    for sub, credit in zip(subject_widgets, credits):
        match sub.get_grade():
            case 'A+': gpa = 4
            case 'A': gpa = 4
            case 'A-': gpa = 3.7
            case 'B+': gpa = 3.3
            case 'B': gpa = 3.0
            case 'B-': gpa = 2.7
            case 'C+': gpa = 2.3
            case 'C': gpa = 2.0
            case 'C-': gpa = 1.7
            case 'D': gpa = 1
            case 'F': gpa = 0
        Total_gpa += (gpa * credit) / 14
    label.configure(text=f"GPA: {round(Total_gpa, 2)}")

# Main window
root = tk.Tk()
root.title("GPA Calculator")
root.geometry('250x300')

# ---- ttk Style ----
style = ttk.Style()
style.theme_use("clam")  # Modern flat theme

style.configure("TLabel", font=("Arial", 11), foreground="#222")
style.configure("TButton", font=("Arial", 11, "bold"), foreground="white", background="#007acc", padding=6)
style.map("TButton", background=[("active", "#005999")])

# Options for grades
options = ['A+','A','A-','B+','B','B-','C+','C','C-','D','F']

# Create subjects
subjects = ['MA1014','CS1033','EE1014','CE1023','ME1033','MT1023']
subject_widgets = []

for subj in subjects:
    subject_widgets.append(SubjectGrade(root, subj, options))

# Create a Button
button = ttk.Button(text='Calculate GPA', command=calculate_gpa)
button.grid(row=6, column=0, pady=10)

# Create a Label
label = ttk.Label(text="GPA: --")
label.grid(row=6, column=1)

root.mainloop()
