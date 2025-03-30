import streamlit as st

y = r"\gamma"
st.title(f"${y}$")
st.write(f"${y}$ (pronounced ɡamə), is approximately equal to 0.57721. It represents the Euler-Mascheroni constant. The definition of ${y}$ is:")
st.latex(r"\gamma = \lim_{n \to \infty} \left( \sum_{k=1}^{n} \frac{1}{k} - \ln(n) \right) \approx 0.57721")
