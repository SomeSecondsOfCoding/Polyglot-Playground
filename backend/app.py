from flask import Flask, request, send_file
import subprocess
import os

app = Flask("PolyGlot-Playground")  # Optional: name the app for clarity

@app.route("/run")
def run():
    lang = request.args.get("lang")
    try:
        # Run the corresponding Docker container for the selected language
        output = subprocess.check_output(
            ["docker", "run", f"polyglot-{lang}"],
            stderr=subprocess.STDOUT,
            timeout=5
        )
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/")
def index():
    # Dynamically resolve the absolute path to index.html
    frontend_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../frontend/index.html")
    )
    return send_file(frontend_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)