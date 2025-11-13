from customtkinter import*
from PIL import Image
window = CTk()
window.title("Чат")
window.geometry("600x600")
window.configure(fg_color = "#fffdd0")
rama = CTkFrame(window, fg_color ="#310062", width = 400, height = 400)
rama.pack_propagate(False)
rama.place(x = 110, y = 100)

text_box =  CTkTextbox(rama,width = 320, height = 330, fg_color = "white")
text_box.place(x = 55, y = 70)
text_box.configure(state = "disabled")
widget_entry = CTkEntry(window, fg_color = "white", width = 300, corner_radius = 100, border_width = 7, border_color="#310062")
widget_entry.place(x = 100, y = 520)
image = Image.open("кнопка отправки.png")
CTk_image = CTkImage(light_image = image, size = (20, 10))
def send():
    sms = widget_entry.get()
    widget_entry.delete(0, END)
    text_box.configure(state = "normal")
    text_box.insert(END,sms + "\n")
    text_box.configure(state = "disable")

    

btn = CTkButton(window,fg_color = "white", text = "Почати",text_color = "#310062",image = CTk_image, compound = "right", corner_radius = 100, border_width = 7, border_color="#310062", command = send)
btn.place(x = 420, y = 520)

label = CTkLabel(window, text = " Онлайн листування", font= CTkFont(family = "Bodoni MT Black", size = 24))
label.pack()













window.mainloop()