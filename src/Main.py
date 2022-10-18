from tkinter import *
from PIL import Image,ImageTk,ImageSequence

window = Tk()

window.geometry('950x550')
window.title("Weather Forecast")
icon = PhotoImage(file = 'images\\icon.png')
window.iconphoto(True,icon)
window.resizable(False,False)

#Back_Ground_Gif snow

# info = Image.open("backgroundGIF\\snow.gif")
# framnr = info.n_frames
# frames = [PhotoImage(file="backgroundGIF\\snow.gif",
#                     format = 'gif -index %i' %(i)) for i in range(framnr)]

# def update(ind):
#       frame = frames[ind]
#       ind += 1
#       if ind > framnr - 1: 
#          ind = 0
#       Back_Ground_Gif.configure(image = frame)
#       window.after(40, update, ind)
    
# Back_Ground_Gif = Label(window)
# Back_Ground_Gif.place(x=0,y=0)
# window.after(0, update, 0)

#Back_Ground_Gif fog

# info = Image.open("backgroundGIF\\fog.gif")
# framnr = info.n_frames
# frames = [PhotoImage(file="backgroundGIF\\fog.gif",
#                     format = 'gif -index %i' %(i)) for i in range(framnr)]

# def update(ind):
#       frame = frames[ind]
#       ind += 1
#       if ind > framnr - 1: 
#          ind = 0
#       Back_Ground_Gif.configure(image = frame)
#       window.after(200, update, ind)
    
# Back_Ground_Gif = Label(window)
# Back_Ground_Gif.place(x=0,y=0)
# window.after(0, update, 0)

#Back_Ground_Gif thunderstorm

# info = Image.open("backgroundGIF\\thunderstorm.gif")
# framnr = info.n_frames
# frames = [PhotoImage(file="backgroundGIF\\thunderstorm.gif",
#                     format = 'gif -index %i' %(i)) for i in range(framnr)]

# def update(ind):
#       frame = frames[ind]
#       ind += 1
#       if ind > framnr - 1: 
#          ind = 0
#       Back_Ground_Gif.configure(image = frame)
#       window.after(70, update, ind)
    
# Back_Ground_Gif = Label(window)
# Back_Ground_Gif.place(x=0,y=0)
# window.after(0, update, 0)

# Back_Ground_Gif rain

info = Image.open("backgroundGIF\\rain.gif")
framnr = info.n_frames
frames = [PhotoImage(file="backgroundGIF\\rain.gif",
                    format = 'gif -index %i' %(i)) for i in range(framnr)]

def update(ind):
      frame = frames[ind]
      ind += 1
      if ind > framnr - 1: 
         ind = 0
      Back_Ground_Gif.configure(image = frame)
      window.after(20, update, ind)
    
Back_Ground_Gif = Label(window)
Back_Ground_Gif.place(x=0,y=0)
window.after(0, update, 0)

#Back_Ground_Gif cloud

# info = Image.open("backgroundGIF\\cloud.gif")
# framnr = info.n_frames
# frames = [PhotoImage(file="backgroundGIF\\cloud.gif",
#                     format = 'gif -index %i' %(i)) for i in range(framnr)]

# def update(ind):
#       frame = frames[ind]
#       ind += 1
#       if ind > framnr - 1: 
#          ind = 0
#       Back_Ground_Gif.configure(image = frame)
#       window.after(50, update, ind)
    
# Back_Ground_Gif = Label(window)
# Back_Ground_Gif.place(x=0,y=0)
# window.after(0, update, 0)

#Back_Ground_Gif sunny

# info = Image.open("backgroundGIF\\sunny.gif")
# framnr = info.n_frames
# frames = [PhotoImage(file="backgroundGIF\\sunny.gif",
#                     format = 'gif -index %i' %(i)) for i in range(framnr)]

# def update(ind):
#       frame = frames[ind]
#       ind += 1
#       if ind > framnr - 1: 
#          ind = 0
#       Back_Ground_Gif.configure(image = frame)
#       window.after(35, update, ind)
    
# Back_Ground_Gif = Label(window)
# Back_Ground_Gif.place(x=0,y=0)
# window.after(0, update, 0)

#Frame hold searchbar, settingbutton and home button
f = Frame(window,
          bg = '#364e70',
          width = 950,
          height = 57)
f.pack()

#SearchBar
searchbar = PhotoImage(file = 'images\\searchbar.png')
Label (f,
       image = searchbar,
       bg = '#364e70'
       ).place(x = 300,y = 4)

#HomeButton
home = PhotoImage(file = 'images\\home.png')
Button (f,
        image = home,
        bg = '#364e70',
        activebackground = '#364e70',
        cursor = 'hand2',
        ).place(x = 5,y = 5)


#SettingButton
setting = PhotoImage(file = 'images\\setting.png')   
Button (f,
        image = setting,
        bg = '#364e70',
        activebackground = '#364e70',
        cursor = 'hand2'
        ).place(x = 899,y = 5)

#SearchButton
search = PhotoImage(file = 'images\\search.png')
Button (f,
        image = search,
        bg = '#4e6381',
        activebackground= '#4e6381',
        borderwidth = 0,
        cursor = 'hand2'
        ).place(x = 595,y = 11)

#Entry
Entry  (f,
        width = 18,
        font = ('poppins',20,'bold'),
        fg = 'white',
        insertbackground = 'white',
        bg = '#4e6381',
        border = 0
        ).place(x = 317,y = 12)

#BigBox
bigbox = PhotoImage(file = 'images\\big.png')
bigbox_image = Label(window,
                     image = bigbox,
                     bg = '#4d99e7',
                     relief = GROOVE)
