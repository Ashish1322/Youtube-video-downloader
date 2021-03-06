# Importing some Modules used to make proeject

from tkinter import  *
from tkinter import  filedialog
from pytube import  YouTube
import pyautogui

# Setting the window
root = Tk()
root.geometry('800x500')
root.minsize(800,500)
root.maxsize(800,500)

ls = [] # Empty list for that: when user can choose directory the path will be append in it and we can use this path in download video func as ls[0] because it has only one element and after the downloading we clear the list


def youtube_download():
    '''This is used to download the video and error handling'''
    url_var = urlvalue.get()
    z = False

    try:  # if url is correct then z = True and due to this 39 line code will run and video will download because if we cannot use condition in line 39 . then if user url is incorrect so execpt block will be run but try block will not be ran so the 'a' inside try block will not be declared and without condition if we use the code of lin 39 then it will try to download video a.streams.first().download(n) and raise error because a is not declared because try block is not ran. So we use the condition if try block ran then line 39 will exicute
        global a
        a = YouTube(url_var)
        z = True
    except:  # handling error if user url is empty or not found
        pyautogui.alert('URL not found !')
        urlvalue.set('')

    if len(ls)==0 : # Error handling of there is no directory choosen becaue of empty list
        pyautogui.alert('Please choose Location !')
    else:
        n = ls[0]
        n = n.replace('/','\\') # Replacing the character / in url path to \ because download will use \
        print(n)

        if z==True: #it will exicute only if try block will be ran due to conditon . This code download the video and clear the entry widget as well as list
            a.streams.first().download(n)
            pyautogui.alert(' Video Downloaded Successfully \n at Location {}'.format(n))
            urlvalue.set('')
            ls.clear()
            root.destroy()



def ask_for_dir():
    '''This Function is used to ask the user for choose the path'''
    location = filedialog.askdirectory()
    print(location)
    ls.append(location)

#setting the icon and title of window
root.title('Youtube video downloader')
photo = PhotoImage(file='1.png')
root.iconphoto(False,photo)

# Setting image Label header
head = Label(root,text='Download Youtube videos easily',font='Arial 25 bold',fg='red')
head.pack()
photo1 = PhotoImage(file='2.png')
image_label = Label(root,image=photo1)
image_label.pack()


#Setting url label and entry tag
url = Label(root,text='Enter URL: ',font='Arial 15 bold')
url.pack()
urlvalue = StringVar()
urlentry = Entry(root,textvariable=urlvalue,width=70,bd=4,relief=GROOVE)
urlentry.pack(pady=10,padx=100)


#Button for chosing files
file_chooe = Button(root,text='Choose Location',command=ask_for_dir,bd=2,relief=RIDGE,font='Arial 9 bold',height=1,width=15,bg='black',fg='white')
file_chooe.pack(pady=10)

# Submit Botton
b = Button(root,text='Download',font='Arial 13 bold',bg='grey',bd=2,relief=RIDGE,command=youtube_download,height=1,width=9)
b.pack(pady=20)

root.mainloop()