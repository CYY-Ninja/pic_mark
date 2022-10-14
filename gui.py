import tkinter as tk
import requests
from PIL import Image, ImageTk
from marker import pic_marker_by_filestools as multi_marks


def mainWindow():
    app = tk.Tk()

    HEIGHT = 500
    WIDTH = 600

    app.title('水印定制工具')
    app.iconbitmap('')      # icon

    C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
    background_image= tk.PhotoImage(file='./landscape.png')
    background_label = tk.Label(app, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    C.pack()

    frame = tk.Frame(app,  bg='#42c2f4', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    #frame_window = C.create_window(100, 40, window=frame)

    textbox = tk.Entry(frame, font=40)
    textbox.place(relwidth=0.65, relheight=1)

    submit = tk.Button(frame, text='加载图片', font=40, command=lambda: multi_marks(textbox.get()))  # program
    #submit.config(font=)
    submit.place(relx=0.7, relheight=1, relwidth=0.3)

    lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    bg_color = 'white'
    results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
    results.config(font=40, bg=bg_color)
    results.place(relwidth=1, relheight=1)

    weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
    weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

    app.mainloop()


if __name__ == '__main__':
    mainWindow()
