categoria=0
reporteJson="categorias.json"
categoriaLibro={}


def menuCategorias():
    while True:
     print("[1]- agregar categoria")
     print("[2]-editar categoria")
     print("[3] eliminar categoria")
     print("[4] buscar categoria")
     print("[5]- volver")
     
     if categoria == 1:
      with open ("biblioteca.json",mode="w") as reporteJson: 
       agregarCategoria={"CategoriaID",CategoriaID 
                         }
