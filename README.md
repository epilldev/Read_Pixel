# Read Pixel - OCR e Processamento de Imagens BMP

Projeto experimental desenvolvido em Python para leitura de imagens BMP, análise de pixels RGB e extração de texto utilizando OCR com Tesseract.

---

## Stack Utilizada

* Python 3
* Pytesseract
* Tesseract OCR
* Pillow (PIL)
* NumPy
* Tkinter

---

## Conceitos Aplicados

* OCR (Optical Character Recognition)
* Processamento de Imagens
* Manipulação de Pixels RGB
* Conversão de Imagens para Arrays NumPy
* Automação de Leitura de Texto em Imagens BMP

---

## Funcionalidades

* Leitura de imagens BMP
* Análise de pixels RGB
* Extração de texto via OCR
* Seleção dinâmica de arquivos
* Conversão de imagem para estrutura NumPy

---

## Execução

Instalação das dependências:

```bash id="jlwm4p"
pip install pytesseract pillow numpy
```

Execução:

```bash id="2jlwm4"
python main.py
```

---

## Dependência Externa

Necessário instalar o Tesseract OCR:

https://github.com/UB-Mannheim/tesseract/wiki

Exemplo de configuração no Windows:

```python id="3jlwm4"
tesse.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## Objetivo

Projeto desenvolvido para estudos de:

* OCR
* Processamento de Imagens
* Manipulação de Pixels
* Automação com Python
