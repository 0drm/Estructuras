import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="Examen Diagnóstico - Estructuras 1", layout="wide")

# Estilos CSS personalizados
st.markdown("""
    <style>
    .header {
        font-size: 24px;
        font-weight: bold;
        color: #1e3a8a;
        padding: 10px;
        border-bottom: 2px solid #1e3a8a;
        margin-bottom: 20px;
    }
    .section {
        background-color: #f0f8ff;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .question {
        margin: 15px 0;
        padding: 10px;
        border-left: 3px solid #1e3a8a;
    }
    .button {
        background-color: #1e3a8a !important;
        color: white !important;
        font-weight: bold !important;
        margin-top: 20px;
    }
    .result {
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        padding: 15px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar estado de sesión
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = [None]*10
if 'puntaje' not in st.session_state:
    st.session_state.puntaje = 0

# Encabezado
st.markdown('<div class="header">📝 Examen Diagnóstico - Estructuras 1</div>', unsafe_allow_html=True)
st.write("**Instrucciones:** Resuelve cada problema y escribe tu respuesta en el espacio proporcionado. Tiempo estimado: 60 minutos.")

# Sección 1: Trigonometría
with st.container():
    st.markdown('<div class="section">🔺 <strong>Sección 1: Trigonometría</strong> (15 puntos)</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="question">1. En un triángulo rectángulo, el cateto adyacente al ángulo θ mide 6 m y la hipotenusa 10 m. Calcule:</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.respuestas[0] = st.number_input("a) sen(θ)", min_value=0.0, max_value=1.0, step=0.01, key="q1a")
    with col2:
        st.session_state.respuestas[1] = st.number_input("b) cos(θ)", min_value=0.0, max_value=1.0, step=0.01, key="q1b")
    with col3:
        st.session_state.respuestas[2] = st.number_input("c) tan(θ)", min_value=0.0, step=0.01, key="q1c")

    st.markdown('<div class="question">2. Descomponga la fuerza F = 200 N en sus componentes horizontal (F_x) y vertical (F_y), si forma un ángulo de 30° con el eje X.</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.respuestas[3] = st.number_input("F_x (N)", min_value=0.0, step=0.1, key="q2a")
    with col2:
        st.session_state.respuestas[4] = st.number_input("F_y (N)", min_value=0.0, step=0.1, key="q2b")

    st.markdown('<div class="question">3. Calcule la altura h de un edificio si, desde un punto a 20 m de su base, se observa su parte superior con un ángulo de elevación de 45°.</div>', unsafe_allow_html=True)
    st.session_state.respuestas[5] = st.number_input("Altura (m)", min_value=0.0, step=0.1, key="q3")

# Sección 2: Álgebra
with st.container():
    st.markdown('<div class="section">➗ <strong>Sección 2: Álgebra</strong> (15 puntos)</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="question">4. Resuelva el sistema de ecuaciones: 3x + 2y = 16, 2x - y = 3</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.respuestas[6] = st.number_input("x", step=0.1, key="q4a")
    with col2:
        st.session_state.respuestas[7] = st.number_input("y", step=0.1, key="q4b")

    st.markdown('<div class="question">5. Factorice la expresión: 3x² - 12x - 36</div>', unsafe_allow_html=True)
    st.session_state.respuestas[8] = st.text_input("Respuesta", key="q5", value="")

    st.markdown('<div class="question">6. Despeje x en la ecuación: 1/(x-2) + 3 = 4/(x-2)</div>', unsafe_allow_html=True)
    st.session_state.respuestas[9] = st.number_input("x", step=0.1, key="q6")

# Sección 3: Geometría
with st.container():
    st.markdown('<div class="section">📏 <strong>Sección 3: Geometría</strong> (10 puntos)</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="question">7. Calcule el área del triángulo con base b = 8 cm y altura h = 5 cm</div>', unsafe_allow_html=True)
    st.session_state.respuestas[10] = st.number_input("Área (cm²)", min_value=0.0, step=0.1, key="q7")

    st.markdown('<div class="question">8. Momento de inercia I de un rectángulo (b=0.3m, h=0.4m) respecto a su base (I = b·h³/3)</div>', unsafe_allow_html=True)
    st.session_state.respuestas[11] = st.number_input("I (m⁴)", min_value=0.0, step=0.0001, format="%.4f", key="q8")

# Sección 4: Física/Estática
with st.container():
    st.markdown('<div class="section">⚖️ <strong>Sección 4: Física/Estática</strong> (10 puntos)</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="question">9. Viga con carga uniforme de 500 kg/m en 4 m. Calcule carga total P</div>', unsafe_allow_html=True)
    st.session_state.respuestas[12] = st.number_input("P (kg)", min_value=0.0, step=1.0, key="q9")

    st.markdown('<div class="question">10. Fuerza resultante de F₁=100N (→) y F₂=150N (↑)</div>', unsafe_allow_html=True)
    st.session_state.respuestas[13] = st.number_input("Resultante (N)", min_value=0.0, step=0.1, key="q10")

# Botón de evaluación
if st.button('📤 Calificar Examen', key='calcular', use_container_width=True):
    # Respuestas correctas
    respuestas_correctas = [
        0.8, 0.6, 1.333,      # Pregunta 1
        173.2, 100,            # Pregunta 2
        20,                    # Pregunta 3
        4, 5,                  # Pregunta 4
        "3(x-6)(x+2)",         # Pregunta 5
        3,                     # Pregunta 6
        20,                    # Pregunta 7
        0.0064,                # Pregunta 8
        2000,                  # Pregunta 9
        180.28                 # Pregunta 10
    ]
    
    # Alternativas aceptables para pregunta 5
    alternativas_q5 = [
        "3(x-6)(x+2)",
        "3(x+2)(x-6)",
        "3 (x-6)(x+2)",
        "3 (x+2)(x-6)",
        "3(x - 6)(x + 2)",
        "3 (x - 6) (x + 2)"
    ]
    
    # Calificación
    puntaje = 0
    resultados = []
    
    # Pregunta 1 (3 partes)
    for i in range(3):
        if abs(st.session_state.respuestas[i] - respuestas_correctas[i]) < 0.05:
            puntaje += 1.67
            resultados.append(f"✅ P1.{chr(97+i)}: Correcto (+1.67 pts)")
        else:
            resultados.append(f"❌ P1.{chr(97+i)}: Incorrecto | Esperado: {respuestas_correctas[i]}")
    
    # Pregunta 2
    if abs(st.session_state.respuestas[3] - respuestas_correctas[3]) < 1:
        puntaje += 2.5
        resultados.append("✅ P2a: Correcto (+2.5 pts)")
    else:
        resultados.append(f"❌ P2a: Incorrecto | Esperado: {respuestas_correctas[3]}")
    
    if abs(st.session_state.respuestas[4] - respuestas_correctas[4]) < 1:
        puntaje += 2.5
        resultados.append("✅ P2b: Correcto (+2.5 pts)")
    else:
        resultados.append(f"❌ P2b: Incorrecto | Esperado: {respuestas_correctas[4]}")
    
    # Pregunta 3
    if abs(st.session_state.respuestas[5] - respuestas_correctas[5]) < 0.1:
        puntaje += 5
        resultados.append("✅ P3: Correcto (+5 pts)")
    else:
        resultados.append(f"❌ P3: Incorrecto | Esperado: {respuestas_correctas[5]}")
    
    # Pregunta 4
    if abs(st.session_state.respuestas[6] - respuestas_correctas[6]) < 0.1:
        puntaje += 2.5
        resultados.append("✅ P4a: Correcto (+2.5 pts)")
    else:
        resultados.append(f"❌ P4a: Incorrecto | Esperado: {respuestas_correctas[6]}")
    
    if abs(st.session_state.respuestas[7] - respuestas_correctas[7]) < 0.1:
        puntaje += 2.5
        resultados.append("✅ P4b: Correcto (+2.5 pts)")
    else:
        resultados.append(f"❌ P4b: Incorrecto | Esperado: {respuestas_correctas[7]}")
    
    # Pregunta 5
    respuesta_q5 = st.session_state.respuestas[8].strip().lower()
    if any(alt in respuesta_q5 for alt in [a.lower() for a in alternativas_q5]):
        puntaje += 5
        resultados.append("✅ P5: Correcto (+5 pts)")
    else:
        resultados.append(f"❌ P5: Incorrecto | Esperado: {respuestas_correctas[8]}")
    
    # Resto de preguntas
    preguntas_restantes = [
        (9, 5, 0.1),    # P6
        (10, 5, 0.1),   # P7
        (11, 5, 0.0001),# P8
        (12, 5, 1),     # P9
        (13, 5, 0.1)     # P10
    ]
    
    for i, (idx, puntos, tolerancia) in enumerate(preguntas_restantes, 6):
        if abs(st.session_state.respuestas[idx] - respuestas_correctas[idx]) < tolerancia:
            puntaje += puntos
            resultados.append(f"✅ P{i+1}: Correcto (+{puntos} pts)")
        else:
            resultados.append(f"❌ P{i+1}: Incorrecto | Esperado: {respuestas_correctas[idx]}")
    
    # Guardar puntaje
    st.session_state.puntaje = puntaje
    
    # Mostrar resultados
    st.markdown(f'<div class="result">Puntaje Total: {puntaje:.2f}/50 pts</div>', unsafe_allow_html=True)
    
    with st.expander("🔍 Ver detalles de calificación"):
        for res in resultados:
            st.write(res)
        
        st.markdown("---")
        if puntaje < 35:
            st.warning("📝 **Recomendación:** Se requiere refuerzo en cursos remediales (precálculo/física)")
        elif puntaje < 45:
            st.info("📘 **Recomendación:** Bases suficientes, requiere reforzamiento en aplicaciones a estructuras")
        else:
            st.success("🏆 **Recomendación:** Buen dominio de los prerrequisitos")

# Instrucciones adicionales
st.markdown("---")
st.markdown("**Notas:**")
st.markdown("- Las respuestas numéricas deben ingresarse con 2 decimales")
st.markdown("- Para factorización (Pregunta 5), use formato: `3(x-6)(x+2)`")
st.markdown("- Puntaje mínimo sugerido: 35/50 puntos")
