import flet as ft

# MODELO DE DATOS

productos = [
    {"id": 1, "nombre": "Totoro", "descripcion": "Peluche de 1 metro de altura, suave y esonjoso.", "precio": 1000, "ruta_imagen": "1.jpg"},
    {"id": 2, "nombre": "Gatitos", "descripcion": "Hermosos llaveros de gatitos", "precio": 100, "ruta_imagen": "2.webp"},
    {"id": 3, "nombre": "Libreta", "descripcion": "LIbreta en forma de lapiza, rayada.", "precio": 50, "ruta_imagen": "3.webp"},
    {"id": 4, "nombre": "Capibara", "descripcion":"Mochila de capibara con flor.", "precio": 200, "ruta_imagen": "4.jpg"},
    {"id": 5, "nombre": "Nimona", "descripcion": "Funko de Nimona.", "precio": 500, "ruta_imagen": "5.jpg"},
    {"id": 6, "nombre": "Sailor Moon", "descripcion": "Set de 6 mangas de Sailor Moon.", "precio": 2000, "ruta_imagen": "6.webp"},
    {"id": 7, "nombre": "Cry baby", "descripcion": "Perfume original, sellado.", "precio": 3000, "ruta_imagen": "7.webp"},
    {"id": 8, "nombre": "Van Gogh", "descripcion": "Set de notas adhesivas Noche estrellada.", "precio": 100, "ruta_imagen": "8.webp"},
]

# COMPONENTE REUTILIZABLE

class ProductoCard(ft.Container):

    def __init__(self, producto):

        super().__init__()

        self.width = 250
        self.padding = 10
        self.border_radius = 15
        self.bgcolor = ft.Colors.WHITE

        self.content = ft.Column(
            spacing=8,
            controls=[

                # Imagen
                ft.Image(
                    src=producto["ruta_imagen"],
                    width=230,
                    height=150,
                    fit="cover"
                ),

                # Nombre
                ft.Text(
                    producto["nombre"],
                    size=18,
                    color=ft.Colors.BLACK,
                    weight="bold"
                ),

                # Descripción
                ft.Text(
                    producto["descripcion"],
                    size=12,
                    color=ft.Colors.GREY_700
                ),

                # Precio
                ft.Text(
                    f"${producto['precio']}",
                    size=16,
                    weight="bold",
                    color=ft.Colors.GREEN
                ),

                # Barra de acciones
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.Icons.FAVORITE),
                        ft.ElevatedButton(
                            "Agregar",
                            icon=ft.Icons.SHOPPING_CART
                        )
                    ]
                )
            ]
        )

# INTERFAZ PRINCIPAL

def main(page: ft.Page):

    page.title = "Marketplace"
    page.bgcolor = ft.Colors.BLUE_50
    page.scroll = "auto"

    header = ft.Text(
        "🛒 BAZARE",
        color=ft.Colors.PURPLE,
        size=30,
        weight="bold"
        
    )

    tarjetas = []

    for producto in productos:
        tarjetas.append(ProductoCard(producto))

    catalogo = ft.Row(
        controls=tarjetas,
        wrap=True,
        spacing=20
    )

    page.add(
        header,
        catalogo
    )


ft.app(
    target=main,
    assets_dir="imagenes"
)