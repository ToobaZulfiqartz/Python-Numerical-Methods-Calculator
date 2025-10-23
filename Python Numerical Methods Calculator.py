from tkinter import Tk, Label, Entry, StringVar, Radiobutton, Button, W, messagebox
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

window = Tk()
window.title("Computational Physics Calculator")
window.geometry("1000x556")
window.configure(bg="#E7D6B5")  

cal = Button(window, text="Computational Physics Numerical Method Equation Calculator", bg="#C1A47A", fg="Black")
cal.grid(column=2, row=0, padx=15, pady=5)

gap = Label(window, text="  ", bg="#E7D6B5")
gap.grid(column=0, row=1, padx=15, pady=5)

# Combobox
selected_option = StringVar()

selection = Button(window, text="Select_Method", fg="black", bg="#D4BFA3")
selection.grid(column=0, row=1, padx=15, pady=5)

def on_combobox_select(event):
    selected_option.set(combo.get()) 

selected_option = StringVar()
combo = ttk.Combobox(window, values=["Bracket Method", "False Method", "Raphson Newton Method", "Secant Method"])
combo.grid(column=0, row=2, padx=15, pady=5)
combo.bind("<<ComboboxSelected>>", on_combobox_select)

gap2 = Label(window, text="  ", bg="#E7D6B5")
gap2.grid(column=0, row=3, padx=15, pady=5)
gap3 = Label(window, text="  ", bg="#E7D6B5")
gap3.grid(column=0, row=4, padx=15, pady=5)

# Radio Buttons
choice = Button(window, text="Select_Function", fg="black", bg="#D4BFA3")
choice.grid(column=0, row=5, padx=15, pady=5)

# 1
value_radio = StringVar()
radio_quadratic = Radiobutton(window, text="ax² + bx + c", variable=value_radio, value="Q", fg="black", bg="#C1A47A")
radio_quadratic.grid(column=0, row=6, sticky=W, padx=15, pady=5)

radio_cubic = Radiobutton(window, text="ax³ + bx² + cx + d", variable=value_radio, value="C", fg="black", bg="#C1A47A")
radio_cubic.grid(column=0, row=7, sticky=W, padx=15, pady=5)

radio_quartic = Radiobutton(window, text="ax⁴ + bx³ + cx² + dx + e", variable=value_radio, value="F", fg="black", bg="#C1A47A")
radio_quartic.grid(column=0, row=8, sticky=W, padx=15, pady=5)

co_a = Label(window, text="a", fg="black", bg="white")
co_a.grid(column=1, row=6, padx=15, pady=5)
a= Entry(window)
a.grid(column=2, row=6, padx=15, pady=5)

co_b = Label(window, text="b",fg="black", bg="white")
co_b.grid(column=3, row=6, padx=15, pady=5)
b= Entry(window)
b.grid(column=4, row=6, padx=15, pady=5)

co_c = Label(window, text="c", fg="black", bg="white")
co_c.grid(column=5, row=6, padx=15, pady=5)
c= Entry(window)
c.grid(column=6, row=6, padx=15, pady=5)

co_d = Label(window, text="d", fg="black", bg="white")
co_d.grid(column=1, row=7, padx=15, pady=5)
d= Entry(window)
d.grid(column=2, row=7, padx=15, pady=5)


co_e = Label(window, text="e",fg="black", bg="white")
co_e.grid(column=3, row=7, padx=15, pady=5)
e= Entry(window)
e.grid(column=4, row=7, padx=15, pady=5)
    
# Set default value for the radio button
value_radio.set("Q")

gap3 = Label(window, text="  ", bg="#E7D6B5")
gap3.grid(column=0, row=9, padx=15, pady=5)

# Inputs
label_upper_limit = Label(window, text="Upper Limit", fg="black", bg="white")
label_upper_limit.grid(column=0, row=10, padx=15, pady=5)
upper_limit_entry = Entry(window)
upper_limit_entry.grid(column=1, row=10, padx=15, pady=5)


label_lower_limit = Label(window, text="Lower Limit", fg="black", bg="white")
label_lower_limit.grid(column=0, row=11, padx=15, pady=5)
lower_limit_entry = Entry(window)
lower_limit_entry.grid(column=1, row=11, padx=15, pady=5)

iterations = Label(window, text="Iterations", fg="black", bg="white")
iterations.grid(column=0, row=12, padx=15, pady=5)
Iterations = Entry(window)
Iterations.grid(column=1, row=12, padx=15, pady=5)

