import os
import sys
from glob import glob
from docx import Document
from docx.shared import Inches, Pt

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
elif __file__:
    app_path = os.path.dirname(__file__)
os.chdir(app_path)

types = [ '**/*.md', '**/*.toml', '**/*.py', '**/*.htm', '**/*.html', '**/*.csv', '**/*.json', '**/*.xml', '**/*.png', '**/*.jpg' ]
files = []

for t in types: files.extend(glob(t, recursive=True))
files = sorted(files)

document = Document()

for file in files:
    if 'build' in file or 'dist' in file: continue
    print(file)
    document.add_heading(file, 0)
    if '.png' in file or '.jpg' in file:
        document.add_picture(file, width=Inches(6))
    else:
        with open(file) as f:
            document.add_paragraph(f.read()).style.font.size = Pt(9)
    document.add_page_break()

document.save('bundle.docx')