import streamlit as st

eulers_identity = r"e^{i\pi}"
st.title(f"${eulers_identity}$")
st.write(f"${eulers_identity}$, also known as Euler's Identity or God's number, ${eulers_identity}$ is their to show how 𝑒, i, and π are related. Bellow is Euler's Formula:")
st.latex(r"e^{i\theta} = \cos(\theta) + i \cdot \sin(\theta)")
st.latex(r"Where\ \ \theta = \pi")
st.latex(r"e^{i\pi} = \cos(\pi) + i \cdot \sin(\pi)")
st.latex(r"Trigonometric\ \ Values:")
st.latex(r"\cos(\pi) = -1\ \ and\ \ \sin(\pi) = 0")
st.latex(r"\therefore e^{i\pi} = -1 + i \cdot 0 = -1")
