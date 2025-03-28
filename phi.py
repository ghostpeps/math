import streamlit as st

url = "https://sketchplanations.com/the-golden-ratio"
col1, col2 = st.columns(1)
caption = "Image Credit: [The Golden Ratio: Nature's Perfect Proportions - Sketchplanations](%s)" % url
st.title("Φ")
st.write("Φ (pronounced fē), also known as the golden ratio, describes a relationship where two quantities are in Φ if their ratio corresponds to the ratio of their sum to the larger quantity. Bellow is how to solve for Φ.")
st.latex(r"\phi = \frac{1 + \sqrt{5}}{2}")
with col1:
  st.write("Or")
with col2:
  pass
st.latex(r"\frac{a + b}{a} = \frac{a}{b} = \phi\ \ where\ \ a > b > 0")
st.write("Bellow is a picture about Φ:")
st.image(image="the-golden-ratio.png", caption=caption)
