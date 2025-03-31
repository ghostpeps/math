import streamlit as st

g = r"G"
st.title(f"${g}$")
st.write(f"${g}$ is a proportionality constant used in Newton's law of universal gravitation to calculate the gravitational force between two objects. The formula is:")
st.latex(r"F = G \cdot \frac{m_1 \cdot m_2}{r^2}")
st.latex(r"F\ \ is\ \ the\ \ force\ \ of\ \ gravity")
st.latex(r"m_1\ \ is\ \ the\ \ first\ \ mass")
st.latex(r"m_2\ \ is\ \ the\ \ second\ \ mass")
st.latex(r"r\ \ is\ \ the\ \ distance\ \ between\ \ the\ \ centers\ \ of\ \ m_1\ \ and\ \ m_2")
st.latex(r"G \approx 6.67430 \cdot 10^{-11}\ \ N \cdot \dfrac{m^2}{kg^2}")
