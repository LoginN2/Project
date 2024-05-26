import requests
from tkinter import *

# Функция для получения погоды
def get_weather():
    city = city_entry.get()
    if city:
        try:
            url = f"http://localhost:5000/weather?city={city}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if 'error' in data:
                # Выводим сообщение об ошибке
                weather_label['text'] = f"Ошибка: {data['error']}"
            else:
                weather_label['text'] = (
                    f"Город: {data['name']}\n"
                    f"Погода: {data['weather'][0]['main']}\n"
                    f"Температура: {data['main']['temp']}°C\n"
                    f"Ощущается как: {data['main']['feels_like']}°C"
                )
        # Обрабатываем возможные ошибки при запросе
        except requests.exceptions.RequestException as e:
            weather_label['text'] = f"Ошибка: {e}"

# главное окно
root = Tk()
root.title("Прогноз погоды")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


x = (screen_width - 350) // 2
y = (screen_height - 200) // 2

# размер и позицию окна
root.geometry(f"400x200+{x}+{y}")


city_label = Label(root, text="Введите город:")
city_label.pack(pady=10)


city_entry = Entry(root)
city_entry.pack(pady=5)

# кнопка "Получить погоду"
get_weather_button = Button(root, text="Получить прогноз", command=get_weather)
get_weather_button.pack(pady=5)


weather_label = Label(root, text="", justify="left", wraplength=300)
weather_label.pack()


root.mainloop()
