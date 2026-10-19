"""Build index.html (responsive study viewer) from the Markdown notes.

Run after editing any .md file:  python build.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = {
    "law": "01-law-cheat-sheet.md",
    "hirarc": "02-hirarc-bridge-embankment.md",
    "practice": "03-practice-questions.md",
}

data = {key: (HERE / name).read_text(encoding="utf-8") for key, name in NOTES.items()}
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
template = (HERE / "template.html").read_text(encoding="utf-8")
body = template.replace("/*__NOTES__*/", payload)

# The artifact host adds its own <html>/<head>/<body>; a standalone file needs them.
page = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
)
(HERE / "index.html").write_text(page, encoding="utf-8")
(HERE / "artifact.html").write_text(body, encoding="utf-8")
print("Built index.html and artifact.html")
