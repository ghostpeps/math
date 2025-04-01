import streamlit as st

l = r"\lambda"
st.title(f"${l}$")
st.write(f"${l}$, or Conway's constant, is a sequence using the look-and-say sequence. Bellow is a list:")
st.write("""
  1. 1 (1)
  2. 11 (one 1)
  3. 21 (two 1's)
  4. 1211 (one 2, one 1)
  5. 111221 (one 1, one 2, two 1's)
  And so on...
""")
st.write("The formula is:")
st.latex(r"\lambda = \lim{n \to \infty} \frac{a_n + 1}{a_n} \approx 1.303577296")
