import streamlit as st

golden = r"\psi"
st.title(f"${golden}$")
st.write(f"${golden}$ is a ratio. $a$ and $b$ are in it if:")
st.latex(r"\left(\frac{a + b}{a}\right)^2 = \frac{a}{b} for a > b > 0")
