from tkinter import *
from tkinter import messagebox
from hotel import HotelManagementSystem


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management Login")
        self.root.geometry("500x350+500+200")
        self.root.resizable(False, False)

        title = Label(
            self.root,
            text="HOTEL MANAGEMENT LOGIN",
            font=("Arial", 18, "bold"),
            bg="black",
            fg="gold"
        )
        title.pack(fill=X)

        Frame(self.root, height=20).pack()

        Label(
            self.root,
            text="Username",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        self.user = Entry(self.root, font=("Arial", 12))
        self.user.pack(ipady=5, ipadx=20)

        Label(
            self.root,
            text="Password",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        self.password = Entry(
            self.root,
            show="*",
            font=("Arial", 12)
        )
        self.password.pack(ipady=5, ipadx=20)

        Button(
            self.root,
            text="LOGIN",
            command=self.login,
            font=("Arial", 12, "bold"),
            bg="green",
            fg="white",
            width=15
        ).pack(pady=20)

        Button(
            self.root,
            text="EXIT",
            command=self.root.destroy,
            font=("Arial", 12, "bold"),
            bg="red",
            fg="white",
            width=15
        ).pack()

    def login(self):
        username = self.user.get()
        password = self.password.get()

        if username == "admin" and password == "admin123":

            self.root.destroy()

            main_root = Tk()
            obj = HotelManagementSystem(main_root)
            main_root.mainloop()

        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()