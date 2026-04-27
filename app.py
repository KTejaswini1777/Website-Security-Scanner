from flask import Flask, render_template, request
import requests
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        url = request.form['url']

        try:
            start = time.time()
            response = requests.get(url)
            end = time.time()

            result = {
                "url": url,
                "status": response.status_code,
                "https": url.startswith("https"),
                "response_time": round(end - start, 3),
                "headers": dict(response.headers)
            }

        except Exception as e:
            result = {"error": str(e)}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)