def main():
    file = "config.txt"
    try:
        configuration = open(file)
    except FileNotFoundError:
        print(f"No se encontró el archivo {file}")
    except IsADirectoryError:
        print(f"Se encontró {file}, pero es un directorio. No se pudo leer.")

if __name__ == '__main__':
    main()
