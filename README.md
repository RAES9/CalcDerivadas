# 📐 Derivador de Funciones con IA (SymPy + Streamlit)

Esta aplicación permite derivar funciones matemáticas escritas en notación tradicional como texto. Utiliza `SymPy` para realizar derivación simbólica precisa y `Streamlit` para mostrar los resultados y gráficos de manera interactiva.

---

## 🚀 Funcionalidades

✅ Derivación automática de funciones escritas como texto  
✅ Soporte para funciones:
- Polinomiales: `5x^3 - 2x + 1`
- Trigonométricas: `sin(x)`, `cos(x)`, `tan(x)`
- Exponenciales: `e^(x^2)`, `exp(3x)`
- Logarítmicas: `ln(x)`
- Compuestas: `x*sin(x)`, `(x+1)^3`

✅ Limpieza automática de caracteres inválidos: `𝑥`, `–`, `^`, etc.  
✅ Gráficas interactivas de `f(x)` y `f'(x)` con `streamlit.line_chart`  
✅ Interfaz clara, responsiva y sin necesidad de instalación local

---

## 🧑‍💻 ¿Cómo usar esta app?

### 1. Clona este repositorio

```bash
git clone https://github.com/tu-usuario/derivador-streamlit.git
cd derivador-streamlit
```

### 2. Instala dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecuta localmente

```bash
streamlit run main.py
```

---

## 🌐 Desplegar en Streamlit Cloud

1. Sube este repositorio a tu cuenta de GitHub  
2. Ve a [https://share.streamlit.io](https://share.streamlit.io)  
3. Conecta tu repo y selecciona `main.py` como archivo principal  
4. ¡Listo! Tu app estará en línea

---

## 📝 Ejemplos que puedes probar

```text
x*sin(x)
e^(x^2)
(x+1)^3
ln(x)
5x^3 - 2x - 1
tan(x^2 + 1)
```

---

## 📦 Dependencias

- [Streamlit](https://streamlit.io/)
- [SymPy](https://www.sympy.org/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)

---

## 💡 Autor

Desarrollado por Edwin Esteban Rivas Lucas  
Estudiante de Ingeniería – Universidad del Valle de Guatemala  
