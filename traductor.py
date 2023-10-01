def principal():
    while True:
        print()
        print("\n1. Agregar traducción nueva")
        print("2. Traductor")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_traduccion()
        elif opcion == '2':
            traducir()
        elif opcion == '3':
            print("El programa a finalizado, vuelva pronto")
            break
        else:
            print("Opción no válida. Por favor inténtelo nuevamnete")

def cargar_diccionario():
    try:
        with open('EN-ES.txt', 'r') as archivo:
            return dict(line.strip().split('=') for line in archivo)
    except FileNotFoundError:
        return {}

def agregar_traduccion():
    palabra_en_ingles = input("Ingresa la palabra en inglés: ")
    palabra_en_español = input("Ingresa la traducción al español: ")

    diccionario = cargar_diccionario()
    diccionario[palabra_en_ingles] = palabra_en_español

    with open('EN-ES.txt', 'w') as archivo:
        for palabra, traduccion in diccionario.items():
            archivo.write(f'{palabra}={traduccion}\n')
    
    print("La palabra se ha agregado exitosamente")

def traducir():
    modo, palabra = input("Ingrese el modo (EN-ES o ES-EN) y la palabra (por ejemplo, ES-EN gato): ").split()

    diccionario = cargar_diccionario()

    if modo == 'EN-ES':
        traduccion = diccionario.get(palabra, 'No se encontró la traducción')
    elif modo == 'ES-EN':
        traduccion = next((key for key, value in diccionario.items() if value == palabra), 'No se encontró la traducción')
    else:
        traduccion = 'Modo no válido \n'
    
    print(f'{modo} {palabra} --> {traduccion}')

principal()

