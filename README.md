# 🔗 URL Shortener

A simple URL shortener with Flask while learning python. I built this to understand how web frameworks work under the hood, from request routing to data storage.

## 📖 About the project

This URL shortener was my practical experience with:

- Building a simple REST API
- Generating unique identifiers
- HTTP redirection
- Integrating frontend (HTML/CSS/JS) with backend (Flask)

## ⚙️ How it works

1. The user pastes a long URL into the input field
2. The backend generates a random 6-character code
3. The `code → original URL` relationship is stored
4. When the short link is accessed, the user is automatically redirected to the original URL

## 🛠️ Tech stack

- Python 3 - main language
- Flask - micro web framework for backend routes and logic
- HTML, CSS and JavaScript - interface and asynchronous communication with the API (fetch)

## 🚀 How to run locally

```bash
# Clone the repository
git clone https://github.com/PedroAlbelo/url-shortener-flask.git
cd url-shortener-flask

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## 📚 What I learned

- How to structure a Flask application (routes, templates, requests)
- The difference between GET and POST requests
- How `venv` isolates dependencies between Python projects
- Asynchronous communication between frontend and backend using `fetch` and JSON
- Debugging real environment issues (paths, unsynced servers, browser caching)

## 🔮 Next steps

- [ ] Persist links in a database (SQLite) instead of memory
- [ ] Add click counter per link
- [ ] Deploy to production (Render/Railway)
- [ ] URL validation

--------------------------

Built by [Pedro Albelo](https://github.com/PedroAlbelo) as part of my software development studies.