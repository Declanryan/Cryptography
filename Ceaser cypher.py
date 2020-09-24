from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import font


class MyGUI:

    def __init__(self, my_parent):
        self.encrypted_str = ""
        self.decrypted_str = ""
        self.parent = my_parent
        self.parent.title("     SECRET MESSAGE")

        # Make protocol handler to manage interaction between the application and the window handler
        self.parent.protocol("WM_DELETE_WINDOW", self.catch_destroy)

        # Set up fonts for text area
        arial_bold = font.Font(family="Arial", size=14, weight=font.BOLD)
        arial_normal = font.Font(family="Arial", size=14, weight=font.NORMAL)

        self.menubar = Menu(self.parent)

        # create a pulldown menu, and add it to the menu bar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.open)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # create more pulldown menus
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        self.editmenu.add_command(label="Paste", command=self.paste)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.parent.config(menu=self.menubar)

        # sets out the layout for the holding frames
        self.main_frame = Frame(my_parent)
        self.main_frame.grid(row=0, column=0)  # holding frame
        self.frame0 = Frame(self.main_frame, padx=5, pady=5, border=1)
        self.frame0.grid(row=0, column=0)  # input frame
        self.frame1 = Frame(self.main_frame, padx=5, pady=5, border=1)
        self.frame1.grid(row=1, column=0)  # text frame
        self.frame2 = Frame(self.main_frame, padx=5, pady=5, border=1)
        self.frame2.grid(row=2, column=0)  # bottom holding frame
        self.frame20 = Frame(self.frame2, padx=10, pady=10)
        self.frame20.grid(row=0, column=0)  # set frame
        self.frame21 = Frame(self.frame2, padx=10, pady=10)
        self.frame21.grid(row=0, column=1)  # encrypt frame
        self.frame22 = Frame(self.frame2, padx=10, pady=10)
        self.frame22.grid(row=0, column=2)  # decrypt frame
        self.frame23 = Frame(self.frame2, padx=10, pady=10)
        self.frame23.grid(row=0, column=3)  # clear frame

        #  sets out the textbox for input
        self.input_text = StringVar()
        self.key_text = StringVar()
        self.input_text.set("please enter the text to convert ")
        self.key_text.set("10")
        self.encrypt_label = Label(self.frame0, padx=5, pady=5, text="ENCRYPT")
        self.encrypt_label.grid(row=0, column=0)
        self.text_box = Entry(self.frame0, width=40, textvariable=self.input_text)
        self.text_box.grid(row=0, column=1)
        self.key_label = Label(self.frame0, padx=5, pady=5, text="Key")
        self.key_label.grid(row=0, column=2)
        self.key_box = Entry(self.frame0, width=5, textvariable=self.key_text)
        self.key_box.grid(row=0, column=3)
        self.text_box.focus_set()

        #  configure the text area
        self.textwin = scrolledtext.ScrolledText(self.frame1, background="lightgrey", wrap=WORD, height=15, width=50,)
        self.textwin.tag_configure("rj", justify=LEFT)
        self.textwin.tag_configure("ab", font=arial_bold)
        self.textwin.tag_configure("an", font=arial_normal)
        self.textwin.grid(row=0, column=0)

        # Buttons ARE PLACED IN BOTTOM FRAME
        self.btn_set = Button(self.frame20, bg="black", fg="white", text="SET", command=lambda: self.set())\
            .grid(row=0, column=0)
        self.btn_encrypt = Button(self.frame21, bg="black", fg="white", text="ENCRYPT", command=lambda: self.encrypt())\
            .grid(row=0, column=1)
        self.btn_decrypt = Button(self.frame22, bg="black", fg="white", text="DECRYPT", command=lambda: self.decrypt())\
            .grid(row=0, column=2)
        self.btn_clear = Button(self.frame23, bg="black", fg="white", text="CLEAR", command=lambda: self.clear())\
            .grid(row=0, column=3)

    def set(self):
        self.encrypted_str = self.text_box.get()

    def clear(self):
        self.textwin.delete(1.0, END,)
        self.encrypted_str = ""
        self.decrypted_str = ""
        self.text_box.delete(0, 'end')

    def encrypt(self):
        key = int(self.key_box.get())
        for i in self.text_box.get():
            i = ord(i)
            i = i + key
            i = chr(i)
            self.encrypted_str += i
        self.textwin.insert("1.50", " ")
        self.textwin.insert("1.0", "{}\n".format(self.encrypted_str), "rj ab")

    def decrypt(self):
        key = int(self.key_box.get())
        for i in self.encrypted_str:
            i = ord(i)
            i = i - key
            i = chr(i)
            self.decrypted_str += i
        self.textwin.insert("1.50", " ")
        self.textwin.insert("1.0", "{}\n".format(self.decrypted_str), "rj ab")

    def open(self):
        print("hello!")

    def save(self):
        print("hello!")

    def cut(self):
        print("hello!")

    def copy(self):
        print("hello!")

    def paste(self):
        print("hello!")

    def about(self):
        print("hello!")

#  display message if quit button is pressed
    def catch_destroy(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.parent.destroy()


def main():
    root = Tk()
    MyGUI(root)
    # Keep listening for events until destroy event occurs.
    root.mainloop()


if __name__ == "__main__":
    main()