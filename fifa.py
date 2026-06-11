import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
from zoneinfo import ZoneInfo

# =====================================
# CONFIGURACIÓN
# =====================================

st.set_page_config(
    page_title="ANUIES Mundial 2026",
    page_icon="⚽",
    layout="wide"
)

st_autorefresh(interval=1000, key="reloj")

# =====================================
# ESTILOS
# =====================================


st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container{
    padding-top: 0.5rem;
    padding-bottom: 0rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

.stApp{
    background:
    linear-gradient(
    180deg,
    #001233 0%,
    #001845 50%,
    #023e8a 100%);
}

.titulo{
    font-size:50px;
    font-weight:bold;
    text-align:center;
    color:white;
    margin-top: -40px;
}

.subtitulo{
    font-size:60px;
    font-weight: bold;
    text-align:center;
    color:#FFD700;
}

            
[data-testid="stMetric"]{
    text-align:center;
}


/* Etiqueta: Días, Horas, Minutos, Segundos */
[data-testid="stMetricLabel"] {
    font-size: 28px !important;
    font-weight: bold !important;
    color: #FFD700 !important;
}

/* Valor: 0, 17, 07, 36 */
[data-testid="stMetricValue"] {
    font-size: 60px !important;
    font-weight: bold !important;
    color: white !important;
}
            
[data-testid="stMetricValue"] {
    font-size: 80px !important;
    font-weight: 900 !important;
    color: white !important;
}
            
/* Etiquetas de st.metric() */

[data-testid="stMetricLabel"] p {
    font-size: 24px !important;
    font-weight: 700 !important;
    color: #FFD700 !important;
}
            
</style>
""", unsafe_allow_html=True)


## LOGO ####
st.image(
    "logo anuies horizontal simple.png",
    width=250
)


# =====================================
# ENCABEZADO
# =====================================

st.markdown(
    "<div class='titulo'>🏆 Mundial 2026 🏆</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitulo'>(🇲🇽) MÉXICO vs SUDÁFRICA (🇿🇦)</div>",
    unsafe_allow_html=True
)

# =====================================
# TEMPORIZADOR
# =====================================

fecha_partido = datetime(
    2026, 6, 11, 11, 30, 0,
    tzinfo=ZoneInfo("America/Mexico_City")
)

ahora = datetime.now(ZoneInfo("America/Mexico_City"))

diferencia = fecha_partido - ahora

dias = diferencia.days
horas = diferencia.seconds // 3600
minutos = (diferencia.seconds % 3600) // 60
segundos = diferencia.seconds % 60

st.markdown("""
<h1 style='text-align:center;
color:#64FFDA;;;'>

⏳ Cuenta Regresiva

</h1>
""",
unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Días", dias)
c2.metric("Horas", horas)
c3.metric("Minutos", minutos)
c4.metric("Segundos", segundos)

#st.divider()

# =====================================
# CONSENSO ANUIES
# =====================================

###PRONÖSTICO####
marcadores = pd.DataFrame({
    "Marcador":[
        "2-1",
        "2-0",
        "3-1",
        "3-0",
        "1-0",
        "2-2",
        "3-2",
        "1-1",
        "4-1",
        "4-2"
    ],
    "Frecuencia":[
        29,
        25,
        20,
        5,
        3,
        3,
        3,
        1,
        1,
        1
    ]
})


##DATOS##

st.markdown("""
<h1 style = 'text-align:center;
color:#64FFDA;;'>
            
📊 Pronóstico ANUIES
            
</h1>

""",
unsafe_allow_html=True)

            
#st.markdown("## 📊 PRONÓSTICO")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Marcador",
        "Mx 2-1 Za"
    )

with c2:
    st.metric(
        "Primer gol",
        "25'"
    )

with c3:
    st.metric(
        "Goleador",
        "Raúl Jiménez"
    )


###PIE
st.markdown("""
<div style="
font-size:20px;
font-weight:bold;
color:white;
text-align:center;
padding:10px;">

 Pronóstico basado en 92 volantes, ¡Gracias por participar!

</div>
""",
unsafe_allow_html=True)
