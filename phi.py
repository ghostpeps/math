import streamlit as st

url = "https://sketchplanations.com/the-golden-ratio"
caption = "Image Credit: [The Golden Ratio: Nature's Perfect Proportions - Sketchplanations](%s)" % url
st.title("Φ")
st.write("Φ or ϕ (pronounced fē), also known as the golden ratio, describes a relationship where two quantities are in Φ/ϕ if their ratio corresponds to the ratio of their sum to the larger quantity. Bellow is how to solve for Φ/Φ or ϕ (pronounced fē), also known as the golden ratio, which describes a relationship where two quantities are in Φ/ϕ if their ratio corresponds to the ratio of their sum to the larger quantity. Bellow is how to solve for Φ/ϕ.")
st.latex(r"\phi = \frac{1 + \sqrt{5}}{2}")
st.write("Or")
st.latex(r"\frac{a + b}{a} = \frac{a}{b} = \phi\ \ where\ \ a > b > 0")
st.write("Bellow is a picture about Φ/ϕ:")
st.image(image="the-golden-ratio.png", caption=caption)
