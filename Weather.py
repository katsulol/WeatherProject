import requests as req
from key import key
import customtkinter as ctk

class SimpleApp(ctk.CTk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Weather App")
        self.geometry("400x400")

        self.info_label = ctk.CTkLabel(self, text="Write the name of the City.")
        self.info_label.pack(pady=10)

        self.user_input = ctk.CTkEntry(self)
        self.user_input.pack()


        self.get_weather_button = ctk.CTkButton(self, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.result_text = ctk.CTkTextbox(self, height=200, width=300)
        self.result_text.pack(pady=10)

    def get_weather(self):
        city = self.user_input.get()

        data = req.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}")

        if data.json()['cod'] == '404':
            self.result_text.delete("1.0", "end")
            self.result_text.insert("end", "No City Found")
        else:
            weather = data.json()['weather'][0]['main']
            temp = round(data.json()['main']['temp'])

            result = f"The weather in {city} is: {weather}\n"
            result += f"The temperature in {city} is: {temp}ºC"

            self.result_text.delete("1.0", "end")
            self.result_text.insert("end", result)


app = SimpleApp()
app.mainloop()
