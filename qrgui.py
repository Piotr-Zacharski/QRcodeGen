from tkinter import *

class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Code Generator")
        self.root.resizable(False,False)

        title=Label(self.root,
                    text="QR Code Generator",
                    font=("aakar, medium", 35),
                    bg='#8e44ad', fg='white').place(x=0,y=0,relwidth=1)

        self.var_name = StringVar()
        self.var_surname = StringVar()
        self.var_email = StringVar()

        # WINDOW

        det_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        det_Frame.place(x=50,y=100,width=500,height=380)
        det_title=Label(det_Frame,
                    text="Wprowadź dane",
                    font=("aakar, medium", 25),
                    bg='#8e44ad', fg='white').place(x=0,y=0,relwidth=1)
        title_Name=Label(det_Frame,
                    text="Imię",
                    font=("aakar, medium", 15, 'bold'),
                    bg='white', fg='black').place(x=20,y=60)
        title_Surname=Label(det_Frame,
                    text="Nazwisko",
                    font=("aakar, medium", 15, 'bold'),
                    bg='white', fg='black').place(x=20,y=100)
        title_Email=Label(det_Frame,
                    text="Email",
                    font=("aakar, medium", 15, 'bold'),
                    bg='white', fg='black').place(x=20,y=140)

        text_Name=Entry(det_Frame,
                    font=("Times New Roman", 15),
                        textvariable=self.var_name,
                    bg='lightyellow', fg='black').place(x=200,y=100)
        text_Surname=Entry(det_Frame,
                    font=("Times New Roman", 15),
                           textvariable=self.var_surname,
                    bg='lightyellow', fg='black').place(x=200,y=140)
        text_Email=Entry(det_Frame,
                    font=("Times New Roman", 15),
                         textvariable=self.var_email,
                    bg='lightyellow', fg='black').place(x=200,y=180)
        btn_generate=Button(det_Frame,
                            text="Wygeneruj kod QR",
                            command=self.generate,
                            font=("Times New Roman", 18, "bold"),
                            bg='#8e44ad',
                            fg='white').place(x=90,y=230, width=300,height=30)
        btn_clear=Button(det_Frame,
                            text="Wyczyść dane",
                            font=("Times New Roman", 18),
                            bg='#8e44ad',
                            fg='white').place(x=90,y=280, width=300,height=30)
        self.msg="Wygenerowano kod QR"
        self.lbl_msg = Label(det_Frame,
                    text=self.msg,
                    font=("Times New Roman", 20, 'bold'),
                    bg='white', fg='green').place(x=0,y=320,relwidth=1)

        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)
        qr_title=Label(qr_Frame,
                    text="Twój kod QR",
                    font=("Times New Roman", 25),
                    bg='#8e44ad', fg='white').place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,text="Brak kodu QR", font=("Times New Roman",15),bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)
    def generate(self):
        if self.var_name.get()=='' or self.var_surname.get()=='' or self.var_email.get()==''
            self.msg="Uzupełnij puste pola!"
            self.lbl_msg.config()
root=Tk()
obj = Qr_Generator(root)
root.mainloop()
