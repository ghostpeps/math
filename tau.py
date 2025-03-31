import streamlit as st

tau = r"\tau"
st.title(f"${tau}$")
st.write(f"${tau}$ (pronounced taʊ) is the double of π. That makes ${tau}$ approximately equal to 6.28. Bellow is a list of ways you could use it.")
st.latex(r"C = d\tau")
st.latex(r"A = \frac{\tau}{2} \cdot r^2")
st.latex(r"e^{e\tau} = 1")
st.write(f"Bellow is hown to solve for ${tau}$:")
st.latex(r"\tau = 2\pi")
