import streamlit as st
import os

# ============================================================
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Friendship Bazaar",
    page_icon="🦄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# ESTILOS PERSONALIZADOS (CSS)
# ============================================================
st.markdown("""
    <style>
    .main-title {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #ff6fb5, #a86bff, #6fc3ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #888888;
        font-size: 18px;
        margin-top: 0px;
        margin-bottom: 25px;
    }
    .product-card {
        border: 2px solid #e8d5f5;
        border-radius: 16px;
        padding: 18px;
        background: linear-gradient(160deg, #fffaf5, #f5f0ff);
        margin-bottom: 18px;
        box-shadow: 2px 4px 10px rgba(168, 107, 255, 0.15);
    }
    .id-badge {
        display: inline-block;
        background-color: #6a3fb5;
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    .rarity-Legendario {
        background-color: #ffb300; color: #3a2900; padding: 2px 10px;
        border-radius: 12px; font-size: 12px; font-weight: 700;
    }
    .rarity-Épico {
        background-color: #a86bff; color: white; padding: 2px 10px;
        border-radius: 12px; font-size: 12px; font-weight: 700;
    }
    .rarity-Raro {
        background-color: #4fc3f7; color: #002b3a; padding: 2px 10px;
        border-radius: 12px; font-size: 12px; font-weight: 700;
    }
    .rarity-PocoComún {
        background-color: #81c784; color: #0a2e0a; padding: 2px 10px;
        border-radius: 12px; font-size: 12px; font-weight: 700;
    }
    .rarity-Común {
        background-color: #cfd8dc; color: #333333; padding: 2px 10px;
        border-radius: 12px; font-size: 12px; font-weight: 700;
    }
    .price-tag {
        font-size: 22px;
        font-weight: 800;
        color: #6a3fb5;
    }
    .product-name {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 2px;
        color: #3a2a4d;
    }
    .detail-box {
        border: 2px solid #d8b4f8;
        border-radius: 18px;
        padding: 25px;
        background: linear-gradient(160deg, #fff8f0, #f3eaff);
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# REGISTRO PRINCIPAL DE PRODUCTOS (BASE DE DATOS SIMULADA)
# ============================================================
# Clave principal: idProducto -> identificador único, estable e irrepetible
PRODUCTOS = [
    {
        "idProducto": "FB-COL-CAN-0001",
        "nombre": "Smarty Pants",
        "categoria": "Coleccionable",
        "rareza": "Legendario",
        "origen": "Canterlot",
        "personajeAsociado": "Twilight Sparkle",
        "nivelMagia": "Bajo",
        "precio": 1500.00,
        "descripcion": "Muñeco de peluche clásico que perteneció a Twilight Sparkle durante su infancia en Canterlot. "
                        "Pieza histórica y sentimental, muy buscada entre coleccionistas de toda Equestria.",
        "imagen": "images/smarty_pants.jpg"
    },
    {
        "idProducto": "FB-ART-CRY-0002",
        "nombre": "Yovidaphone",
        "categoria": "Artefacto Mágico",
        "rareza": "Épico",
        "origen": "Crystal Empire",
        "personajeAsociado": "Pinkie Pie",
        "nivelMagia": "Medio",
        "precio": 980.00,
        "descripcion": "Curioso instrumento mecánico-mágico capaz de emitir melodías hipnóticas. "
                        "Se dice que su sonido puede alterar el estado de ánimo de quien lo escucha.",
        "imagen": "images/yovidaphone.jpg"
    },
    {
        "idProducto": "FB-ALI-PVL-0003",
        "nombre": "Cupcakes de Sugarcube Corner",
        "categoria": "Alimento",
        "rareza": "Común",
        "origen": "Ponyville",
        "personajeAsociado": "Pinkie Pie",
        "nivelMagia": "Nulo",
        "precio": 45.50,
        "descripcion": "Deliciosos cupcakes horneados con la receta secreta de Sugarcube Corner. "
                        "Perfectos para fiestas, celebraciones o simplemente para alegrar el día.",
        "imagen": "images/cupcakes_sugarcube_corner.jpg"
    },
    {
        "idProducto": "FB-ALI-SAA-0004",
        "nombre": "Sidra de Sweet Apple Acres",
        "categoria": "Alimento",
        "rareza": "Poco Común",
        "origen": "Sweet Apple Acres",
        "personajeAsociado": "Applejack",
        "nivelMagia": "Nulo",
        "precio": 85.00,
        "descripcion": "Sidra de manzana artesanal elaborada con la receta tradicional de la familia Apple. "
                        "Edición especial de temporada de cosecha, muy codiciada en Ponyville.",
        "imagen": "images/sidra_sweet_apple_acres.jpg"
    },
    {
        "idProducto": "FB-LIB-CAN-0005",
        "nombre": "Libro de Hechizos Avanzados de Twilight",
        "categoria": "Libro Mágico",
        "rareza": "Raro",
        "origen": "Canterlot",
        "personajeAsociado": "Twilight Sparkle",
        "nivelMagia": "Alto",
        "precio": 620.00,
        "descripcion": "Tomo antiguo perteneciente a la biblioteca personal de Twilight Sparkle. "
                        "Contiene hechizos de transformación y protección estudiados en la Academia de Celestia.",
        "imagen": "images/libro_hechizos_twilight.jpg"
    },
    {
        "idProducto": "FB-REL-EVE-0006",
        "nombre": "Réplica del Elemento de la Magia",
        "categoria": "Reliquia",
        "rareza": "Legendario",
        "origen": "Bosque Everfree",
        "personajeAsociado": "Twilight Sparkle",
        "nivelMagia": "Arcano",
        "precio": 5200.00,
        "descripcion": "Réplica ceremonial del Elemento de la Magia, uno de los seis Elementos de la Armonía. "
                        "Fabricada con cristal de Equestria y bendecida por unicornios de Canterlot.",
        "imagen": "images/elemento_magia.jpg"
    },
    {
        "idProducto": "FB-REL-EVE-0007",
        "nombre": "Réplica del Elemento de la Honestidad",
        "categoria": "Reliquia",
        "rareza": "Legendario",
        "origen": "Bosque Everfree",
        "personajeAsociado": "Applejack",
        "nivelMagia": "Arcano",
        "precio": 5100.00,
        "descripcion": "Réplica del Elemento de la Honestidad, forjada en honor al espíritu sincero y leal "
                        "que representa a los ponis terrestres de Equestria.",
        "imagen": "images/elemento_honestidad.jpg"
    },
    {
        "idProducto": "FB-ART-CLO-0008",
        "nombre": "Pluma de Pegaso Tornado",
        "categoria": "Artefacto Mágico",
        "rareza": "Raro",
        "origen": "Cloudsdale",
        "personajeAsociado": "Rainbow Dash",
        "nivelMagia": "Medio",
        "precio": 410.00,
        "descripcion": "Pluma desprendida durante un Sonic Rainboom. Conserva una carga residual de energía "
                        "que, según rumores, otorga mayor velocidad a quien la porta.",
        "imagen": "images/pluma_pegaso_tornado.jpg"
    },
    {
        "idProducto": "FB-COL-CRY-0009",
        "nombre": "Corona Conmemorativa del Crystal Empire",
        "categoria": "Coleccionable",
        "rareza": "Épico",
        "origen": "Crystal Empire",
        "personajeAsociado": "Princesa Cadance",
        "nivelMagia": "Alto",
        "precio": 2300.00,
        "descripcion": "Réplica oficial de la corona usada en el Festival del Imperio de Cristal. "
                        "Pieza de colección elaborada con cristal genuino del Imperio.",
        "imagen": "images/corona_crystal_empire.jpg"
    },
    {
        "idProducto": "FB-ART-PVL-0010",
        "nombre": "Poción de Risa de Sugarcube Corner",
        "categoria": "Artefacto Mágico",
        "rareza": "Poco Común",
        "origen": "Ponyville",
        "personajeAsociado": "Pinkie Pie",
        "nivelMagia": "Medio",
        "precio": 150.00,
        "descripcion": "Frasco burbujeante que provoca ataques de risa incontrolables. "
                        "Ideal para fiestas sorpresa, aunque se recomienda usar con moderación.",
        "imagen": "images/pocion_risa.jpg"
    },
    {
        "idProducto": "FB-LIB-SAD-0011",
        "nombre": "Manuscrito de Saddle Arabia",
        "categoria": "Libro Mágico",
        "rareza": "Raro",
        "origen": "Saddle Arabia",
        "personajeAsociado": "Sin asociación directa",
        "nivelMagia": "Alto",
        "precio": 740.00,
        "descripcion": "Antiguo manuscrito de arena encantada proveniente de los desiertos de Saddle Arabia. "
                        "Contiene conocimientos ancestrales sobre conjuros de protección climática.",
        "imagen": "images/manuscrito_saddle_arabia.jpg"
    },
    {
        "idProducto": "FB-COL-CAN-0012",
        "nombre": "Capa de Gala de la Princesa Luna",
        "categoria": "Coleccionable",
        "rareza": "Épico",
        "origen": "Canterlot",
        "personajeAsociado": "Princesa Luna",
        "nivelMagia": "Medio",
        "precio": 1850.00,
        "descripcion": "Capa ceremonial usada en celebraciones nocturnas de Canterlot. "
                        "Confeccionada con tejido estelar que brilla suavemente en la oscuridad.",
        "imagen": "images/capa_gala_luna.jpg"
    },
]

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================
def clase_rareza(rareza: str) -> str:
    """Devuelve la clase CSS correspondiente a cada nivel de rareza."""
    return "rarity-" + rareza.replace(" ", "")


def formato_precio(precio: float) -> str:
    """Formatea el precio en bits."""
    return f"💰 {precio:,.2f} bits"


def mostrar_imagen(ruta_imagen: str, alto_emoji_px: int = 90) -> None:
    """
    Muestra la imagen del producto si el archivo existe en disco.
    Si no se encuentra, muestra un emoji de respaldo para no romper la interfaz.
    """
    if ruta_imagen and os.path.exists(ruta_imagen):
        st.image(ruta_imagen, use_container_width=True)
    else:
        st.markdown(
            f"""
            <div style="font-size:{alto_emoji_px}px; text-align:center; padding-top:10px;">
                🦄✨
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# ENCABEZADO PRINCIPAL
# ============================================================
st.markdown('<div class="main-title">🦄 Friendship Bazaar</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">El mercado mágico de Equestria — artefactos, reliquias y objetos legendarios</div>',
    unsafe_allow_html=True
)

# ============================================================
# BARRA LATERAL — FILTROS
# ============================================================
st.sidebar.header("🔍 Filtros de búsqueda")

categorias = sorted(set(p["categoria"] for p in PRODUCTOS))
rarezas = sorted(set(p["rareza"] for p in PRODUCTOS))

categoria_sel = st.sidebar.multiselect(
    "Categoría",
    options=categorias,
    default=[]
)

rareza_sel = st.sidebar.multiselect(
    "Rareza",
    options=rarezas,
    default=[]
)

texto_busqueda = st.sidebar.text_input("Buscar por nombre o personaje")

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Total de productos en catálogo:** {len(PRODUCTOS)}")
st.sidebar.markdown(
    "Cada objeto cuenta con un **idProducto** único que actúa como su "
    "clave de identificación en el registro de Friendship Bazaar."
)

# ============================================================
# APLICAR FILTROS
# ============================================================
productos_filtrados = PRODUCTOS

if categoria_sel:
    productos_filtrados = [p for p in productos_filtrados if p["categoria"] in categoria_sel]

if rareza_sel:
    productos_filtrados = [p for p in productos_filtrados if p["rareza"] in rareza_sel]

if texto_busqueda:
    texto = texto_busqueda.lower().strip()
    productos_filtrados = [
        p for p in productos_filtrados
        if texto in p["nombre"].lower() or texto in p["personajeAsociado"].lower()
    ]

# ============================================================
# ESTADO DE SESIÓN — PRODUCTO SELECCIONADO
# ============================================================
if "producto_seleccionado" not in st.session_state:
    st.session_state.producto_seleccionado = None

# ============================================================
# VISTA DE DETALLE (si hay un producto seleccionado)
# ============================================================
if st.session_state.producto_seleccionado is not None:
    producto = next(
        (p for p in PRODUCTOS if p["idProducto"] == st.session_state.producto_seleccionado),
        None
    )

    if producto:
        if st.button("⬅️ Volver al catálogo"):
            st.session_state.producto_seleccionado = None
            st.rerun()

        st.markdown('<div class="detail-box">', unsafe_allow_html=True)

        col_img, col_info = st.columns([1, 2])

        with col_img:
            mostrar_imagen(producto.get("imagen", ""), alto_emoji_px=90)
            st.markdown(
                f'<div class="id-badge">ID ÚNICO: {producto["idProducto"]}</div>',
                unsafe_allow_html=True
            )

        with col_info:
            st.markdown(f'<div class="product-name" style="font-size:30px;">{producto["nombre"]}</div>',
                        unsafe_allow_html=True)
            st.markdown(
                f'<span class="{clase_rareza(producto["rareza"])}">{producto["rareza"]}</span> '
                f'&nbsp;&nbsp; 🏷️ {producto["categoria"]}',
                unsafe_allow_html=True
            )
            st.write("")
            st.markdown(f'<div class="price-tag">{formato_precio(producto["precio"])}</div>',
                        unsafe_allow_html=True)

        st.markdown("---")

        st.markdown("#### 📜 Descripción")
        st.write(producto["descripcion"])

        st.markdown("#### 🧭 Detalles del objeto")
        det_col1, det_col2 = st.columns(2)

        with det_col1:
            st.markdown(f"**🆔 ID del producto:** `{producto['idProducto']}`")
            st.markdown(f"**📦 Categoría:** {producto['categoria']}")
            st.markdown(f"**🌍 Origen:** {producto['origen']}")
        with det_col2:
            st.markdown(f"**🐴 Personaje asociado:** {producto['personajeAsociado']}")
            st.markdown(f"**✨ Nivel de magia:** {producto['nivelMagia']}")
            st.markdown(f"**💎 Rareza:** {producto['rareza']}")

        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")
        comprar_col, intercambiar_col = st.columns(2)
        with comprar_col:
            if st.button("🛒 Comprar ahora", use_container_width=True):
                st.success(f"¡Has reservado **{producto['nombre']}** por {formato_precio(producto['precio'])}! 🎉")
        with intercambiar_col:
            if st.button("🔄 Proponer intercambio", use_container_width=True):
                st.info("Tu propuesta de intercambio ha sido enviada al vendedor. 🐴💌")
    else:
        st.warning("El producto seleccionado no existe en el catálogo.")
        st.session_state.producto_seleccionado = None

# ============================================================
# VISTA DE CATÁLOGO (tarjetas de productos)
# ============================================================
else:
    st.markdown(f"### 🛍️ Catálogo ({len(productos_filtrados)} productos encontrados)")

    if not productos_filtrados:
        st.warning("No se encontraron productos con los filtros seleccionados. Intenta ajustar tu búsqueda.")
    else:
        columnas = st.columns(3)

        for indice, producto in enumerate(productos_filtrados):
            col = columnas[indice % 3]
            with col:
                st.markdown('<div class="product-card">', unsafe_allow_html=True)

                mostrar_imagen(producto.get("imagen", ""), alto_emoji_px=60)

                st.markdown(
                    f'<div class="id-badge">ID: {producto["idProducto"]}</div>',
                    unsafe_allow_html=True
                )
                st.markdown(f'<div class="product-name">{producto["nombre"]}</div>', unsafe_allow_html=True)
                st.markdown(
                    f'<span class="{clase_rareza(producto["rareza"])}">{producto["rareza"]}</span> '
                    f'&nbsp; 🏷️ {producto["categoria"]}',
                    unsafe_allow_html=True
                )
                st.write("")
                st.markdown(f"🌍 **Origen:** {producto['origen']}")
                st.markdown(f"🐴 **Personaje:** {producto['personajeAsociado']}")
                st.markdown(f"✨ **Magia:** {producto['nivelMagia']}")
                st.write("")
                st.markdown(f'<div class="price-tag">{formato_precio(producto["precio"])}</div>',
                            unsafe_allow_html=True)
                st.write("")

                if st.button("Ver detalles", key=f"detalle_{producto['idProducto']}", use_container_width=True):
                    st.session_state.producto_seleccionado = producto["idProducto"]
                    st.rerun()

                st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# PIE DE PÁGINA
# ============================================================
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#999999; font-size:13px;'>"
    "🦄 Friendship Bazaar — El mercado mágico de Equestria | Hecho con Streamlit 🐍✨"
    "</div>",
    unsafe_allow_html=True
)
