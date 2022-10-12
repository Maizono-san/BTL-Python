from tkinter import *


window = Tk()

window.geometry('950x550')
window.title("Weather Forecast")
icon = PhotoImage(file = 'images\\icon.png')
window.iconphoto(True,icon)
window.resizable(False,False)

#BackGroundImage
background = PhotoImage(file = 'images\\background.png')
background_image = Label(window,
                         image = background)
background_image.pack()



#BackGroundGif
# info = Image.open("images\\background.gif")
# framnr = info.n_frames
# frames = [PhotoImage(file="images\\background.gif",
#                     format = 'gif -index %i' %(i)) for i in range(framnr)]

# def update(ind):
#       frame = frames[ind]
#       ind += 1
#       if ind > framnr - 1: 
#          ind = 0
#       Back_Ground_Gif.configure(image = frame)
#       window.after(50, update, ind)
    
# Back_Ground_Gif = Label(window)
# Back_Ground_Gif.pack()
# window.after(50, update, 0)


#SearchBar
searchbar = PhotoImage(file = 'images\\searchbar.png')
Label (window,
       image = searchbar,
       bg = '#4d99e7'
       ).place(x = 245,y = 4)

#HomeButton
home = PhotoImage(file = 'images\\home.png')
Button (window,
        image = home,
        bg = '#4d99e7',
        activebackground = '#4d99e7',
        cursor = 'hand2',
        ).place(x = 5,y = 5)


#SettingButton
setting = PhotoImage(file = 'images\\setting.png')   
Button (window,
        image = setting,
        bg = '#4d99e7',
        activebackground = '#4d99e7',
        cursor = 'hand2'
        ).place(x = 899,y = 5)

#SearchButton
search = PhotoImage(file = 'images\\search.png')
Button (window,
        image = search,
        bg = '#69adf4',
        activebackground= '#69adf4',
        borderwidth = 0,
        cursor = 'hand2'
        ).place(x = 595,y = 11)

#Entry
Entry  (window,
        width = 18,
        font = ('poppins',20,'bold'),
        fg = 'white',
        insertbackground = 'white',
        bg = '#69adf4',
        border = 0
        ).place(x = 317,y = 12)

#BigBox
bigbox = PhotoImage(file = 'images\\big.png')
bigbox_image = Label(window,
                     image = bigbox,
                     bg = '#4d99e7',
                     relief = GROOVE)
bigbox_image.place(x = 20,y = 390)

#SmallBoxes
smallbox = PhotoImage(file = 'images\\small.png')
Label(window,
      image = smallbox,
      bg = '#4d99e7',
      relief = GROOVE).place(x = 300,y = 405)
Label(window,
      image = smallbox,
      bg = '#4d99e7',
      relief = GROOVE).place(x = 410 ,y = 405)
Label(window,
      image = smallbox,
      bg = '#4d99e7',
      relief = GROOVE).place(x = 520 ,y = 405)
Label(window,
      image = smallbox,
      bg = '#4d99e7',
      relief = GROOVE).place(x = 630 ,y = 405)
Label(window,
      image = smallbox,
      bg = '#4d99e7',
      relief = GROOVE).place(x = 740 ,y = 405)
Label(window,
      image = smallbox,
      bg = '#4d99e7',
      relief = GROOVE).place(x = 850 ,y = 405)

window.mainloop()
