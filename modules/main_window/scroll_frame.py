import customtkinter as ctk
from .main_frame import app, HEIGHT

scrollabel_frame = ctk.CTkScrollableFrame(app,
    width = 276,
    height = HEIGHT,
    fg_color= "#096C82",
    scrollbar_button_color= "#096C82",
    scrollbar_button_hover_color= "#096C82",
)

scrollabel_frame.pack(side= "left") 