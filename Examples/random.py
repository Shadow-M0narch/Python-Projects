from tkinter import *
from tokenize import String

class MyApp:
    def __init__(self, root):
        root.title("Fibonacci")
        root.iconbitmap('./assets/monokuma.ico')

        menu = Menu(root)
        item = Menu(menu)

        def close():
            root.destroy()
            root.quit()

        item.add_command(label='Exit', command=close)
        menu.add_cascade(label='File', menu=item)

        root.config(menu=menu)

        window_width = 300
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        label1 = Label(root, text="Your Input:")
        label1.pack()

        # Dictionary Method
        # label["text"] = "Hello Everyone."
        # label ["font"] = ("Courier", 20)

        #Configure Method
        # label.configure(text="Hello Everyone.", font=("Courier", 20))

        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text)
        self.label_text = StringVar()
        label2 = Label(root, textvariable=self.label_text)

        label2.pack()
        entry.pack()

        
        button = Button(root, text="Submit", command=self.press_button)
        button.pack()


    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)
        

root = Tk()

MyApp(root)

root.mainloop()

