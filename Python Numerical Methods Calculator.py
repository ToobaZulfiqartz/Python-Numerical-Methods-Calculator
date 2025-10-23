from tkinter import Tk, Label, Entry, StringVar, Radiobutton, W, Button, messagebox

window = Tk()
window.title("Physics Equation Solver")
window.geometry("666x366")
window.configure(bg="black")  

Label(window, text="Physics Equation Solver", font=("Arial", 14, "bold"), fg="black", bg="white").grid(row=2, column=1,sticky="w", pady=5)

# --- Choose Method ---
Label(window, text="1. Choose a Method", font=("Arial", 12, "bold"), fg="black", bg="white").grid(row=4, column=1, sticky="w", pady=5)

#Button Method
userchoice = StringVar()

b1 =Button(window, text="1. Bracket Method", command=lambda: userchoice.set("Bracket"))
b1.grid(column=1, row=5, sticky=W, padx=15, pady=5)
b2 =Button(window, text="2. False Method", command=lambda: userchoice.set("False"))
b2.grid(column=1, row=6, sticky=W, padx=15, pady=5)
b3 =Button(window, text="3. Rapphson Newton Method", command=lambda: userchoice.set("Newton"))
b3.grid(column=1, row=7, sticky=W, padx=15, pady=5)
b4 =Button(window, text="4. Secant Method", command=lambda: userchoice.set("Seacant"))
b4.grid(column=1, row=8, sticky=W, padx=15, pady=5)

Label(window, text="2. Choose an Equation and put values", font=("Arial", 12, "bold"), fg="black", bg="white").grid(row=9, column=1, sticky="w", pady=5)
# Radio Buttons
# 1
value_radio = StringVar()
radio_quadratic = Radiobutton(window, text="ax² + bx + c", variable=value_radio, value="Q", command="value")
radio_quadratic.grid(column=0, row=10, sticky=W, padx=15, pady=5)

co_a = Label(window, text="a")
co_a.grid(column=1, row=10, padx=15, pady=5)
a= Entry(window)
a.grid(column=2, row=10, padx=15, pady=5)

co_b = Label(window, text="b")
co_b.grid(column=3, row=10, padx=15, pady=5)
b= Entry(window)
b.grid(column=4, row=10, padx=15, pady=5)

co_c = Label(window, text="c")
co_c.grid(column=5, row=10, padx=15, pady=5)
c= Entry(window)
c.grid(column=6, row=10, padx=15, pady=5)

# 2
radio_cubic = Radiobutton(window, text="ax³ + bx² + cx + d", variable=value_radio, value="C", command="value1")
radio_cubic.grid(column=0, row=11, sticky=W, padx=15, pady=5)

def value1():
    print(" Function is ax³ + bx² + cx + d")

co_a = Label(window, text="a")
co_a.grid(column=1, row=11, padx=15, pady=5)
a= Entry(window)
a.grid(column=2, row=11, padx=15, pady=5)

co_b = Label(window, text="b")
co_b.grid(column=3, row=11, padx=15, pady=5)
b= Entry(window)
b.grid(column=4, row=11, padx=15, pady=5)

co_c = Label(window, text="c")
co_c.grid(column=5, row=11, padx=15, pady=5)
c= Entry(window)
c.grid(column=6, row=11, padx=15, pady=5)

co_d = Label(window, text="d")
co_d.grid(column=7, row=11, padx=15, pady=5)
d= Entry(window)
d.grid(column=8, row=11, padx=15, pady=5)

# 3
radio_quartic = Radiobutton(window, text="ax⁴ + bx³ + cx² + dx + e", variable=value_radio, value="F", command="value2")
radio_quartic.grid(column=0, row=12, sticky=W, padx=15, pady=5)

def value2():
    print("Function is ax⁴ + bx³ + cx² + dx + e")
        
co_a = Label(window, text="a")
co_a.grid(column=1, row=12, padx=15, pady=5)
a= Entry(window)
a.grid(column=2, row=12, padx=15, pady=5)

co_b = Label(window, text="b")
co_b.grid(column=3, row=12, padx=15, pady=5)
b= Entry(window)
b.grid(column=4, row=12, padx=15, pady=5)

co_c = Label(window, text="c")
co_c.grid(column=5, row=12, padx=15, pady=5)
c= Entry(window)
c.grid(column=6, row=12, padx=15, pady=5)

co_d = Label(window, text="d")
co_d.grid(column=7, row=12, padx=15, pady=5)
d= Entry(window)
d.grid(column=8, row=12, padx=15, pady=5)


co_e = Label(window, text="e")
co_e.grid(column=9, row=12, padx=15, pady=5)
e= Entry(window)
e.grid(column=10, row=12, padx=15, pady=5)
    
# Set default value for the radio button
value_radio.set("Q")


# Upper Limit Label and Entry
label_upper_limit = Label(window, text="Upper Limit")
label_upper_limit.grid(column=0, row=14, padx=15, pady=5)
upper_limit_entry = Entry(window)
upper_limit_entry.grid(column=1, row=14, padx=15, pady=5)

# Lower Limit Label and Entry
label_lower_limit = Label(window, text="Lower Limit")
label_lower_limit.grid(column=0, row=15, padx=15, pady=5)
lower_limit_entry = Entry(window)
lower_limit_entry.grid(column=1, row=15, padx=15, pady=5)

# Iterations
iterations = Label(window, text="Iterations")
iterations.grid(column=0, row=16, padx=15, pady=5)
Iterations = Entry(window)
Iterations.grid(column=1, row=16, padx=15, pady=5)

co_xi = Label(window, text="xi")
co_xi.grid(column=0, row=17, padx=15, pady=5)
xi= Entry(window)
xi.grid(column=1, row=17, padx=15, pady=5)

