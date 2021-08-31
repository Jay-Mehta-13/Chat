# GUI for clients
from tkinter import *
import client

window = Tk()
window.title("Chat")

def send_message():
    msg = message.get("1.0", END)
    message.delete('1.0', END)
    rev_msg = client.send_server(msg)
    received.config(text=rev_msg)

message = Text(window, width=60, height=5, borderwidth=10, fg='Black', font='14')
message.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Received message
rev_msg = 'Nothing Yet'

received = Label(window, text=rev_msg)
received.grid(row=1, column=0)

button_send = Button(window, text='Send', font='Georgia 14', command=send_message)
button_send.grid(row=0, column=6)

window.mainloop()
