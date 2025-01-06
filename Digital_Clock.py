
import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Clock")
        self.root.geometry("400x200")
        self.root.configure(bg='black')
        
        # Create labels for time and date
        self.time_label = tk.Label(
            self.root,
            font=('calibri', 40, 'bold'),
            background='black',
            foreground='cyan'
        )
        self.time_label.pack(anchor='center', pady=20)
        
        self.date_label = tk.Label(
            self.root,
            font=('calibri', 20),
            background='black',
            foreground='cyan'
        )
        self.date_label.pack(anchor='center')
        
        self.update_clock()
        
    def update_clock(self):
        # Update time
        time_string = strftime('%H:%M:%S')
        self.time_label.config(text=time_string)
        
        # Update date
        date_string = strftime('%B %d, %Y')
        self.date_label.config(text=date_string)
        
        # Schedule next update
        self.root.after(1000, self.update_clock)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    clock = DigitalClock()
    clock.run()






















# import tkinter as tk
# from tkinter import Label
# import time

# def update_time():
#     current_time = time.strftime('%Y-%m-%d %H:%M:%S')
#     clock_label.config(text=current_time)
#     clock_label.after(1000, update_time)

# root = tk.Tk()
# root.title("Digital Clock")

# clock_label = Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
# clock_label.pack(anchor='center')

# update_time()
# root.mainloop()
