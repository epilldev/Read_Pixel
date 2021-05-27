# Importação da biblioteca que irá fazer o reconhecimento da imagem no código
# É utilizado também um modulo para a tecnologia OCR

import pytesseract as tesse
import numpy as np
import tkinter.filedialog as tkf
from PIL import Image
img = Image.open("~/Syngenta.bmp") # Carregamento da Imagem no código.
pixels = img.convert('RGB').getcolors() # Gera a lista de cores e quantidade de pixel de cada cor
print(pixels) # Imprime a lista gerada

# Agora será a tentativa para leitura da mensagem secreta

print("PRIMEIRA TENTATIVA")

tesse.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Utilizando a tecnologia OCR
texto = tesse.image_to_string(Image.open("~/Syngenta.bmp")) # Convertendo a mensagem em String
print(texto) # Imprime a mensagem gerada


print("SEGUNDA TENTATIVA")

# Forma diferente de pegar a imagem na pasta, em vez de passar o diretório
root = tkf.Tk()
root.withdraw()
img_file = tkf.askopenfilename(
    parent=root, title="Select a BMP file", filetypes=(("BMP files", "*.bmp"),)
)
img = np.array(Image.open(img_file)) # Carregando a imagem novamente
shp = img.shape   # Carregar as propriedades da imagem
the_bytes = tesse.image_to_string(shp)


print(the_bytes)