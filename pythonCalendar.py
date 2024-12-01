from tkinter import *
import calendar

def Calendar_See():
    window = Tk()



if __name__ == "__main__":
    root = Tk()
    root.config(background="yellow")
    root.title("GUI Calendar")
    root.geometry("280x170")

    name = Label(root, text="Calendar", bg="light pink", font=("Arial",20,"bold"))
    name.grid(row=1,column=1)

    year = Label(root, text="Enter the year",bg="Light blue",font=("Arial", 15,"bold"))
    year.grid(row=2,column=1)
    

    year_entry = Entry(root, font=("Arial", 15,"bold"))
    year_entry.grid(row=3,column=1)

    show_button=Button(root, text="Show Calendar!",fg="red",bg="black",
                       font=("Arial", 15,"bold"), command=Calendar_See)
    show_button.grid(row=4,column=1)




    root.mainloop()