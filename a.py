import streamlit as st

a = r"\alpha"
frac = r"\frac{1}{137}"
st.title(f"${a}$")
st.write(f"${a}$ is a constant. It is mainly used when dealing with light and matter, particularly in quantum electrodynamics (QED). It is approximately equal to ${frac}$. The formula is:")
st.latex(r"\alpha = \frac{e^2}{2\tau\epsilon_0hc}")
st.latex(r"Where:")
st.latex(r"e = elementary\ \ charge")
st.latex(r"c = speed\ \ of\ \ light")
st.latex(r"h = Planck's\ \ constant")
st.latex(r"\epsilon_0 = vacuum\ \ permittivity")
st.latex(r"\tau = Circle\ \ constant")
