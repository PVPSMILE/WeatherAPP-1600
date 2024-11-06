import customtkinter as ctk
from ..json_functions.read_json import read_json
from .scroll_frame import scrollabel_frame

data = read_json(name_json= 'config_weather.json')

curent_city = data['name']
curent_city_temp = round(data['main']['temp'])
curent_city_weather = data['weather'][0]['description']

class City_Frame(ctk.CTkFrame):
    def __init__(self, master : str, **kwargs):
        ctk.CTkFrame.__init__(self,
            master,
            height= 105,
            width=236,
            fg_color = "#4599A4",
            border_color = "#FFFFFF",
            corner_radius = 15,
            border_width = 2,
            **kwargs)
        
        self.pack(pady = (30, 0))
        
        DATA_WEATHER = read_json(name_json = "config_weather.json")
    
        curent_position =  ctk.CTkLabel(
            master = self,
            text = 'Николай жук❤️',
            font = ('Roboto Slab', 16, 'bold'),
            text_color = 'white'
        )
        curent_position.place(x = 14,y = 6)

        label_for_temp = ctk.CTkLabel(
            master = self,
            text = f'{round(DATA_WEATHER["main"]["temp"])}°',
            font = ('Inter', 50, 'bold'),
            text_color = 'white'
        )

        label_for_temp.place(x = 150 , y = 8)

frame_1 = City_Frame(master=scrollabel_frame)
frame_2 = City_Frame(master=scrollabel_frame)
frame_3 = City_Frame(master=scrollabel_frame)





