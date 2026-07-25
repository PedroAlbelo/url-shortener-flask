from flask import Flask, request, redirect, jsonify, render_template
import random
import string

app = Flask(__name__)

# Temporary database, short code -> original URL
urls = {}

def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "No URL was provided"}), 400

    code = generate_code()
    while code in urls:
        code = generate_code()

    urls[code] = original_url

    return jsonify({
        "original_url": original_url,
        "short_url": f"http://127.0.0.1:5000/{code}"
    })

@app.route("/history")
def history():
    return jsonify(urls)

@app.route("/<code>")
def redirect_to_url(code):
    original_url = urls.get(code)
    if original_url:
        return redirect(original_url)
    return "Link not found", 404

if __name__ == "__main__":
    app.run(debug=True)