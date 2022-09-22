estudiantes = {"123": {"Nombre": "Antony",
                       "Apellido": "Botello", "Telefono": "3135279210", "Curso": 5}}
opcion = None


def marco(titulo: str, contenido: str = ""):
    cantidad = (len(titulo)+30)
    print("#"*cantidad)
    print(f"####           {titulo}           ####")
    print("#"*cantidad)
    if len(contenido)>0:
        print("\n"+contenido+f"\n"+"#"*cantidad)


def agregar(id: str, nombre: str, apellido: str, telefono: str,  curso: int):
    """Función para agregar estudiantes

    Args:
        id (str): _description_
        nombre (str): _description_
        apellido (str): _description_
        telefono (str): _description_
        curso (int): _description_
    """
    estudiante = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Telefono": telefono,
        "Curso": curso
    }
    estudiantes.update({id: estudiante})


def mostrar(id: str):
    contenido = f"ID: {id}\n"
    for key in estudiantes[id]:
        valor=estudiantes[id][key]
        contenido += f"{key}: {valor}\n"
    marco(f"Estudiante {id}", contenido)


def actualizar(id:str, campo:str, info):
    if campo in estudiantes[id]:
        estudiantes[id][campo] = info
    else:
        print("El campo no existe.")


def eliminar(id):
    seguro = input("Esta seguro de eliminar (Y/N)\n")
    if seguro == "Y" or seguro == "y":
        aux = estudiantes.pop(id)
        nombre = aux["Nombre"]
        print(f"El estudiante {nombre} se eliminó correctamente.")
    else:
        print(f"Eliminación cancelada.")


opciones = ""
while opcion != "5":
    opciones += "1. Ingresar nuevo Estudiante.\n"
    opciones += "2. Consultar estudiantes registrados.\n"
    opciones += "3. Editar estudiantes registrados.\n"
    opciones += "4. Eliminar un Estudiante.\n"
    opciones += "5. Salir\n"
    marco("Menú Estudiantes", opciones)

    opcion = input("Digite la opción:\n")

    if opcion == "1":
        marco("Agregar Estudiantes")

        agregar(
            input("Digite el documento\n"),
            input("Digite el Nombre\n").capitalize,
            input("Digite el Apellido\n").capitalize,
            input("Digite el Teléfono\n"),
            int(input("Digite el Curso\n"))
        )
    if opcion == "2":
        sub = None
        while sub != "3":
            marco("Listar Estudiantes")
            print("\n1. Listar todos.")
            print("2. Buscar por documento.")
            print("3. Volver")
            sub = input("Digite la opción:\n")
            if sub == "1":
                for estudiante in estudiantes:
                    mostrar(estudiante)
            elif sub == "2":
                mostrar(input("Digite el documento\n"))
    if opcion == "3":
        marco("Actualizar Estudiantes")
        actualizar(input("Digite el estudiante.\n"),
                   input("Digite el nombre del campo.\n").capitalize,
                   input("Digite la actualización.\n").capitalize)
    if opcion == "4":
        marco("Eliminar Estudiantes")
        eliminar(input("Digite el estudiante.\n"))
else:
    print("Hasta la proxima!")
