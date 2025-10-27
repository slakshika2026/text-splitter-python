# splitter.py
# Python script to split a .docx file into 700-word chunks for AI detection
# Requires: pip install python-docx

from docx import Document
import os

# ==== CONFIGURATION ====
input_file = "CriticalReview.docx"   # replace with your file name
output_folder = "chunks"
words_per_chunk = 700

# ==== CREATE OUTPUT FOLDER ====
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ==== READ DOCX FILE ====
doc = Document(input_file)
full_text = []
for para in doc.paragraphs:
    if para.text.strip():
        full_text.append(para.text.strip())

text = " ".join(full_text)
words = text.split()

# ==== SPLIT INTO CHUNKS ====
chunk_count = 0
for i in range(0, len(words), words_per_chunk):
    chunk_words = words[i:i+words_per_chunk]
    chunk_text = " ".join(chunk_words)
    chunk_count += 1
    chunk_file = os.path.join(output_folder, f"chunk_{chunk_count}.txt")
    with open(chunk_file, "w", encoding="utf-8") as f:
        f.write(chunk_text)

print(f"Split {len(words)} words into {chunk_count} chunks.")
print(f"Chunks saved in folder: '{output_folder}'")