bigbox_image.place(x = 20,y = 390)

#BiggerBox
biggerbox = PhotoImage(file = 'images\\bigger.png')
bigbox_image = Label(window,
                     image = biggerbox,
                     bg = '#4d99e7',
                     relief = GROOVE)
bigbox_image.place(x = 20,y = 110)

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

#Information_in_BiggerBox
city = Label(window,
           text = 'Hanoi',
           font = ('Segoe UI',14,'bold'),
           fg = 'white',
           bg = '#364e70')
city.place(x = 35, y = 115)

td = Label(window,
             text = 'Today',
             font = ('Segoe UI',14,'bold'),
             fg = 'white',
             bg = '#364e70')
td.place(x = 35,y = 140)

time = Label(window,
             text = '9:00 PM',
             font = ('Segoe UI',10),
             fg = 'white',
             bg = '#364e70')
time.place(x = 35,y = 166)

big_weather_icon = PhotoImage(file = 'images\\rain_icon_big.png')
big_weather_icon_lb = Label(window,
                        image = big_weather_icon,
                        bg = '#364e70')
big_weather_icon_lb.place(x = 35,y = 190)

temperature = Label(window,
                    text = '24°C',
                    font = ('Segoe UI',38,'bold'),
                    bg = '#364e70',
                    fg = 'white')
temperature.place(x = 130, y = 190)

weather_status = Label(window,
                       text = 'Rainy',
                       font = ('Segoe UI',16,'bold'),
                       fg = 'white',
                       bg = '#364e70')
weather_status.place(x = 300,y = 210)

wind = Label(window,
             text = 'WIND',
             font = ('Segoe UI',11),
             bg = '#364e70',
             fg = 'white')
wind.place(x = 35,y = 280)

wind_v = Label(window,
             text = '8 km/h',
             font = ('Segoe UI',11),
             bg = '#364e70',
             fg = 'white')
wind_v.place(x = 35,y = 300)

humidity = Label(window,
             text = 'HUMIDITY',
             font = ('Segoe UI',11),
             bg = '#364e70',
             fg = 'white')
humidity.place(x = 135,y = 280)

humidity_percent = Label(window,
             text = '47%',
             font = ('Segoe UI',11),
             bg = '#364e70',
             fg = 'white')
humidity_percent.place(x = 135,y = 300)

visibility = Label(window,
             text = 'VISIBILITY',
             font = ('Segoe UI',11),
             bg = '#364e70',
             fg = 'white')
visibility.place(x = 235,y = 280)

visibility_s = Label(window,
             text = '9 km',
             font = ('Segoe UI',11),
             bg = '#364e70',
             fg = 'white')
visibility_s.place(x = 235,y = 300)

pressure = Label(window,
             text = 'PRESSURE',
             font = ('Segoe UI',11),
             bg = '#364e70',
             fg = 'white')
pressure.place(x = 335,y = 280)

pressure_milibar = Label(window,
             text = '1015 mb',
             font = ('Segoe UI',11),
             bg = '#364e70',
             fg = 'white')
pressure_milibar.place(x = 335,y = 300)

#Information_in_BigBox
Label(window,
      text = 'Tuesday 18',
      font = ('Segoe UI',12),
      bg = '#364e70',
      fg = 'white').place(x = 35,y = 400)

weather_icon = PhotoImage(file = 'images\\rain_icon.png')
Label(window,
      image = weather_icon,
      bg = '#364e70').place(x = 35,y = 440)

Label(window,
      text = '24°C',
      font = ('Segoe UI',12),
      bg = '#364e70',
      fg = 'white').place(x = 100,y = 435)

Label(window,
      text = '21°C',
      font = ('Segoe UI',12),
      bg = '#364e70',
      fg = 'white').place(x = 100,y = 465)

Label(window,
      text = 'Rainy',
      font = ('Segoe UI',12),
      bg = '#364e70',
      fg = 'white').place(x = 180,y = 445)

#Information_in_SmallBox
Label(window,
      text = 'Wed 19',
      font = ('Segoe UI',10),
      bg = '#364e70',
      fg = 'white').place(x = 315,y = 410)

small_weather_icon = PhotoImage(file = 'images\\rain_icon_small.png')

Label(window,
      image = small_weather_icon,
      bg = '#364e70').place(x = 315,y = 440)

Label(window,
      text = 'Thu 20',
      font = ('Segoe UI',10),
      bg = '#364e70',
      fg = 'white').place(x = 425,y = 410)

Label(window,
      image = small_weather_icon,
      bg = '#364e70').place(x = 425,y = 440)

Label(window,
      text = 'Fri 21',
      font = ('Segoe UI',10),
      bg = '#364e70',
      fg = 'white').place(x = 535,y = 410)

Label(window,
      image = small_weather_icon,
      bg = '#364e70').place(x = 535,y = 440)

Label(window,
      text = 'Sad 22',
      font = ('Segoe UI',10),
      bg = '#364e70',
      fg = 'white').place(x = 645,y = 410)

Label(window,
      image = small_weather_icon,
      bg = '#364e70').place(x = 645,y = 440)

Label(window,
      text = 'Sun 23',
      font = ('Segoe UI',10),
      bg = '#364e70',
      fg = 'white').place(x = 755,y = 410)

Label(window,
      image = small_weather_icon,
      bg = '#364e70').place(x = 755,y = 440)

Label(window,
      text = 'Mon 23',
      font = ('Segoe UI',10),
      bg = '#364e70',
      fg = 'white').place(x = 865,y = 410)

Label(window,
      image = small_weather_icon,
      bg = '#364e70').place(x = 865,y = 440)

window.mainloop()