co_xm = Label(window, text="xm")
co_xm.grid(column=0, row=18, padx=15, pady=5)
xm= Entry(window)
xm.grid(column=1, row=18, padx=15, pady=5)

# Submit
b1 =Button(window, text="Submit", bg="black", fg="white", command="result")
b1.grid(column=4, row=22, sticky=W, padx=15, pady=5)

def result():
    method = userchoice.get()
    equation_type = value_radio.get()
    try:
        a = float(a_entry.get())
        b = float(b_entry.get()) if b_entry.get() else 0
        c = float(c_entry.get()) if c_entry.get() else 0
        d = float(d_entry.get()) if equation_type == "C" and d_entry.get() else 0
        xl = float(lower_limit_entry.get())
        xu = float(upper_limit_entry.get())
        iterations = float(iterations_entry.get())
        xi = float(xi_entry.get()) if xi_entry.get() else 0
        xm = float(xm_entry.get()) if xm_entry.get() else 0
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return

    if equation_type == "Q":
        if method == "Bracket":
            for k in range(iterations):
                xr = (xu + xl) / 2
                f_xr = a * xr**2 + b * xr + c
                f_xl = a * xl**2 + b * xl + c
                f_xu = a * xu**2 + b * xu + c

                if f(xl)*f(xr)<0:
                        xu=xr
                else:
                        xl=xr
                print("xr=",xr,"f(xr)=",f(xr))
                print("\n")

            
        elif method == "False":
            for k in range(iterations):
                xr = xu-(f(xu)*(xl-xu)/(f(xl)-f(xu)))
                f_xr = a * xr**2 + b * xr + c
                f_xl = a * xl**2 + b * xl + c
                f_xu = a * xu**2 + b * xu + c

                if f(xl)*f(xr)<0:
                        xu=xr
                else:
                        xl=xr
                print("xr=",xr,"f(xr)=",f(xr))
                print("\n")

        elif method == "Newton":
            for k in range(iterations):
                ai= xi - f(xi)/df(xi)
                f_xi = a * xi**2 + b * xi + c
                f_ai = a * ai**2 + b * ai + c
                df_xi = 2*a * xi + b
                k=1
                if k!=0:
                 print(j+1,"xi+1=",ai,"f(xi+1)=",f(ai))
                 print("\n")
                 xi=ai
                 
    elif equation_type == "C":
        if method == "Bracket":
            for k in range(iterations):
                xr = (xu + xl) / 2
                f_xr = a * xr**3 + b * xr**2 + c * xr +d
                f_xl = a * xl**3 + b * xl**2 + c * xl +d
                f_xu = a * xu**3 + b * xu**2 + c *xu +d

                if f(xl)*f(xr)<0:
                        xu=xr
                else:
                        xl=xr
                print("xr=",xr,"f(xr)=",f(xr))
                print("\n")

            
        elif method == "False":
            for k in range(iterations):
                xr = xu-(f(xu)*(xl-xu)/(f(xl)-f(xu)))
                f_xr = a * xr**3 + b * xr**2 + c * xr + d
                f_xl = a * xl**3 + b * xl**2 + c * xl + d
                f_xu = a * xu**3 + b * xu**2 + c *xu + d

                if f(xl)*f(xr)<0:
                        xu=xr
                else:
                        xl=xr
                print("xr=",xr,"f(xr)=",f(xr))
                print("\n")

        elif method == "Raphson Newton":
            for k in range(iterations):
                ai= xi - f(xi)/df(xi)
                f_xi = a * xi**3 + b * xi**2 + c * xi + d
                f_ai = a * ai**3 + b * ai**2 + c * ai + d
                df_xi = 3*a * xi**2 + 2*b*xi +c
                k=1
                if k!=0:
                 print(j+1,"xi+1=",ai,"f(xi+1)=",f(ai))
                 print("\n")
                 xi=ai

    if equation_type == "F":
        if method == "Bracket":
            for k in range(iterations):
                xr = (xu + xl) / 2
                f_xr = a * xr**4 + b * xr**3 + c *xr**2 + d * xr + e
                f_xl = a * xl**4 + b * xl**3 + c *xl**2 + d * xl + e
                f_xu = aa * xu**4 + b * xu**3 + c *xu**2 + d * xu + e

                if f(xl)*f(xr)<0:
                        xu=xr
                else:
                        xl=xr
                print("xr=",xr,"f(xr)=",f(xr))
                print("\n")

            
        elif method == "False":
            for k in range(iterations):
                xr = xu-(f(xu)*(xl-xu)/(f(xl)-f(xu)))
                f_xr = a * xr**4 + b * xr**3 + c *xr**2 + d * xr + e
                f_xl = a * xl**4 + b * xl**3 + c *xl**2 + d * xl + e
                f_xu = aa * xu**4 + b * xu**3 + c *xu**2 + d * xu + e

                if f(xl)*f(xr)<0:
                        xu=xr
                else:
                        xl=xr
                print("xr=",xr,"f(xr)=",f(xr))
                print("\n")

        elif method == "Raphson Newton":
            for k in range(iterations):
                ai= xi - f(xi)/df(xi)
                f_xi = a * xi**4 + b * xi**3 + c *xi**2 + d * xi + e
                f_ai =  a * ai**4 + b * ai**3 + c *ai**2 + d * ai + e
                df_xi = 4*a * xi**3 + 3*b*xi**2 + 2*c*xi + d
                k=1
                if k!=0:
                 print(j+1,"xi+1=",ai,"f(xi+1)=",f(ai))
                 print("\n")
                 xi=ai


        
# Start the main loop
window.mainloop()
