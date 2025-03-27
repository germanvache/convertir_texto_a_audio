from gtts import gTTS

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()
    return texto

def convertir_a_audio(texto, nombre_archivo):
    # Crear objeto gTTS
    tts = gTTS(text=texto, lang='es')
    
    # Guardar el archivo de audio
    tts.save(nombre_archivo)

def main():
    # Ruta del archivo de texto que deseas convertir
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    
    # Leer el contenido del archivo
    texto = leer_archivo(ruta_archivo)
    
    # Convertir el texto a audio
    nombre_archivo = "audio_output.mp3"  # Puedes cambiar el nombre si lo deseas
    convertir_a_audio(texto, nombre_archivo)
    
    print(f"El contenido del archivo ha sido convertido a audio y guardado como '{nombre_archivo}'.")

if __name__ == "__main__":
    main()
