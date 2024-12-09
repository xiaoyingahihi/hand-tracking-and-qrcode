from tkinter import simpledialog
import webbrowser
import cv2
import hand as htm
import tkinter as tk
import mediapipe as mp
import numpy as np
import pyautogui
import screen_brightness_control as sbc

from tkinter import messagebox
from PIL import Image, ImageTk 
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from hand import handDetector

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PHAM THE VINH")

        # logo
        self.logo_image = Image.open("hand_tracking_and_qrcode/logoute1.png")
        new_size = (750, 180)  
        self.logo_image = self.logo_image.resize(new_size, Image.Resampling.LANCZOS)
        self.logo_photo1 = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(root, image=self.logo_photo1)
        self.logo_label.place(x=0, y=0)

        # logo
        self.logo_image2 = Image.open("hand_tracking_and_qrcode/logoclc.png")  
        new_size2 = (150, 150)  
        self.logo_image2 = self.logo_image2.resize(new_size2, Image.Resampling.LANCZOS)
        self.logo_photo2 = ImageTk.PhotoImage(self.logo_image2)
        self.logo_label2 = tk.Label(root, image=self.logo_photo2)
        self.logo_label2.place(x=1100, y=20)

        # Text
        self.text_label = tk.Label(root, text="PROJECT 3 CHOICE",
                                  font=("Helvetica", 36, "bold"), fg="red")
        self.text_label.place(x=360, y=210)
        self.text_label1 = tk.Label(root, text="Sinh viên thực hiện:",
                                  font=("Helvetica", 16, "bold"), fg="black")
        self.text_label1.place(x=150, y=385)
        self.text_label2 = tk.Label(root, text="Phạm Thế Vinh",
                                  font=("Helvetica", 16, ""), fg="black")
        self.text_label2.place(x=425, y=386)
        self.text_label3 = tk.Label(root, text="Mã số sinh viên:",
                                  font=("Helvetica", 16, "bold"), fg="black")
        self.text_label3.place(x=150, y=420)
        self.text_label4 = tk.Label(root, text="21161388",
                                  font=("Helvetica", 16, ""), fg="black")
        self.text_label4.place(x=370, y=421)
        self.text_label5 = tk.Label(root, text="Ngành:",
                                  font=("Helvetica", 16, "bold"), fg="black")
        self.text_label5.place(x=150, y=455)
        self.text_label6 = tk.Label(root, text="Công nghệ Kỹ thuật Điện tử - Viễn thông",
                                  font=("Helvetica", 16, ""), fg="black")
        self.text_label6.place(x=250, y=456)
        self.text_label7 = tk.Label(root, text="Lớp:",
                                  font=("Helvetica", 16, "bold"), fg="black")
        self.text_label7.place(x=150, y=490)
        self.text_label8 = tk.Label(root, text="21161CLĐT2B",
                                  font=("Helvetica", 16, ""), fg="black")
        self.text_label8.place(x=220, y=491)
        
        # button
        self.image = Image.open("hand_tracking_and_qrcode/start.jpg")  
        self.image = self.image.resize((250, 250), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.start_button = tk.Button(root, command=self.login_window, image=self.photo, bg="#000000", relief="flat",
                                        bd=5, width=250, height=250)
        self.start_button.place(x=850, y=370)

        self.image1 = Image.open("hand_tracking_and_qrcode/fblogo.png")  
        self.image1 = self.image1.resize((150, 47), Image.Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.start_button1 = tk.Button(root, command=self.open_linkfb, image=self.photo1, bg="#1b3ab5", relief="flat",
                                        bd=5, width=150, height=51)
        self.start_button1.place(x=150, y=560)

        self.image2 = Image.open("hand_tracking_and_qrcode/inslogo.jpg")  
        self.image2 = self.image2.resize((150, 47), Image.Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.start_button2 = tk.Button(root, command=self.open_linkins, image=self.photo2, bg="#b51b94", relief="flat",
                                        bd=5, width=150, height=51)
        self.start_button2.place(x=350, y=560)

        #control_volume_mouse_dosang
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))

        self.volRange = self.volume.GetVolumeRange() 
        self.minVol = self.volRange[0]
        self.maxVol = self.volRange[1]

        self.mode = 0  
        self.state_truoc = None 
        self.volume_hientai = 0  
        self.dosang_hientai = 100  

        self.detector = handDetector(detectionCon=0.5)

    #link
    def open_linkfb(self):      
        url1 = "https://www.facebook.com/x.369369"
        webbrowser.open(url1)
    def open_linkins(self):
        url2 = "https://www.instagram.com/fontcat8888"
        webbrowser.open(url2)
    
    #login
    def login_window(self):
        self.window = tk.Toplevel(self.root)
        self.window.geometry("300x200")
        self.window.title("Đăng Nhập")
        tk.Label(self.window, text="Nhập Mật Khẩu:").pack(pady=20)
        self.password_entry = tk.Entry(self.window, show='*')
        self.password_entry.pack()
        tk.Button(self.window, text="Xác nhận", command=self.check_password).pack(pady=10)
    def check_password(self):
        password = self.password_entry.get()
        if password == '21161388':
            self.window.destroy()
            self.show_main_menu()
        else:
            messagebox.showerror("Lỗi", "Sai Mật Khẩu")
            self.window.destroy()
    
    #menu
    def show_main_menu(self):
        self.logo_label.place_forget()
        self.logo_label2.place_forget()
        self.text_label.place_forget()
        self.text_label1.place_forget()
        self.text_label2.place_forget()
        self.text_label3.place_forget()
        self.text_label4.place_forget()
        self.text_label5.place_forget()
        self.text_label6.place_forget()
        self.text_label7.place_forget()
        self.text_label8.place_forget()
        self.start_button.place_forget()
        self.start_button1.place_forget()   
        self.start_button2.place_forget()   
    #client 
        self.logo_image3 = Image.open("hand_tracking_and_qrcode/background.png")
        new_size = (1280, 720)  
        self.logo_image3 = self.logo_image3.resize(new_size, Image.Resampling.LANCZOS)
        self.logo_photo3 = ImageTk.PhotoImage(self.logo_image3)
        self.logo_labe9 = tk.Label(root, image=self.logo_photo3)
        self.logo_labe9.place(x=-5, y=-5)
    #button
        self.image = Image.open("hand_tracking_and_qrcode/qrcodebt.png")  
        self.image = self.image.resize((200, 112), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.start_button = tk.Button(self.root, command=self.qrcode, image=self.photo, bg="#e33d20", relief="flat",
                                        bd=5, width=200, height=112)
        self.start_button.place(x=50, y=50)

        self.image1 = Image.open("hand_tracking_and_qrcode/countfbt.png")  
        self.image1 = self.image1.resize((200, 112), Image.Resampling.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.start_button = tk.Button(self.root, command=self.start_video, image=self.photo1, bg="#193c9c", relief="flat",
                                        bd=5, width=200, height=112)
        self.start_button.place(x=50, y=200)

        self.image2 = Image.open("hand_tracking_and_qrcode/3statebt.png")  
        self.image2 = self.image2.resize((200, 112), Image.Resampling.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.start_button = tk.Button(self.root, command=self.control_volume_mouse_dosang, image=self.photo2, bg="#42a156", relief="flat",
                                        bd=5, width=200, height=112)
        self.start_button.place(x=50, y=350)
    
    #qr
    def qrcode(self):
        messagebox.showinfo("Thông báo", "Xác nhận chạy chương trình!")
        qrc = cv2.QRCodeDetector()
        cam = cv2.VideoCapture('hand_tracking_and_qrcode/SPKT.mp4')
        while True:
            ret, frame = cam.read()
            if ret:
                ret_qr, decode_info, points, _ = qrc.detectAndDecodeMulti(frame)
                if ret_qr:
                    for s, p in zip(decode_info, points):
                        if s:
                            cv2.putText(frame, s, (100,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)
                        else:
                            pass
                        frame = cv2.polylines(frame, [p.astype(int)], True, (0,0,255), 8)
                cv2.imshow('QR Code', frame)
                print(decode_info)

            if cv2.waitKey(1) == ord('q'):
                break
        cv2.destroyAllWindows()
        messagebox.showinfo("Thông báo", "Chương trình kết thúc")
    
    #countfingers
    def start_video(self):
        cam = cv2.VideoCapture(0)
        detector = htm.handDetector(detectionCon=0.5)
        diemdaungontay = [4, 8, 12, 16, 20]
        messagebox.showinfo("Thông báo", "Xác nhận chạy chương trình!")
        while True:
            ret, frame = cam.read()
            if not ret:
                break

            frame = detector.findHands(frame)
            hands = detector.findPositions(frame)

            for hand in hands:
                lmList = hand['lmList']
                handType = hand['type']
                print(f"{handType} hand landmarks: {lmList}")
                ngontay = [0] * 5

                if len(lmList) > 0:
                    if (lmList[diemdaungontay[0]][1] < lmList[diemdaungontay[0] - 1][1]) and (handType == 'Right'):
                        ngontay[0] = 1
                    else:
                        if (lmList[diemdaungontay[0]][1] > lmList[diemdaungontay[0] - 1][1]) and (handType == 'Left'):
                            ngontay[0] = 1

                    for id in range(1, 5):
                        if lmList[diemdaungontay[id]][2] < lmList[diemdaungontay[id] - 2][2]:
                            ngontay[id] = 1
                    
                    songontay = ngontay.count(1)
                    color = (0, 255, 0) if handType == 'Right' else (0, 0, 255)
                    position = (35, 60) if handType == 'Right' else (45, 160)
                    cv2.rectangle(frame, (0, 0) if handType == 'Right' else (0, 100), (200, 100) if handType == 'Right' else (200, 200), color, -1)
                    display_handType = 'Left' if handType == 'Right' else 'Right'
                    text = f'{display_handType}: {songontay}'
                    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            cv2.imshow('Nhan dien so ngon tay', frame)

            if cv2.waitKey(1) == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Thông báo", "Chương trình kết thúc")       
    
    #control_volume_mouse_dosang
    def control_volume(self, lmList):
        ngon_cai = lmList[4]   
        ngontro = lmList[8]   
        length = np.hypot(ngontro[1] - ngon_cai[1], ngontro[2] - ngon_cai[2])

        self.volume_hientai = np.interp(length, [15, 130], [self.minVol, self.maxVol])
        self.volume.SetMasterVolumeLevel(self.volume_hientai, None)
    def control_mouse(self, lmList, frame):
        screen_width, screen_height = pyautogui.size()
        scale = 2
        toadox = np.interp(lmList[8][1], [0, frame.shape[1]], [0, screen_width])
        toadoy = np.interp(lmList[8][2], [0, frame.shape[0]], [0, screen_height])
        scaled_x = screen_width - (toadox * scale)
        scaled_y = toadoy * scale
        pyautogui.moveTo(scaled_x, scaled_y)
        
        # click
        ngon_cai = lmList[4] 
        ngon_cai_toado2 = lmList[2] 

        length = np.hypot(ngon_cai[1] - ngon_cai_toado2[1], ngon_cai[2] - ngon_cai_toado2[2])  
        length1 = 20  
        if length < length1:
            pyautogui.click()
    def control_brightness(self, lmList):
        ngon_cai = lmList[4]  
        ngon_ut = lmList[20]  
        length_brightness = np.hypot(ngon_ut[1] - ngon_cai[1], ngon_ut[2] - ngon_cai[2])
        self.dosang_hientai = np.interp(length_brightness, [25, 150], [0, 100])
        print(length_brightness)
        sbc.set_brightness(int(self.dosang_hientai))
    def chuyen_trang_thai(self, lmList):
        if ((lmList[12][2] < lmList[10][2]) and (lmList[16][2] < lmList[14][2])):  
            return "closed"
        elif ((lmList[12][2] > lmList[10][2]) and (lmList[16][2] > lmList[14][2])):  
            return "open"
        return None  
    def hien_thi(self, frame):
        text = f"Mode: {['Volume', 'Mouse', 'Brightness'][self.mode]}"
        cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        if self.mode == 0:
            volume_hienthi = np.interp(self.volume_hientai, [self.minVol, self.maxVol], [0, 100])
            cv2.putText(frame, f"Volume: {int(volume_hienthi)}%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if self.mode == 2:
            cv2.putText(frame, f"Brightness: {int(self.dosang_hientai)}%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    def control_volume_mouse_dosang(self):
        cam = cv2.VideoCapture(2) 

        while True:
            ret, frame = cam.read()
            if not ret:
                break

            frame = self.detector.findHands(frame)  
            hands = self.detector.findPositions(frame, draw=False)

            if hands:
                lmList = hands[0]['lmList']  
                state_hientai = self.chuyen_trang_thai(lmList)

                if state_hientai and self.state_truoc and state_hientai != self.state_truoc:
                    if state_hientai == "closed":
                        self.mode = (self.mode + 1) % 3  
                        print(f"Switched to mode: {self.mode}")

                self.state_truoc = state_hientai  

                if self.mode == 0:
                    self.control_volume(lmList)  
                elif self.mode == 1:
                    self.control_mouse(lmList, frame) 
                elif self.mode == 2:
                    self.control_brightness(lmList) 

            self.hien_thi(frame)

            cv2.imshow("Image", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()    
        messagebox.showinfo("Thông báo", "Chương trình kết thúc")


root = tk.Tk()
app = App(root)
root.geometry("1280x720")
root.mainloop()
