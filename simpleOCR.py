from os import listdir
from os.path import join, splitext
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


# Configs
img_path = 'image'
GEN_TXT = True
GEN_PDF = True
txt_path = 'txt'
pdf_path = 'pdf'
language = 'eng'
"""
English: 'eng'
Simplified Chinese: 'chi_sim'
Traditional Chinese: 'chi_tra'
Bilingual: "chi_tra+eng"
"""

def run_ocr(f):
    (filename, extension) = splitext(f)
    # Skips non-image files
    if extension == '':
        return

    print('Starts an OCR on', f)
    try:
        img = Image.open(join(img_path, f))

        # Simple image to string
        if GEN_TXT:
            content = pytesseract.image_to_string(img, lang=language)
            txt = join(txt_path, filename+'.txt')
            with open(txt, 'w') as tf:
                tf.write(content)
            print('Successfully wrote the extracted text in', txt)

        # Get a searchable PDF
        if GEN_PDF:
            content = pytesseract.image_to_pdf_or_hocr(img, lang=language, extension='pdf')
            pdf = join(pdf_path, filename+'.pdf')
            with open(pdf, 'w+b') as pf:
                pf.write(content) # pdf type is bytes by default
            print('Successfully wrote the converted pdf in', pdf)

    except Exception as e:
        print("Fail!", e.__class__, "occurred:")
        print(e)
    print()


files = listdir(img_path)

for f in files:
    run_ocr(f)

