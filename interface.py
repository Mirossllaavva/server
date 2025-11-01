from customtkinter import*
from PIL import Image
window = CTk()
window.title("Чат")
window.geometry("600x600")
window.configure(fg_color = "pink")
rama = CTkFrame(window, fg_color = "white", width = 400, height = 400)
rama.pack_propagate(False)
rama.place(x = 110, y = 100)

text_box =  CTkTextbox(rama, fg_color = "black")

text_box.pack()
widget_entry = CTkEntry(window, fg_color = "white", width = 300)
widget_entry.place(x = 100, y = 520)
image = Image.open("кнопка отправки.png")
CTk_image = CTkImage(light_image = image, size = (20, 10))
btn = CTkButton(window,text = "Почати", image = CTk_image, compound = "right")
btn.place(x = 420, y = 520)

label = CTkLabel(window, text = "222")
label.pack()













window.mainloop()