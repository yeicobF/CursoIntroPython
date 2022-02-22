def main():
    file = "config.txt"
    try:
        configuration = open(file)
    except FileNotFoundError:
        print(f"No se encontró el archivo {file}")
    except IsADirectoryError:
        print(f"Se encontró {file}, pero es un directorio. No se pudo leer.")
    except PermissionError:
        print(f"No tienes nos permisos necesarios para abrir {file}")
    # Cuando los errores son de una naturaleza similar y no es necesario
    # controlarlos individualmente, puedes agrupar las excepciones como una
    # usando paréntesis en la línea `except`.
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()
