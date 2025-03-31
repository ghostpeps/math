import streamlit as st

zeta = r"\zeta(3)"
st.title(f"${zeta}$")
st.write(f"${zeta}$, also known as Apéry's constant, is a constant using the zeta function. It can also be said as the zeta function at 3. Bellow is how to solve for ${zeta}$:")
st.latex(r"\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} for s > 1")
st.latex(r"Where\ \ s = 3")
st.latex(r"\zeta(3) = \sum_{n=1}^{\infty} \frac{1}{n^3}")
st.latex(r"\zeta(3) \approx 1.20205")
