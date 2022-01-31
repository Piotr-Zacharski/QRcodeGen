from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Code Generator")
        self.root.resizable(False,False)

        title=Label(self.root,
                    text="Generator kodów QR sieci WiFi",
                    font=("aakar, medium", 35),
                    bg='#8e44ad', fg='white').place(x=0,y=0,relwidth=1)

        self.var_name = StringVar()
        self.var_surname = StringVar()

        # WINDOW

        det_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        det_Frame.place(x=50,y=100,width=500,height=380)
        det_title=Label(det_Frame,
                    text="Wprowadź dane sieci WiFi",
                    font=("aakar, medium", 25),
                    bg='#8e44ad', fg='white').place(x=0,y=0,relwidth=1)
        title_Name=Label(det_Frame,
                    text="SSID",
                    font=("aakar, medium", 15, 'bold'),
                    bg='white', fg='black').place(x=20,y=60)
        title_Surname=Label(det_Frame,
                    text="Hasło",
                    font=("aakar, medium", 15, 'bold'),
                    bg='white', fg='black').place(x=20,y=100)


        text_Name=Entry(det_Frame,
                    font=("Times New Roman", 15),
                        textvariable=self.var_name,
                    bg='lightyellow', fg='black').place(x=200,y=60)
        text_Surname=Entry(det_Frame,
                    font=("Times New Roman", 15),
                           textvariable=self.var_surname,
                    bg='lightyellow', fg='black').place(x=200,y=100)

        btn_generate=Button(det_Frame,
                            text="Wygeneruj kod QR",
                            command=self.generate,
                            font=("Times New Roman", 18, "bold"),
                            bg='#8e44ad',
                            fg='white').place(x=90,y=230, width=300,height=30)
        btn_clear=Button(det_Frame,
                            text="Wyczyść dane",
                            command=self.clear,
                            font=("Times New Roman", 18),
                            bg='#8e44ad',
                            fg='white').place(x=90,y=280, width=300,height=30)
        self.msg=""
        self.lbl_msg = Label(det_Frame,
                    text=self.msg,
                    font=("Times New Roman", 20, 'bold'),
                    bg='white', fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)

        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=590,y=100,width=300,height=380)
        qr_title=Label(qr_Frame,
                    text="Kod QR sieci WiFi",
                    font=("Times New Roman", 25),
                    bg='#8e44ad', fg='white').place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,text="Brak kodu QR", font=("Times New Roman",15),bd=1,relief=RIDGE)
        self.qr_code.place(x=55,y=100,width=180,height=180)
    def clear(self):
        self.var_name.set('')
        self.var_surname.set('')
        self.msg=""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
    def generate(self):
        if self.var_name.get()==''or self.var_surname.get()=='':
            self.msg="Uzupełnij puste pola!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Imię: {self.var_name.get()}\nNazwisko: {self.var_surname.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code, [180,180])
            qr_code.save("Codes/code"+str(self.var_name.get())+'.png')
            self.im=ImageTk.PhotoImage(file="Codes/code"+str(self.var_name.get())+'.png')
            self.qr_code.config(image=self.im)
            self.msg="Wygenerowano kod QR"
            self.lbl_msg.config(text=self.msg,fg='green')
root=Tk()
obj = Qr_Generator(root)
root.mainloop()
