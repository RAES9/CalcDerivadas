import streamlit as st
from sympy import symbols, diff, simplify, latex, lambdify
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
import pandas as pd
import re

x = symbols('x')
st.set_page_config(page_title="Derivador de Funciones", page_icon="📐")
st.title("📐 Derivador de Funciones")
st.markdown("Introduce una función válida en términos de `x`. Ejemplos:\n"
            "- `x*sin(x)`\n"
            "- `e^(x^2)`\n"
            "- `(x+1)^3`\n"
            "- `ln(x)`\n"
            "- `5x^3 - 2x - 1`")

def normalizar_funcion(func):
    func = func.replace('𝑥', 'x').replace('×', '*').replace('–', '-').replace('−', '-')
    func = func.replace('^', '**')
    func = re.sub(r'(\d)(x)', r'\1*\2', func)     # 5x → 5*x
    func = re.sub(r'(x)(\d)', r'\1*\2', func)     # x2 → x*2
    return func

func_input = st.text_input("✍️ Escribe tu función:", value="5x^3 - 2x - 1")

if func_input:
    try:
        func_input = normalizar_funcion(func_input)

        expr = parse_expr(func_input, evaluate=False)
        derivada = diff(expr, x)
        derivada_simplificada = simplify(derivada)

        st.subheader("🧮 Resultado simbólico")
        st.latex(f"f(x) = {latex(expr)}")
        st.latex(f"f'(x) = {latex(derivada_simplificada)}")

        f_lamb = lambdify(x, expr, modules=["numpy"])
        f_der_lamb = lambdify(x, derivada_simplificada, modules=["numpy"])
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lamb(x_vals)
        y_der_vals = f_der_lamb(x_vals)

        df = pd.DataFrame({
            "x": x_vals,
            "f(x)": y_vals,
            "f'(x)": y_der_vals
        })

        st.subheader("📊 Gráfica de la función y su derivada")
        st.line_chart(df.set_index("x"))

    except Exception as e:
        st.error(f"❌ Error al procesar la función: {e}")
