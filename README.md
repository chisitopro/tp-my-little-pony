# 🦄 Friendship Bazaar

**Friendship Bazaar** es una aplicación web de e-commerce desarrollada con **Python** y **Streamlit**, ambientada en el universo de *My Little Pony*. Simula un marketplace de Equestria donde se compran, venden e intercambian artefactos mágicos, reliquias históricas, productos artesanales y objetos icónicos de la serie.

---

## 📋 Descripción general

La aplicación presenta un catálogo de productos cargados en memoria (sin base de datos externa), cada uno identificado por una **clave única** (`idProducto`). Permite explorar el catálogo mediante tarjetas visuales, filtrar por categoría y rareza, buscar por nombre o personaje, y ver el detalle completo de cada objeto en una vista dedicada.

---

## ✨ Funcionalidades principales

- 🛍️ **Catálogo visual**: los productos se muestran en tarjetas organizadas en una grilla de 3 columnas.
- 🔍 **Filtros laterales**: por categoría, por rareza y por texto libre (nombre o personaje asociado).
- 🪪 **Clave única destacada**: el `idProducto` se muestra como una insignia (badge) visualmente diferenciada en cada tarjeta y en el detalle.
- 📖 **Vista de detalle**: al seleccionar un producto se despliegan todos sus atributos (origen, personaje, nivel de magia, rareza, descripción, precio).
- 🛒 **Acciones simuladas**: botones de "Comprar ahora" y "Proponer intercambio" (simulan la acción mostrando un mensaje de confirmación; no procesan pagos reales).
- 🎨 **Diseño temático**: colores y estilos personalizados con CSS embebido, inspirados en la estética de Equestria.

---

## 🗂️ Estructura de datos de cada producto

| Campo | Tipo | Descripción |
|---|---|---|
| `idProducto` | str | **Clave principal** única del producto (ej. `FB-COL-CAN-0001`). |
| `nombre` | str | Nombre comercial del objeto. |
| `categoria` | str | Tipo comercial (Coleccionable, Artefacto Mágico, Alimento, Libro Mágico, Reliquia). |
| `rareza` | str | Común, Poco Común, Raro, Épico, Legendario. |
| `origen` | str | Reino o región de Equestria de origen. |
| `personajeAsociado` | str | Personaje canon vinculado al objeto. |
| `nivelMagia` | str | Nulo, Bajo, Medio, Alto, Arcano. |
| `precio` | float | Precio en bits. |
| `descripcion` | str | Historia o detalle del objeto. |
| `imagen` | str | Ruta local a la imagen del producto (ej. `images/smarty_pants.jpg`). |

El catálogo incluye **12 productos de ejemplo**, entre ellos: Smarty Pants, Yovidaphone, Cupcakes de Sugarcube Corner, Sidra de Sweet Apple Acres, libros mágicos y réplicas de los Elementos de la Armonía.

---

## ⚙️ Requisitos

- Python 3.9 o superior
- Streamlit

---

## 📦 Instalación

1. Clona o descarga este repositorio/carpeta.
2. (Opcional pero recomendado) crea un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate      # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

   O directamente:

   ```bash
   pip install streamlit
   ```

---

## ▶️ Ejecución

Desde la carpeta donde se encuentra `app.py`, ejecuta:

```bash
streamlit run app.py
```

Streamlit abrirá automáticamente la aplicación en tu navegador, normalmente en:

```
http://localhost:8501
```

---

## 🖼️ Imágenes de productos

Cada producto tiene un campo `imagen` con la ruta a su archivo local, dentro de la carpeta `images/`.

- Si el archivo existe, se muestra normalmente tanto en la tarjeta del catálogo como en la vista de detalle.
- Si el archivo **no existe**, la aplicación muestra automáticamente un emoji de respaldo (🦄✨) en su lugar, así que la app nunca se rompe por imágenes faltantes.

Para agregar tus propias imágenes:

1. Guarda el archivo dentro de la carpeta `images/` (formatos soportados: `.jpg`, `.jpeg`, `.png`, `.webp`).
2. Usa el nombre de archivo esperado para cada producto (ver `images/README.md` para la lista completa), o bien actualiza el campo `"imagen"` de ese producto en `app.py` si prefieres otro nombre.

---

## 📁 Estructura del proyecto

```
friendship-bazaar/
│
├── app.py              # Aplicación completa (UI + datos + lógica)
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Este archivo
└── images/             # Imágenes locales de los productos
    └── README.md       # Lista de nombres de archivo esperados por producto
```

> Toda la lógica, los estilos y los datos de ejemplo están contenidos en un único archivo (`app.py`) para mantener la app simple, portable y fácil de ejecutar.

---

## 🚧 Limitaciones actuales (alcance de esta versión)

- Los datos viven **en memoria** (lista de diccionarios en Python); al reiniciar la app, el catálogo vuelve a su estado original.
- No hay autenticación de usuarios ni persistencia real de compras/intercambios.
- Los botones de "Comprar" e "Intercambiar" son **simulaciones** (no se conectan a una pasarela de pago ni a una base de datos).

## 🔮 Posibles mejoras futuras

- Conexión a una base de datos real (SQLite, PostgreSQL) para persistir productos, usuarios y transacciones.
- Sistema de autenticación de vendedores y compradores.
- Carrito de compras y checkout funcional.
- Subida de imágenes reales por producto.
- Módulo de subastas para reliquias legendarias.

---

## 🐴 Créditos temáticos

Todos los nombres de productos, personajes y lugares pertenecen al universo de *My Little Pony*, utilizados aquí únicamente con fines educativos/demostrativos de diseño de software.
