from flask import Flask


class State:
    loading = True


s = State()
app = Flask(__name__)


@app.route("/")
def hello():
    return f"""
    <!doctype html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Dishwasher Status</title>
                <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🧽</text></svg>">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">            </head>
            <body>
                <h2>Dishwasher is <button class="btn-large" onClick="change()"> {"loading" if s.loading else "unloading"}</button></h1>
                <script>
                    function change() {{ 
                        fetch("./change").then(function(response) {{
                            return response.json();
                        }}).then(function(data) {{
                            location.reload();
                        }}).catch(function() {{
                            console.log("Booo");
                        }});
                    }}
                </script>
            </body>
        </html>
    """


@app.route("/change", methods=["GET"])
def change():
    s.loading = not s.loading
    return "200"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
