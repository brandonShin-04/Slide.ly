import fitz
from transformers import BartTokenizer, BartForConditionalGeneration
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text +=page.get_text()
    print("this is in the extract text function")
    print(text)
    return text


tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

pdf_path = "C:\\Users\\jacob\\Downloads\\ECE333T - Intro to Conclusion (full draft).pdf"
input_text = extract_text_from_pdf(pdf_path)
size_of_text = len(input_text)
prompt = "Please summarize the following text into bullet points:\n\n" + input_text

inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=1024)
print("\nTokens: ", tokenizer.convert_ids_to_tokens(inputs[0]))

summary_ids = model.generate(inputs, max_length= size_of_text, min_length=50, length_penalty=2.0, num_beams=7, early_stopping=True)

summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Bullet Points")
print(summary)