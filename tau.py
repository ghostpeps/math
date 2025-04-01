import streamlit as st

tau = r"\tau"
st.title(f"${tau}$")
st.write(f"${tau}$ (pronounced taʊ) is the double of π. That makes ${tau}$ approximately equal to 6.28. Bellow is a list of ways you could use it.")
st.latex(r"C = r\tau")
st.latex(r"A = \frac{\tau}{2} \cdot r^2")
st.latex(r"e^{i\tau} = 1")
st.write(f"Bellow is how to solve for ${tau}$:")
st.latex(r"\tau = 2\pi")
st.html(
  """<p style="text-align: center;">Or</p>"""
)
st.latex(r"\tau = \frac{C}{r}")
