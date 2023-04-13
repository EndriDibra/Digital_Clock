# Author: Endri Dibra

# importing the required libraries

# time library
from time import strftime

# tkinter library
from tkinter import *
from tkinter.ttk import *

# creating frame to store digital clock
root = Tk()
root.title('Digital Digital_Clock')


# taking and displaying time on the label
def get_time():

    # storing the content of digital clock
    # : hours, minutes, seconds, am/pm, day
    string = strftime('%H:%M:%S %p %a')

    label.config(text=string)
    label.after(1000, get_time)


# creating the design for digital clock
label = Label(root, font=('ds-digital', 50), background='blue', foreground='white')

# positioning digital clock
# in the center of the (tkinter frame)
label.pack(anchor='center')

# running get_time() function
get_time()

# running mainloop() function
mainloop()
