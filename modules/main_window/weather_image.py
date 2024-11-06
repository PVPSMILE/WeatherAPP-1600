import customtkinter as ctk
import PIL.Image
from .main_frame import app
from ..json_functions.read_json import read_json
import os


class WeatherImage(ctk.CTkLabel):
    def __init__(self, master: object, **kwargs):
        ctk.CTkLabel.__init__(
            self,
            master = master,
            image = self.load_image(),   
            text = "",
            **kwargs
        )

    def load_image(self):
        weather_data = read_json(name_json = "config_weather.json")
        
        icon_name = weather_data["weather"][0]["icon"]

        path_image = os.path.abspath(__file__ + f"/../../../media/images/{icon_name}.png")
        
        open_icon = PIL.Image.open(fp = path_image)

        return ctk.CTkImage(light_image = open_icon , size = (170 , 160))
        
image = WeatherImage(master = app)
image.place(x = 380 , y = 170)