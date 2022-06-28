from tkinter import *
from tkinter import messagebox
import twilio
from twilio.rest import Client
import smtplib
import random

otp = random.randint(1000, 9999)
otp = str(otp)

Mo = Tk()
Mo.title("Send OTP on Mobile")
Mo.geometry("565x250")
Mobile_label = Label(Mo, text="Enter Mobile no: ", font="ariel 15 bold", relief=FLAT)
Mobile_label.grid(row=0, column=0, padx=15, pady=60)
Mobile_entry = Entry(Mo, font="ariel 15 bold", width=25, relief=GROOVE, bd=2)
Mobile_entry.grid(row=0, column=1, padx=12, pady=60)
Mobile_entry.focus()


def sms():
    account_sid = 'AC75cfa95aa7fde813551bc216a9a18977'
    auth_token = '5d37fea024701586bb168228cc603b11'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Hello Your Secure Device OTP is - ' + str(otp),
        from_='19292051587',
        to=Mobile_entry.get())
    messagebox.showinfo("Send OTP via SMS", f"OTP sent to {Mobile_entry.get()}")


Mob_button = Button(Mo, text="Send SMS", font="ariel 15 bold", bg="black", fg="green2", bd=3, command=sms)
Mob_button.place(x=210, y=150)
Mo.mainloop()

root = Tk()
root.title("Send OTP Via Email")
root.geometry("565x450")
email_label = Label(root, text="Enter receiver's Email: ", font="ariel 15 bold", relief=FLAT)
email_label.grid(row=0, column=0, padx=15, pady=60)
email_entry = Entry(root, font="ariel 15 bold", width=25, relief=GROOVE, bd=2)
email_entry.grid(row=0, column=1, padx=12, pady=60)
email_entry.focus()


def send():
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
        s.starttls()
        ssender = "pythonproject24@gmail.com"
        spass = "myzxaqasdfzwpdzy"
        s.login(ssender, spass)
        s.sendmail(ssender, email_entry.get(), otp)
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {email_entry.get()}")
        s.quit()

    except:
        messagebox.showinfo("Send OTP via Email",
                            "Please enter the valid email address OR check an internet connection")


send_button = Button(root, text="Send Email", font="ariel 15 bold", bg="black", fg="green2", bd=3, command=send)
send_button.place(x=210, y=150)
root.mainloop()