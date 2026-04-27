import os
import joblib
import pandas as pd
import streamlit as st

# ── Page config (must be first Streamlit call) ───────────────────────────────
st.set_page_config(
    page_title="Predictor de Precios · Madrid",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }
#MainMenu, footer, header   { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 4rem; max-width: 720px; }
.stApp { background: #ECEEF2; }

/* ── Hero ── */
.hero {
    background: linear-gradient(135deg, #C8102E 0%, #7A000E 100%);
    border-radius: 20px;
    padding: 2.4rem 2rem;
    margin-bottom: 1.6rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(200, 16, 46, 0.25);
}
.hero h1 {
    color: white; font-size: 2rem; font-weight: 800;
    margin: 0; letter-spacing: -0.5px; line-height: 1.2;
}
.hero p {
    color: rgba(255,255,255,0.82); font-size: 0.95rem;
    margin: 0.5rem 0 0; font-weight: 300;
}

/* ── Section labels ── */
.slabel {
    display: block; font-size: 0.68rem; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase;
    color: #C8102E; margin: 1.6rem 0 0.5rem;
}

/* ── Result card ── */
.result-box {
    background: linear-gradient(135deg, #1A1A2E 0%, #16213E 100%);
    border-radius: 20px; padding: 2.2rem 2rem 2rem;
    text-align: center; margin-top: 1rem;
    box-shadow: 0 12px 40px rgba(0,0,0,0.20);
    animation: fadeUp 0.4s ease;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0);    }
}
.result-box .rlabel {
    font-size: 0.68rem; text-transform: uppercase;
    letter-spacing: 2px; color: rgba(255,255,255,0.5);
    margin-bottom: 0.3rem;
}
.result-box .rprice {
    font-size: 3.2rem; font-weight: 800;
    color: #FFD700; letter-spacing: -1px; line-height: 1.1;
}
.result-box .rsub {
    font-size: 0.82rem; color: rgba(255,255,255,0.45); margin-top: 0.5rem;
}

/* ── Button ── */
.stButton > button {
    background: linear-gradient(135deg, #C8102E, #7A000E) !important;
    color: white !important; border: none !important;
    border-radius: 12px !important; padding: 0.75rem 1rem !important;
    font-size: 1rem !important; font-weight: 600 !important;
    width: 100% !important; letter-spacing: 0.3px !important;
    box-shadow: 0 4px 16px rgba(200,16,46,0.30) !important;
    margin-top: 0.6rem; transition: all 0.2s ease !important;
}
.stButton > button:hover {
    box-shadow: 0 6px 22px rgba(200,16,46,0.45) !important;
    transform: translateY(-1px) !important;
}

/* ── Divider ── */
.sdivider {
    border: none; border-top: 1px solid rgba(0,0,0,0.08);
    margin: 0.4rem 0 1rem;
}
</style>
""", unsafe_allow_html=True)

# ── Load model ───────────────────────────────────────────────────────────────
_dir = os.path.dirname(os.path.abspath(__file__))

try:
    modelo = joblib.load(os.path.join(_dir, "..", "Models", "Rf.joblib"))
except Exception as e:
    st.error(f"No se pudo cargar el modelo: {e}")
    st.stop()

# ── Static data ───────────────────────────────────────────────────────────────

# Precio medio por código postal (calculado en el EDA)
PRECIO_MEDIO_CP = {
    28000: 942338,  28001: 1709528, 28002: 700100,  28003: 898889,
    28004: 745917,  28005: 421413,  28006: 1207212,  28007: 529747,
    28008: 766309,  28009: 941621,  28010: 1018679,  28011: 259011,
    28012: 439992,  28013: 760050,  28014: 856046,   28015: 669236,
    28016: 923762,  28017: 238758,  28018: 166500,   28019: 226302,
    28020: 597620,  28021: 156772,  28022: 280852,   28023: 1274253,
    28024: 199225,  28025: 197312,  28026: 202513,   28027: 379788,
    28028: 603234,  28029: 347317,  28030: 247271,   28031: 234693,
    28032: 260153,  28033: 471372,  28034: 718994,   28035: 733699,
    28036: 1197915, 28037: 260568,  28038: 164928,   28039: 301371,
    28040: 645360,  28041: 212177,  28042: 457692,   28043: 911651,
    28044: 192864,  28045: 357857,  28046: 1134196,  28047: 219078,
    28048: 764000,  28049: 561631,  28050: 480497,   28051: 314346,
    28052: 382726,  28053: 152717,  28054: 255165,   28055: 761064,
}

# Latitud aproximada del centroide de cada distrito
DISTRITO_LAT = {
    "Centro":              40.413, "Arganzuela":          40.396,
    "Retiro":              40.407, "Salamanca":           40.428,
    "Chamartín":           40.457, "Tetuán":              40.460,
    "Chamberí":            40.434, "Fuencarral-El Pardo": 40.480,
    "Moncloa-Aravaca":     40.433, "Latina":              40.400,
    "Carabanchel":         40.385, "Usera":               40.389,
    "Puente de Vallecas":  40.394, "Moratalaz":           40.406,
    "Ciudad Lineal":       40.440, "Hortaleza":           40.476,
    "Villaverde":          40.346, "Villa de Vallecas":   40.373,
    "Vicálvaro":           40.406, "San Blas-Canillejas": 40.426,
    "Barajas":             40.476,
}

# Zonas → distritos → códigos postales
ZONAS = {
    "Norte": {
        "Chamartín":            [28002, 28016, 28036, 28046],
        "Tetuán":               [28020, 28035, 28039],
        "Fuencarral-El Pardo":  [28029, 28034, 28048, 28049],
        "Hortaleza":            [28033, 28043, 28050],
        "Barajas":              [28042, 28055],
    },
    "Centro": {
        "Centro":               [28004, 28005, 28012, 28013, 28014],
        "Arganzuela":           [28045],
        "Retiro":               [28007, 28008, 28009],
        "Salamanca":            [28001, 28006, 28028],
        "Chamberí":             [28003, 28010, 28015],
        "Moncloa-Aravaca":      [28011, 28023, 28040],
        "Ciudad Lineal":        [28017, 28027, 28037],
        "Latina":               [28019, 28024, 28044, 28047, 28054],
        "San Blas-Canillejas":  [28022],
    },
    "Sur": {
        "Carabanchel":          [28025],
        "Usera":                [28026],
        "Puente de Vallecas":   [28018, 28038, 28053],
        "Moratalaz":            [28030],
        "Villaverde":           [28021],
        "Villa de Vallecas":    [28031],
        "Vicálvaro":            [28032],
    },
}

# ── App ───────────────────────────────────────────────────────────────────────
def main():

    # Hero
    st.markdown("""
    <div class="hero">
        <h1>🏠 Predictor de Precios</h1>
        <p>Estimá el valor de una vivienda en Madrid con Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Ubicación ────────────────────────────────────────────────────────────
    st.markdown('<span class="slabel">📍 Ubicación</span>', unsafe_allow_html=True)
    st.markdown('<hr class="sdivider">', unsafe_allow_html=True)

    zona = st.selectbox("Zona de Madrid", list(ZONAS.keys()))
    c1, c2 = st.columns(2)
    distrito = c1.selectbox("Distrito", list(ZONAS[zona].keys()))
    cp       = c2.selectbox("Código postal", ZONAS[zona][distrito])

    # ── Características ──────────────────────────────────────────────────────
    st.markdown('<span class="slabel">🏗️ Características</span>', unsafe_allow_html=True)
    st.markdown('<hr class="sdivider">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    superficie   = c1.number_input("Superficie (m²)", min_value=17.0,  value=80.0, step=5.0)
    habitaciones = c2.number_input("Habitaciones",    min_value=0,     value=2,    step=1)
    banos        = c3.number_input("Baños",           min_value=1,     value=1,    step=1)

    # ── Comodidades ──────────────────────────────────────────────────────────
    st.markdown('<span class="slabel">✨ Comodidades</span>', unsafe_allow_html=True)
    st.markdown('<hr class="sdivider">', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    ascensor    = c1.checkbox("🛗 Ascensor")
    parking     = c2.checkbox("🚗 Parking")
    balcon      = c3.checkbox("🌿 Balcón")
    terraza     = c4.checkbox("☀️ Terraza")

    c5, c6, c7, _ = st.columns(4)
    aire        = c5.checkbox("❄️ Aire acond.")
    calefaccion = c6.checkbox("🔥 Calefacción")
    piscina     = c7.checkbox("🏊 Piscina")

    # ── Predicción ───────────────────────────────────────────────────────────
    if st.button("Estimar precio →"):
        entrada = pd.DataFrame([{
            "Latitud":            DISTRITO_LAT[distrito],
            "Precio_Medio_cp":    PRECIO_MEDIO_CP[cp],
            "Superficie_m2":      superficie,
            "Habitaciones":       habitaciones,
            "Baños":              banos,
            "Ascensor":           int(ascensor),
            "Parking":            int(parking),
            "Balcon":             int(balcon),
            "Aire_Acondicionado": int(aire),
            "Calefaccion":        int(calefaccion),
            "Piscina":            int(piscina),
            "Terraza":            int(terraza),
        }])

        precio = modelo.predict(entrada)[0]

        st.markdown(f"""
        <div class="result-box">
            <div class="rlabel">Precio estimado</div>
            <div class="rprice">€{precio:,.0f}</div>
            <div class="rsub">{distrito} · CP {cp}</div>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
