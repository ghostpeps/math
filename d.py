import streamlit as st

delta = r"\delta"
st.title(f"${delta}$")
st.write(f"${delta}$ is used to show a small difference for a variable. Ex.")
st.latex(r"\deltax = 2")
st.write("This means that the change of $x$ is 2.")
