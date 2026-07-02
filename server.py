from pathlib import Path
from flask import Flask, abort
from waitress import serve

folder = Path(__file__).parent / "sites"
app = Flask(__name__, template_folder="sites")

def processline(line):
    debug = 1
    print(f"Processing line: {line} at number {debug}")
    debug += 1
    start = line.find("[") + 1
    end = line.find("]")
    if start > 0 and end > start:
        result = line[start:end]

    tag = result.lower()

    start = line.find("{") + 1
    end = line.rfind("}")
    if start > 0 and end > start:
        result = line[start:end]
    content = result

    if tag == "header":
        lines.append(f"<h1>{content}</h1>")
    elif tag == "body":
        lines.append(f"<p>{content}</p>")
    elif tag == "chapter":
        lines.append(f"<h2>{content}</h2>")
    elif tag == "section":
        lines.append(f"<h3>{content}</h3>")
    elif tag == "footer":
        lines.append(f"<footer><small>{content}</small></footer>")
    elif tag == "link":
        lines.append(f'<a href="{content}" target="_blank" rel="noopener noreferrer">{content}</a>')
    elif tag == "pagelink":
        lines.append(f'<p><a href="/{content}">{content}</a></p>')

for file in folder.glob("*.sw"):
    lines = []
    print(f"Found file: {file.name}")
    fileedit = ((file.with_suffix(".html")).name)
    with open(f"sites/{fileedit}", "a") as f:
        debug = 1
        for line in file.read_text().splitlines():
            processline (line)
            lines.append("\n")
            
    with open(f"sites/{fileedit}", "w") as f:
        f.write("<html><body>")
        f.write("".join(lines))
        f.write("</body></html>")

@app.route("/")
def home():
    file_path = folder / 'home.html'
    if not file_path.exists():
        abort(404)
    return file_path.read_text()

@app.route("/<page>")
def serve_page(page):
    file_path = folder / f"{page}.html"

    if not file_path.exists():
        abort(404)

    return file_path.read_text()

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)