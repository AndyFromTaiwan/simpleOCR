from os import listdir
from os.path import join, splitext
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


# Configs
img_path = 'image'
txt_path = 'txt'
pdf_path = 'pdf'
language = 'eng'
GEN_PDF = True


files = listdir(img_path)

for f in files:
    print('Starts an OCR on', f)
    try: 
        (filename, extension) = splitext(f)
        img = Image.open(join(img_path, f))

        # Simple image to string
        content = pytesseract.image_to_string(img, lang=language)
        txt = join(txt_path, filename+'.txt')
        with open(txt, 'w') as tf:
            tf.write(content)
        print('Successfully wrote the converted text in', txt)

        # Get a searchable PDF
        if GEN_PDF:
            pdf = join(pdf_path, filename+'.pdf')
            content = pytesseract.image_to_pdf_or_hocr(img, lang=language, extension='pdf')
            with open(pdf, 'w+b') as pf:
                pf.write(content) # pdf type is bytes by default
            print('Successfully wrote the converted pdf in', pdf)

    except Exception as e:
        print("Fail!", e.__class__, "occurred:")
        print(e)
    print()

