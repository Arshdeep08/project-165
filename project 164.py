from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("image viewer")
root.geometry("500x500")
root.configure(background="black")

label_image = Label(root, bg="white", highlightthickness=5)
img_path = ""

def OpenImage():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Text File", filetypes=[("Image Files","*jpg;*.gif;*.jpg;;*.png")])
    print(img_path)
    im = ImageTk.PhotoImage(Image.open ("charizard.png"))
    label_image["image"] = im
    im.close()

def RotateImage():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Text File", filetypes=[("Image Files","*jpg;*.gif;*.jpg;;*.png")])
    print(img_path)
    im = ImageTk.PhotoImage(Image.open ("charizard.png"))
    img = im.rotate(180)
    label_image["image"] = img
    im.close()

btn = Button(root, text="Open Image", command = OpenImage)
btn.place(relx=0.5, rely=0.18, anchor = CENTER)
btn2 = Button(root, text="Rotate Image", command = RotateImage)
btn2.place(relx=0.5, rely=0.6, anchor = CENTER)


label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()