# PokeCLI 🎮

Una aplicación de línea de comandos interactiva para consultar información sobre Pokémon, sus movimientos y tipos utilizando la PokeAPI.

## 📋 Características

- **Búsqueda de Pokémon**: Busca Pokémon por nombre o ID
- **Visualización de GIFs**: Muestra animaciones de los Pokémon en la terminal
- **Información detallada**: Consulta habilidades, experiencia base, dimensiones, tipos y estadísticas
- **Búsqueda de movimientos**: Explora movimientos por nombre o tipo
- **Lista de tipos**: Visualiza todos los tipos de Pokémon disponibles
- **Interfaz colorida**: Menús interactivos con colores para mejor experiencia de usuario

## 🔧 Requisitos

- Python 3.7 o superior
- Conexión a internet (para consultar la PokeAPI)
- Terminal compatible con colores ANSI y visualización de imágenes

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/patient-c/pokecli-py
cd pokecli-py
```
2. Crear entorno virtual y activarlo ( Opcional pero recomendado )
```bash
python -m venv venv
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

O instala manualmente:
```bash
pip install pokebase colorama art term-image pillow keyboard
```

## 🚀 Uso

Ejecuta el script principal:
```bash
python pokecli.py
```

## Screenshot

![title](screenshot.png)

## Menú Principal

1. **Buscar Pokemon por nombre o id y ver atributos**
   - Ingresa el nombre o ID del Pokémon
   - Visualiza su animación GIF
   - Consulta habilidades, experiencia, dimensiones, tipos y estadísticas

2. **Listar tipos de Pokemon**
   - Muestra todos los tipos disponibles

3. **Buscar movimientos**
   - Busca movimientos por nombre
   - Lista movimientos por tipo
   - Consulta qué Pokémon pueden aprender cada movimiento

4. **Salir**

## 📂 Estructura del Proyecto

```
pokecli/
├── pokecli.py              # Script principal
├── requirements.txt     # Dependencias del proyecto
├── showdown/            # Carpeta con GIFs de Pokémon
│   ├── 1.gif
│   ├── 2.gif
│   └── ...
├── README.md
└── LICENSE
```

## 🎨 Ejemplo de Uso

```
Ingrese el nombre o id del pokemon a buscar: pikachu

[Animación GIF de Pikachu]

Opciones de Pokemon:
1. Habilidades
2. Experiencia Base
3. Longitud y peso
4. Tipo
5. Estadisticas
6. Salir al menu principal
```

## 🌐 Fuentes de Datos

- **PokeAPI**: Todos los datos de Pokémon provienen de [PokeAPI](https://pokeapi.co/)
- **GIFs**: Los sprites animados son propiedad de sus respectivos creadores y se utilizan con fines educativos

## 📝 Notas

- Asegúrate de tener la carpeta `showdown` con los GIFs en el mismo directorio que el script
- Algunos Pokémon pueden no tener traducción al español en ciertos atributos
- La aplicación requiere una terminal compatible con colores ANSI

## 🐛 Problemas Conocidos

- Si un movimiento no tiene nombre en español, se muestra solo en inglés
- Requiere conexión a internet para funcionar

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

patient-c - [@patient-c](https://github.com/patient-c)

## 🙏 Agradecimientos

- [PokeAPI](https://pokeapi.co/) por proporcionar los datos
- [Pokebase](https://github.com/PokeAPI/pokebase) por el wrapper de Python
- Comunidad de Pokémon Showdown por los sprites animados

---

## 📋 Dependencias

El proyecto utiliza las siguientes bibliotecas (ver `requirements.txt`):

- **pokebase**: Wrapper de Python para PokeAPI
- **colorama**: Colores ANSI para terminal
- **art**: Generación de arte ASCII
- **term-image**: Visualización de imágenes en terminal
- **pillow**: Procesamiento de imágenes
- **keyboard**: Captura de eventos de teclado
- **requests**: Cliente HTTP
