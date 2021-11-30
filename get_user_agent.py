import os
import sys
import pyshark
from user_agents import parse
from tkinter import *
from tkinter import filedialog
root = Tk()
# Please paste this in the terminal: files/wireshark_output.pcapng


def isMobileDevice(useragent):
    user_agent = parse(useragent)
    if user_agent.is_mobile:
        return True
    else:
        return False


def isTabletDevice(useragent):
    user_agent = parse(useragent)
    if user_agent.is_tablet:
        return True
    else:
        return False


def isPC(useragent):
    user_agent = parse(useragent)
    if user_agent.is_pc:
        return True
    else:
        return False


def getUserAgent():
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("pcapng files", "*.pcapng"), ("all files", "*.*")))
    if root.filename == '':
        print("No file selected")
        sys.exit()
    else:
        useragents = []
        cap = pyshark.FileCapture(
            root.filename, display_filter='frame contains "GET"')
        for packet in cap:
            print(packet['http'].user_agent)
            useragents.append(packet['http'].user_agent)
        i = 0
        for useragent in useragents:
            i = i+1
            if isMobileDevice(useragent):
                myLabel = Label(root, text="Mobile Device")
                myLabel.pack()
            elif isTabletDevice(useragent):
                myLabel = Label(root, text="Tablet Device")
                myLabel.pack()
            elif isPC(useragent):
                myLabel = Label(root, text="PC Device")
                myLabel.pack()
            else:
                myLabel = Label(root, text="Unknown Device")
                myLabel.pack()
            myLabel = Label(root, text="Packet"+str(i) +
                            ": " + useragent)
            myLabel.pack()
        cap.close()


fileInputBtn = Button(root, text="Choose file to scrape", command=getUserAgent)

fileInputBtn.pack()

root.mainloop()
