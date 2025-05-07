# 🌐 PolyGlot Playground

**PolyGlot Playground** is an interactive, multi-language code runner that uses Docker containers to safely execute example programs written in different programming languages — all from a simple web interface.

This is perfect for learning, demonstrating, or comparing how different languages solve the same problem.

---

## 🚀 Features

| Feature                              | Description |
|-------------------------------------|-------------|
| 🌐 **Web Interface**                | Built with plain HTML/CSS; lets you select a language and run code with one click |
| 🧠 **Multi-Language Support**       | Supports Python (working), and planned support for C, C++, Java, and Haskell |
| 🐳 **Docker Isolation**             | Each language runs in its own isolated Docker container for safety and simplicity |
| 🔁 **Live Output Display**          | See the output of the program directly in the browser |
| 🧩 **Modular Structure**            | Easy to add more languages or algorithms by editing just two files |
| 🔧 **Flask Backend API**            | Lightweight Python Flask server routes frontend calls to Docker commands |

---

## 📁 Project Structure

```plaintext
polyglot-playground/
├── backend/               # Flask server
│   └── app.py             # Main backend logic, routes, and Docker interaction
├── frontend/              # Web interface
│   └── index.html         # Simple UI with dropdown and output display
├── runners/               # Language-specific code folders
│   └── python/
│       └── main.py        # Python program to be run in Docker
├── Dockerfiles/           # Dockerfile for each language
│   └── Dockerfile.python  # Builds the Docker image for Python
├── venv/                  # Python virtual environment (optional)
└── README.md              # Project description and usage
```


## 🧪 How It Works

1. You select a language from the dropdown menu.
2. The browser sends a request to the Flask backend (`/run?lang=python`).
3. Flask runs the corresponding Docker container (e.g., `polyglot-python`).
4. Docker runs the code and returns the output.
5. Output is shown live in the browser.

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/polyglot-playground.git
cd polyglot-playground
```
### 2. Create & Activate Virtual Environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Flask

```bash
pip install flask
```
### 4. Build the Python Docker Image

```bash
docker build -t polyglot-python -f Dockerfiles/Dockerfile.python .
```
### 5. Run the Flask Server

```bash
python backend/app.py
```

### 6. Open in Browser
Visit: http://localhost:5000