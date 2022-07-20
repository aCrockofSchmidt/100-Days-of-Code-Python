import tkinter

def button_clicked():
    my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


#Create window

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Create Label

my_label = tkinter.Label(text="I Am A Label", font=("Arial", 24, "bold"))
#my_label["text"] = "New Text"
my_label.config(text="Newer Text")
#my_label.pack(side="left")
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Create Button

button = tkinter.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New \nButton")
new_button.grid(column=2, row=0)

# Create Entry - basically an input

input = tkinter.Entry(width=10)
print(input.get())
#input.pack()
input.grid(column=3, row=2)


window.mainloop()