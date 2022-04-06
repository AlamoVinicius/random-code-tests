
import easyocr
reader = easyocr.Reader(['PT'])
resultado = reader.readtext('placas-de-sinalizacao-de-transito-21.jpg')
