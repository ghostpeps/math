import streamlit as st

ii = r"i^i"
neg_one = r"\sqrt{-1}^{\sqrt{-1}}"
rad = r"\frac{1}{\sqrt{e^\pi}}"
st.title(f"${ii}$")
st.write(f"${ii}$ is the same as saying ${neg_one}$. It is also the same as ${rad}$. Bellow is how to solve for it.")
st.latex(r"i^i = \left(e^{i\frac{\pi}{2}}\right)^i = e^{i^2 \cdot \frac{\pi}{2}} = e^{-\frac{\pi}{2}}")
st.latex(r"i^i \approx 0.207879572")
