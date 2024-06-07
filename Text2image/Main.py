import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as tm
import trans as ret
import Driver as genimg

# Colors
bgcolor = "#89cff0"  # Light blue
bgcolor1 = "#1e4f6e"  # Dark blue
fgcolor = "#008080"  # Teal

def Home():
    def clear():
        txt.delete(0, 'end') 
        txt2.delete(0, 'end')

    def lan1toeng(event=None):
        sym = txt.get()
        if sym:
            translated = ret.get_translation(sym)
            txt2.delete(0, 'end')
            txt2.insert('end', translated)
        else:
            tm.showinfo("Input error", "Enter your text")

    def generate_image():
        sym = txt2.get()
        if sym:
            genimg.process(sym)
        else:
            tm.showinfo("Input error", "Enter your text")

    # Main window
    window = tk.Tk()
    window.title("Image to Text Generator")
    window.attributes('-fullscreen', True)  # Set fullscreen

    # Background image
    bg_image = Image.open("bg.jpg")
    bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Title
    message1 = tk.Label(window, text="Image to Text Generator", bg=bgcolor, fg=fgcolor, font=('Helvetica', 30, 'bold'))
    message1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Input label and entry
    lbl = tk.Label(window, text="Enter Your Text", fg=fgcolor, font=('Helvetica', 20))
    lbl.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    txt = tk.Entry(window, width=40, fg=fgcolor, font=('Helvetica', 15), highlightthickness=0, highlightbackground=bgcolor) # Set highlightthickness and highlightbackground
    txt.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    txt.focus()  # Set focus to input box
    txt.bind("<Return>", lan1toeng)  # Bind Enter key to translate function

    # Output label and entry
    lbl2 = tk.Label(window, text="Do you mean:", fg=fgcolor, font=('Helvetica', 20))
    lbl2.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    txt2 = tk.Entry(window, width=70, fg="red", font=('Helvetica', 15), highlightthickness=0, highlightbackground=bgcolor) # Set highlightthickness and highlightbackground
    txt2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Generate image button
    generate_image_btn = tk.Button(window, text="Generate Image", command=generate_image, fg=fgcolor, bg=bgcolor1, font=('Helvetica', 15, 'bold'), relief=tk.RAISED)
    generate_image_btn.place(relx=0.35, rely=0.7, anchor=tk.CENTER)

    # Clear button
    clear_btn = tk.Button(window, text="Clear", command=clear, fg=fgcolor, bg=bgcolor1, font=('Helvetica', 15, 'bold'), relief=tk.RAISED)
    clear_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    # Quit button
    quit_btn = tk.Button(window, text="Quit", command=window.destroy, fg=fgcolor, bg=bgcolor1, font=('Helvetica', 15, 'bold'), relief=tk.RAISED)
    quit_btn.place(relx=0.65, rely=0.7, anchor=tk.CENTER)

    # Automatically translate text on startup
    lan1toeng()

    window.mainloop()

Home()
