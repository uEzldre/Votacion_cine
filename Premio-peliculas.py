Info_peliculas = []
categorias = ["1: Ficción", "2: Acción", "3: Romance", "4: Historia", "5: Documental", "6: Banda Sonora"]
Votos = 0
def registrar_peliculas():
    while True:
        nombre = input("Ingrese el nombre de la pelicula (deje vacio para salir del proceso):\n").capitalize().strip()
        if nombre == "":
            break
        ya_registrada = any(p["Titulo de la pelicula"] == nombre for p in Info_peliculas)
        if ya_registrada:
            print("La pelicula ya está registrada")
            break
        

        while True:
            print("\tCategorias:")
            for cate in categorias:
                print(cate)    
            try:
                categoria = int(input("Elija una categoria:\n"))
                if categoria < 1 or categoria > len(categorias):
                    raise IndexError("El número ingresado está fuera del rango permitido.")
                else:
                    print("Categoria seleccionada:", categorias[categoria-1])
                    break
            except ValueError:
                print("caracter invalido, ingrese caracteres numericos enteros")
                continue
        pelis = {
            "Titulo de la pelicula": nombre,
            "Categoria a la que se nomina": categorias[categoria-1],
            "Votos": 0
        }
        Info_peliculas.append(pelis)

def dar_votos():
    if not Info_peliculas:
        print("No hay peliculas Para votar en este momento")
        return
    for i, r in enumerate(Info_peliculas, 1):
        print(f"#{i}) Pelicula: {r['Titulo de la pelicula']}\nCategoria: {r['Categoria a la que se nomina']} \nVotos: {r['Votos']}")
    try:
        dar_votos = int(input("Ingrese el numero de pelcula que quiere votar:\n"))
        if 1 <= dar_votos <= len(Info_peliculas):
            Info_peliculas[dar_votos - 1]["Votos"] += 1
            print("Voto registrado para:",Info_peliculas[dar_votos - 1]['Titulo de la pelicula'] )
        else:
            print("Numero fuera de rango")
    except ValueError:
        print("Entrada inválida, Debe ingresar un número")

def mostrar_ganador():
    if not Info_peliculas:
        print("No hay peliculas nominadas")
        return

    print("\nPeliculas ordenadas por votos (mayor a menor):")
    ordenados = sorted(Info_peliculas, key=lambda x: x['Votos'], reverse=True)

    for p in ordenados:
        print(f"- {p['Titulo de la pelicula']}\nCategoría: {p['Categoria a la que se nomina']}\nVotos: {p['Votos']}")

def menu():
    while True:
        try:
            print("\n\tRegistro de peliculas\n1. Registrar nueva pelicula\n2. dar votos a una pelicula\n3. Mostrar ganador\n4. Salir")
            opcion = input("Selecciona una opción:\n").strip()

            if opcion == "1":
                registrar_peliculas()
            elif opcion == "2":
                dar_votos()
            elif opcion == "3":
                mostrar_ganador()
            elif opcion == "4":
                print("Terminando sesión")
                break
            else:
                print("opción invalida")
        except ValueError:
            print("Ingrese una opción numerica (1-4)")
menu()