co_xi = Label(window, text="xi", fg="black", bg="white")
co_xi.grid(column=0, row=13, padx=15, pady=5)
xi= Entry(window)
xi.grid(column=1, row=13, padx=15, pady=5)

co_xm = Label(window, text="xm", fg="black", bg="white")
co_xm.grid(column=0, row=14, padx=15, pady=5)
xm= Entry(window)
xm.grid(column=1, row=14, padx=15, pady=5)
co_1 = Label(window, text="xi-1", fg="black", bg="white")
co_1.grid(column=0, row=14, padx=15, pady=5)

# Result
def result():
    method = selected_option.get()
    equation_type = value_radio.get()

    try:
        a_val = float(a.get())
        b_val = float(b.get()) if b.get() else 0
        c_val = float(c.get()) if c.get() else 0
        d_val = float(d.get()) if d.get() else 0
        e_val = float(e.get()) if e.get() else 0
        xl = float(lower_limit_entry.get()) if lower_limit_entry.get() else 0
        xu = float(upper_limit_entry.get()) if upper_limit_entry.get() else 0
        i = int(Iterations.get())
        xi_val = float(xi.get()) if xi.get() else 0
        xm_val = float(xm.get()) if xm.get() else 0
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return

    def f(x):
        if equation_type == "Q":  
            return a_val * x**2 + b_val * x + c_val
        elif equation_type == "C":  
            return a_val * x**3 + b_val * x**2 + c_val * x + d_val
        elif equation_type == "F":  
            return a_val * x**4 + b_val * x**3 + c_val * x**2 + d_val * x + e_val

    def df(x):
        if equation_type == "Q":  
            return a_val * 2 * x + b_val
        elif equation_type == "C":  
            return a_val * 3 * x**2 + b_val * 2 * x + c_val
        elif equation_type == "F":  
            return a_val * 4 * x**3 + b_val * 3 * x**2 + c_val * 2 * x + d_val
    
    x_values = np.linspace(-10,10)
    y_values = [f(x) for x in x_values] 

    if method == "Bracket Method":
        for k in range(i):
            xr = (xu + xl) / 2
            if f(xl) * f(xr) < 0:
                xu = xr
            else:
                xl = xr
            print(k+1,"xr=", xr, "f(xr)=", f(xr))
            print("\n")
        plt.plot(x_values,y_values, label='x vs f(x)', color='Brown')
        plt.plot(xr,f(xr),marker="o",label='xr', color='Black')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid()
        plt.title('Bracket Method')
        plt.show()

        
    elif method == "False Method":
        for k in range(i):
            xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
            if f(xl) * f(xr) < 0:
                xu = xr
            else:
                xl = xr
            print(k+1,"xr=", xr, "f(xr)=", f(xr))
            print("\n")
        plt.plot(x_values,y_values, label='x vs f(x)', color='Brown')
        plt.plot(xr,f(xr),marker="o",label='xr', color='Black')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid()
        plt.title('False Method')
        plt.show()

        
    elif method == "Raphson Newton Method":
        j=1
        for k in range(i):
            xi_plus_one = xi_val - f(xi_val) / df(xi_val)
            if j!=0:
             print(k + 1, "xi+1=", xi_plus_one, "f(xi+1)=", f(xi_plus_one))
             print("\n")
            xi_val = xi_plus_one
        plt.plot(x_values,y_values, label='x vs f(x)', color='Brown')
        plt.plot(xi_plus_one,f(xi_plus_one),marker="o",label='xi+1', color='Black')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid()
        plt.title('Newton Method')
        plt.show()
   
        
    elif method == "Secant Method":
        j=1
        for k in range(i):
            xi_plus_one = xi_val - (f(xi_val) * (xm_val - xi_val) / (f(xm_val) - f(xi_val)))
            xm_val = xi_val
            if j!=0:
             print(k + 1, "xi+1=", xi_plus_one, "f(xi+1)=", f(xi_plus_one))
             print("\n")
            xi_val = xi_plus_one
        plt.plot(x_values,y_values, label='xr vs f(xr)', color='Brown')
        plt.plot(xi_plus_one,f(xi_plus_one),marker="o",label='xi+1', color='Black')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid()
        plt.title('Secant Method')
        plt.show()


# Submit
            
b1=Button(window, text="Submit", fg="black", bg="#C1A47A", command=result)
b1.grid(column=3, row=15, sticky=W, padx=15, pady=5)

window.mainloop()


