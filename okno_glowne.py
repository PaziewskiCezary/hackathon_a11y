from tkinter import *
 
window = Tk()
 
window.title("Odtwarzacz")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
 
window.geometry(str(screen_width)+'x'+str(screen_height))


photo = PhotoImage(file = r"C:\Users\Ada\Documents\neuroinformatyka\VII semestr\hackathon\pobrane.png")

photoimage = photo.subsample(3, 3)

 
retur = Button(window, image = photoimage)

retur.place(relx=0.1, rely=0.1, anchor='nw')

 
#retur.grid(column=0, row=0)

p_spo = PhotoImage(file = r"C:\Users\Ada\Documents\neuroinformatyka\VII semestr\hackathon\spo.png")

p_spo = p_spo.subsample(3, 3)

 
spo = Button(window, image = p_spo)

spo.place(relx=0.3, rely=0.5, anchor=CENTER)

 
#spo.grid(column=0, row=1)

p_yt = PhotoImage(file = r"C:\Users\Ada\Documents\neuroinformatyka\VII semestr\hackathon\yt.png")

p_yt = p_yt.subsample(3, 3)

 
yt = Button(window, image = p_yt)

yt.place(relx=0.6, rely=0.5, anchor=CENTER)

 
#yt.grid(column=1, row=1)

p_rr = PhotoImage(file = r"C:\Users\Ada\Documents\neuroinformatyka\VII semestr\hackathon\rr.png")

p_rr = p_rr.subsample(3, 3)

 
rr = Button(window, image = p_rr)

rr.place(relx=0.9, rely=0.5, anchor=CENTER)

 
#rr.grid(column=2, row=1)



 
window.mainloop()
