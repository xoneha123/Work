import tkinter as tk
from tkinter import ttk
import json

LARGEFONT = ("Verdana", 35)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Weather, Temperature, Humidity, HistoricalData):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Weather)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Weather(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Weather", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Temperature", command=lambda: controller.show_frame(Temperature))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Humidity", command=lambda: controller.show_frame(Humidity))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Historical Data", command=lambda: controller.show_frame(HistoricalData))
        button3.grid(row=3, column=1, padx=10, pady=10)


class Temperature(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Temperature", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        temp_label = ttk.Label(self, text="Fetching temperature...", font=("Verdana", 20))
        temp_label.grid(row=1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Weather", command=lambda: controller.show_frame(Weather))
        button1.grid(row=2, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Humidity", command=lambda: controller.show_frame(Humidity))
        button2.grid(row=3, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Historical Data", command=lambda: controller.show_frame(HistoricalData))
        button3.grid(row=4, column=1, padx=10, pady=10)

        # Read temperature data from JSON file
        try:
            with open('data.json') as file:
                data = json.load(file)
                temperature = data.get('temperature')
                if temperature:
                    temp_label.configure(text=f"Temperature: {temperature}°C")
                else:
                    temp_label.configure(text="Temperature data not found")
        except FileNotFoundError:
            temp_label.configure(text="Data file not found")


class Humidity(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Humidity", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Temperature", command=lambda: controller.show_frame(Temperature))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Weather", command=lambda: controller.show_frame(Weather))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Historical Data", command=lambda: controller.show_frame(HistoricalData))
        button3.grid(row=3, column=1, padx=10, pady=10)


class HistoricalData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Historical Weather Data", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        date_label = ttk.Label(self, text="Select Date:", font=("Verdana", 20))
        date_label.grid(row=1, column=1, padx=10, pady=10)

        date_picker = ttk.Entry(self, font=("Verdana", 16))
        date_picker.grid(row=2, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Weather", command=lambda: controller.show_frame(Weather))
        button1.grid(row=3, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Temperature", command=lambda: controller.show_frame(Temperature))
        button2.grid(row=4, column=1, padx=10, pady=10)

        # Add a button to fetch and display the historical weather data
        button3 = ttk.Button(self, text="Fetch Data", command=lambda: self.fetch_historical_data(date_picker.get()))
        button3.grid(row=5, column=1, padx=10, pady=10)

        self.historical_data_label = ttk.Label(self, text="", font=("Verdana", 20))
        self.historical_data_label.grid(row=6, column=1, padx=10, pady=10)

    def fetch_historical_data(self, selected_date):
        # For demonstration purposes, just display the selected date without fetching data
        self.historical_data_label.configure(text=f"Display historical weather data for {selected_date}")


# Driver Code
app = tkinterApp()
app.mainloop()
