# URL Shortener Website

A simple URL shortener web application built with Python and Django. This application allows users to generate shortened URLs and manage them through a user-friendly interface.

## Features

- Shorten long URLs
- Redirect shortened URLs to original destinations
- Track time used
- Simple and clean user interface

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
  
## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Japasche/URL_Shortener.git
   cd URL_Shortener
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install the project dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   You need to run the Django migrations to set up the database.
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   Start the Django development server to run the application locally.
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your browser and visit `http://localhost:8000` to use the URL shortener.

## Usage

Once the server is running, you can:

- Enter a long URL to generate a shortened version.
- Copy the shortened URL and share it.
- Navigate to the shortened URL to be redirected to the original long URL.
  - To do this add the shortened URL to the end of this: http://localhost:8000/

### Example

```text
Original URL: https://www.example.com/some/long/url/path
Shortened URL: http://localhost:8000/AnjHFe
```
## Technologies

- **Django**: High-level Python web framework
- **SQLite**: Lightweight database for local development
- **Bootstrap**: CSS framework for responsive UI design
