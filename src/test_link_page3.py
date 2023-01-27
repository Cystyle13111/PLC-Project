import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from pymodbus.client import ModbusTcpClient as mbclient

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        #resize image
        tk.Frame.__init__(self, parent)
        self.configure(bg="#fff")
        logo_dn = Image.open("D:\doanPLC\BARCODE\screen\Login2.png")
        resized_logo_dn = logo_dn.resize((400,400),Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(resized_logo_dn)
        label = tk.Label(self, image=photo1,bg="white")
        label.image=photo1
        label.place(x = 150, y = 130)
        logo_spkt = Image.open("D:\doanPLC\BARCODE\screen\Hcmute.png")
        resized_logo_spkt = logo_spkt.resize((100,100),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_logo_spkt)
        label = tk.Label(self, image=photo,bg="white")
        label.image=photo
        label.place(x=10,y=5)
        logo_khoa = Image.open("D:\doanPLC\BARCODE\screen\logo_feee.png")
        resized_logo_khoa = logo_khoa.resize((100,100),Image.ANTIALIAS)
        logo_khoa = ImageTk.PhotoImage(resized_logo_khoa)
        label = tk.Label(self, image= logo_khoa,bg="white")
        label.image= logo_khoa
        label.place(x = 140, y = 5)
        
        #border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        #border.pack(fill="both", expand="yes", padx = 70, pady=70)
        
        #L1 = tk.Label(self, text="Username", font=("Arial Bold", 15), bg='ivory')
        #L1.place(x=500, y=200)
        #T1 = tk.Entry(self, width = 30, bd = 5)
        #T1.place(x=600, y=200)
        
        #L2 = tk.Label(self, text="Password", font=("Arial Bold", 15), bg='ivory')
        #L2.place(x=50, y=80)
        #T2 = tk.Entry(self, width = 30, show='*', bd = 5)
        #T2.place(x=180, y=80)
        frame=tk.Frame(self,width=350,height=350,bg="white")
        frame.place(x=600,y=150)

        heading=tk.Label(frame,text='Sign in', fg='#57a1f8',bg='white',
                        font=('Microsoft YaHei UI Light',25,'bold'))
        heading.place(x=120,y=65)

        ######################---------------------------------------
        #ẩn/hiện Username khi tiến hành nhập
        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')

        #Nhập Username
        user = tk.Entry(frame,width=25,fg='black',border=0,bg='white',
                        font=('Microsoft YaHei UI Light',11))
        user.place(x=30,y=130)
        user.insert(0,'Username')
        user.bind('<FocusIn>',on_enter)
        user.bind('<FocusOut>', on_leave)

        tk.Frame(frame,width=295,height=2,bg='black').place(x=25,y=160)

        ######################---------------------------------------
        #ẩn/hiện Password khi tiến hành nhập
        def on_enter(e):
            code.delete(0, 'end')

        def on_leave(e):
            name=code.get()
            if name=='':
                code.insert(0,'Password')

        #Nhập Password
        code = tk.Entry(frame,width=25,fg='black',border=0,bg='white',
                        font=('Microsoft YaHei UI Light',11), show='*')
        code.place(x=30,y=200)
        code.insert(0,'Password')
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)

        tk.Frame(frame,width=295,height=2,bg='black').place(x=25,y=230)
        def verify():
            try:
                if user.get() == "user" and code.get() == "user" :
                    controller.show_frame(SecondPage)    
                else:
                    messagebox.showinfo("Error","Vui long nhap dung mat khau")
            except:
                print("error")
        B1 = tk.Button(self, width=40,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0, command=verify)
        B1.place(x=635,y=400)

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        width = 500
        height = 350
        dim = (width,height)
        #background
        background = Image.open(r'D:\doanPLC\BARCODE\screen\main.jpg')
        resized = background.resize((1180, 708), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(resized)
        label = tk.Label(self, image=photo1,bg="white")
        label.image=photo1
        label.place(x = 0, y = 0)
        logo_spkt = Image.open(r'D:\doanPLC\BARCODE\screen\Hcmute.png')
        resized_logo_spkt = logo_spkt.resize((100,100),Image.ANTIALIAS)
        logo_spkt = ImageTk.PhotoImage(resized_logo_spkt)
        logo_spkt_label = tk.Label(self, image= logo_spkt, bg = "white")
        logo_spkt_label.image = logo_spkt
        logo_spkt_label.place(x = 600, y = 5)
        logo_khoa = Image.open(r'D:\doanPLC\BARCODE\screen\logo_feee.png')
        resized_logo_khoa = logo_khoa.resize((100,100),Image.ANTIALIAS)
        logo_khoa = ImageTk.PhotoImage(resized_logo_khoa)
        logo_khoa_label = tk.Label(self, image= logo_khoa, bg = "white")
        logo_khoa_label.image = logo_khoa
        logo_khoa_label.place(x = 1070, y = 5)
        hthi_truong = tk.Label(self,text='ĐẠI HỌC SƯ PHẠM KỸ THUẬT TP.HCM',font = ('Helvetica', 13, 'bold'), bg= "white")
        hthi_truong.place(x = 740, y = 15)
        hthi_khoa = tk.Label(self,text='KHOA ĐIỆN - ĐIỆN TỬ',font = ('Helvetica', 13, 'bold'), bg= "white")
        hthi_khoa.place(x = 790, y = 40)
        hthi_bomon = tk.Label(self,text='BỘ MÔN ĐIỀU KHIỂN TỰ ĐỘNG',font = ('Helvetica', 13, 'bold'), bg= "white")
        hthi_bomon.place(x = 760, y = 65)
        hthi_sv = tk.Label(self,text='SVTH :',font = ('Helvetica', 15, 'bold'), bg= "white")
        hthi_sv.place(x = 630, y = 150)
        hthi_hoten1 = tk.Label(self,text='TẠ TRẦN NHẬT MINH',font = ('Helvetica', 15, 'bold'), bg= "white")
        hthi_hoten1.place(x = 700, y = 150)
        hthi_mssv1 = tk.Label(self,text='MSSV : 19151034',font = ('Helvetica', 15, 'bold'), bg= "white")
        hthi_mssv1.place(x = 940, y = 150)
        hthi_hoten2 = tk.Label(self,text='NGUYỄN ĐỨC MẠNH',font = ('Helvetica', 15, 'bold'), bg= "white")
        hthi_hoten2.place(x = 702, y = 180)
        hthi_mssv1 = tk.Label(self,text='MSSV : 19151253',font = ('Helvetica', 15, 'bold'), bg= "white")
        hthi_mssv1.place(x = 940, y = 180)
        hthi_gv = tk.Label(self,text='GVHD :',font = ('Helvetica', 15, 'bold'), bg= "white")
        hthi_gv.place(x = 630, y = 220)
        hthi_hoten3 = tk.Label(self,text='NGUYỄN THỊ YẾN TUYẾT',font = ('Helvetica', 15, 'bold'), bg= "white")
        hthi_hoten3.place(x = 702, y = 220)

        hthi_doan = tk.Label(self,text='ĐỒ ÁN ĐIỀU KHIỂN LẬP TRÌNH',font = ('Helvetica', 18, 'bold'), bg= "black",fg= "white")
        hthi_doan.place(x = 110, y = 20)
        hthi_tendoan1 = tk.Label(self,text='PHÂN LOẠI SẢN PHẨM THEO MÀU SẮC',font = ('Helvetica', 20, 'bold'), bg= "black",fg= "yellow")
        hthi_tendoan1.place(x = 20, y = 50)
        hthi_tendoan2 = tk.Label(self,text='SỬ DỤNG PLC S7-1200',font = ('Helvetica', 20, 'bold'), bg= "black",fg= "yellow")
        hthi_tendoan2.place(x = 100, y = 80)
        
        #Bảng dem san pham
        #bordercolor=tk.Frame(self,highlightbackground="black",highlightthickness=2,width=500,height=100,bg="white")   
        #bordercolor.place(x=640, y=370)
        #hthi_dem = tk.Label(self,text='GIÁM SÁT SẢN PHẨM',font = ('Helvetica', 20, 'bold'), bg= "white")
        #hthi_dem.place(x = 735, y = 350)
        #hthi_dem_vang = tk.Label(self,text='SẢN PHẨM MÀU',font = ('Helvetica', 18, 'bold'), bg= "white", fg = "red")
        #hthi_dem_vang.place(x = 670, y = 400)
        #dem_vang = tk.Entry(self, width=12,fg='red',border=2,bg='white',font=('Helvetica', 18, 'bold'), state='readonly')
        #dem_vang.place(x = 980, y = 250) 
        #hthi_dem_tim = tk.Label(self,text='SẢN PHẨM TÍM',font = ('Helvetica', 18, 'bold'), bg= "white", fg = "red")
        #hthi_dem_tim.place(x = 670, y = 320)
        #dem_hong = tk.Entry(self, width=5,fg='red',border=2,bg='white',font=('Helvetica', 18, 'bold'), state='readonly')
        #dem_hong.place(x = 1000, y = 320) 
        #hthi_dem_xanh = tk.Label(self,text='SẢN PHẨM XANH',font = ('Helvetica', 18, 'bold'), bg= "white", fg = "red")
        #hthi_dem_xanh.place(x = 670, y = 390)
        #dem_xanh = tk.Entry(self, width=5,fg='red',border=2,bg='white',font=('Helvetica', 18, 'bold'), state='readonly')
        #dem_xanh.place(x = 1000, y = 390) 
        hinhtruong = Image.open(r'D:\doanPLC\BARCODE\screen\hinhtruong.jpg')
        resized_hinhtruong = hinhtruong.resize((568,420),Image.ANTIALIAS)
        hinhtruong = ImageTk.PhotoImage(resized_hinhtruong)
        hinhtruong_label = tk.Label(self, image= hinhtruong, bg = "white")
        hinhtruong_label.image = hinhtruong
        hinhtruong_label.place(x = 600, y = 280)

               #Graphics self.root
        imageFrame = tk.Frame(self, width=500, height=350)
        imageFrame.place(x=30,y=200)
        #Capture video frames
        lmain = tk.Label(imageFrame)
        lmain.place(x=0,y=0)
        #send data to PLC
        # use modbus TCP
        client = mbclient('192.168.0.1', port=502)  # IP PLC
        client.connect()
        print('Connect')
        UNIT = 0x1
        cap = cv2.VideoCapture(0)
        #self.dem_sp_vang = 0
        #self.dem_sp_tim = 0
        #self.dem_sp_xanh = 0
        def show_frame():
            myOutputPLC = 0
            
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (dim))
            hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            height, width, _ = frame.shape
            cx = int(width / 2 + 150 )
            cy = int(height / 2)

            # Pick pixel value
            pixel_center = hsv_frame[cy, cx]
            hue_value = pixel_center[0]
            color = "Undefined"
            color_yellow = False
            color_blue = False
            color_purple = False
            if hue_value > 25 and hue_value <32:
                color = "Yellow"
                myOutput = 'Loai 1'
                #myOutputPLC = 1
                color_yellow = True
                #self.dem_sp_vang = self.dem_sp_vang + 1
                loaisp = tk.StringVar()
                loaisp.set("VANG")
                #dem_vang = tk.Entry(self, width=12,fg='red',border=2,bg='white',font=('Helvetica', 17, 'bold'), state='readonly', textvariable= loaisp)
                #dem_vang.place(x = 970, y = 250) 
            elif hue_value < 128 and hue_value> 91:
                color = "BLUE"
                myOutput = 'Loai 2'
                #myOutputPLC = 2
                loaisp = tk.StringVar()
                loaisp.set("XANH")
                color_blue = True
                #dem_vang = tk.Entry(self, width=12,fg='red',border=2,bg='white',font=('Helvetica', 17, 'bold'), state='readonly', textvariable= loaisp)
                #dem_vang.place(x = 970, y = 250) 
                #self.dem_sp_xanh = self.dem_sp_xanh + 1
                #xanh = tk.StringVar()
                #xanh.set(int(self.dem_sp_xanh/17))
                #dem_xanh = tk.Entry(self, width=5,fg='red',border=2,bg='white',font=('Helvetica', 18, 'bold'), state='readonly',textvariable=xanh)
                #dem_xanh.place(x = 1000, y = 390) 
            elif hue_value > 140 and hue_value <172:
                color = "PURPLE"
                myOutput = 'Loai 3'
                myOutputPLC = 3
                loaisp = tk.StringVar()
                loaisp.set("TIM")
                color_purple = True
                #dem_vang = tk.Entry(self, width=12,fg='red',border=2,bg='white',font=('Helvetica', 17, 'bold'), state='readonly', textvariable= loaisp)
                #dem_vang.place(x = 970, y = 250) 
                #self.dem_sp_tim = self.dem_sp_tim + 1
                #tim = tk.StringVar()
                #tim.set(int(self.dem_sp_tim/15))
                #dem_tim = tk.Entry(self, width=5,fg='red',border=2,bg='white',font=('Helvetica', 18, 'bold'), state='readonly',textvariable=tim)
                #dem_tim.place(x = 1000, y = 320) 
            
            else:
                color = "Undefined"
                myOutputPLC = 0
                loaisp = tk.StringVar()
                loaisp.set("Undefined")
                #dem_vang = tk.Entry(self, width=12,fg='red',border=2,bg='white',font=('Helvetica', 17, 'bold'), state='readonly', textvariable= loaisp)
                #dem_vang.place(x = 970, y = 250) 
            if color_yellow == True:
                color_yellow = False
                myOutputPLC = 1
            if color_blue == True:
                color_blue = False
                myOutputPLC = 2
            if color_purple == True:
                color_purple = False
                myOutputPLC = 3
                

                
                
            
                
            #print("the output of PLC is" + str(myOutputPLC))
            pixel_center_bgr = frame[cy, cx]
            b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
            #cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
            cv2.putText(frame, color, (cx-300, 100), 0, 2, (255, 255, 255), 5)
            cv2.circle(frame, (cx-50, cy), 5, (25, 25, 25), 3)
            client.write_register(0, int(myOutputPLC), unit=UNIT)  # if using modbus register 0 (mau sac)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(2, show_frame) 
        show_frame()  #Display 2
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 708)
        window.grid_columnconfigure(0, minsize = 1180)
        
        self.frames = {}
        for F in (FirstPage, SecondPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")
            
app = Application()
app.maxsize(1180,708)
app.mainloop()            
            
        
