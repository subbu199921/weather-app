# Weather App 

A simple and elegant **Weather App** built with **Django**, utilizing the **OpenWeather API** to fetch real-time weather information. The app features an interactive and animated UI for a great user experience.

Website link :  https://subhashweather.pythonanywhere.com/

##  Features

1 **Search City Weather** - Users can search for any city's weather conditions.
2 **Current Weather Details** - Displays temperature, humidity, wind speed, and weather descriptions.
3 **Beautiful UI & Animations** - Smooth fade-in effects, sliding animations, and rotating weather icons.
4 **Mobile Responsive** - Works seamlessly on all devices.
5 **Django Template Rendering** - Uses Django templates to display dynamic data.
6 **Real-Time Weather Updates** - Fetches live weather data from OpenWeather API.

---

##  Technologies Used

- **Django** (Backend framework for handling requests and rendering templates)
- **HTML5 & CSS3** (Frontend design and animations)
- **Font Awesome** (Icons for weather conditions)
- **OpenWeather API** (Fetches weather data)

---

##  Installation & Setup

Follow these steps to run the project on your local machine:

###  1. Clone the Repository

```bash
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
```

###  2. Create a Virtual Environment

```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
```

###  3. Install Dependencies

```bash
    pip install -r requirements.txt
```

###  4. Set Up API Key

1. Sign up on [OpenWeather API](https://openweathermap.org/api) and generate an API key.
2. Create a `.env` file in the project's root directory and add:

```env
    OPENWEATHER_API_KEY=your_api_key_here
```

###  5. Apply Migrations

```bash
    python manage.py migrate
```

###  6. Start the Django Development Server

```bash
    python manage.py runserver
```

Now, open your browser and navigate to:

```
    http://127.0.0.1:8000/
```

---

## Project Structure

```plaintext
weather-app/
│-- weather/             # Django app
│   │-- static/weather/  # CSS, Images
│   │-- templates/weather/
│   │   │-- home.html
│   │   │-- location_detail.html
│   │-- views.py         # Handles weather API requests
│   │-- urls.py          # URL routing
│   │-- utils.py         # Fetches weather data
│-- manage.py
│-- requirements.txt
│-- .env                 # API Key storage
│-- README.md
```

---

##  How It Works

1. **User searches for a city.**
2. **Django fetches data** from the OpenWeather API.
3. **The template renders** the current weather details.
4. **Weather icons and animations** make the UI engaging.
5. **Users can navigate back** to the homepage using a button.


##  Future Enhancements

 1 **7-Day Forecast** feature.
 2 **Hourly weather updates**.
 3 **User authentication for saved locations**.
 4 **Dark mode support**.

##  Author

Developed by **[Subhash Chandra](https://github.com/subbu199921)**.

If you like this project, feel free to ⭐ the repo!

