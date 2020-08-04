from os import listdir
from os.path import join, splitext
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


img_path = 'image'
text_path = 'text'
language = 'eng'

files = listdir(img_path)

for f in files:
    print('Starts an OCR on', f)
    try: 
        (filename, extension) = splitext(f)
        img = Image.open(join(img_path, f))
        content = pytesseract.image_to_string(img, lang=language)

        text = join(text_path, filename+'.txt')
        tf = open(text, "w")
        tf.write(content)
        tf.close()
        print('Successfully wrote the converted text in', text)
    except Exception as e:
        print("Fail!", e.__class__, "occurred:")
        print(e)
    print()

