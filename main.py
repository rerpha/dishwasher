from flask import Flask


class State:
    loading = True


s = State()


def generate_html():
    return f"""
    <!doctype html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Dishwasher Status</title>
                <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🧽</text></svg>">
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">        
            </head>
            <body>
                <h1 class="fs-1">Dishwasher is <button class="btn btn-primary btn-lg" onClick="change()"> {"loading" if s.loading else "unloading"}</button></h1>
                <script>
                    function sleep(milliseconds) {{
                        const date = Date.now();
                        let currentDate = null;
                        do {{
                            currentDate = Date.now();
                        }} while (currentDate - date < milliseconds);
                    }}
                    function change() {{ 
                        var xhr = new XMLHttpRequest();
                        xhr.open("GET", "/change", true);
                        xhr.send("");
                        sleep(200);
                        location.reload();
                    }}
                </script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
            </body>
        </html>
    """


app = Flask(__name__)


@app.route("/")
def hello():
    return generate_html()


@app.route("/change", methods=["GET"])
def change():
    s.loading = not s.loading
    return "200"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
