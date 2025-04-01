import streamlit as st

url = "https://sketchplanations.com/the-golden-ratio"
phi = r"\phi"
caption = "Image Credit: [The Golden Ratio: Nature's Perfect Proportions - Sketchplanations](%s)" % url
st.title(f"${phi}$")
st.write(f"${phi}$ (pronounced fē), also known as the golden ratio, describes a relationship where two quantities are in ${phi}$ if their ratio corresponds to the ratio of their sum to the larger quantity. Bellow is how to solve for it.")
st.latex(r"\phi = \frac{1 + \sqrt{5}}{2}")
st.html(
  """<p style="text-align: center;">Or</p>"""
)
st.latex(r"""
  \frac{\color{lightgreen}a + b}{\color{blue}a} = \frac{\color{blue}a}{\color{red}b} = \phi\ \ for\ \ \color{blue}a \color{off}> \color{red}b \color{off}> 0
""")
st.write(f"Bellow is a picture about ${phi}$:")
st.image(image="the-golden-ratio.png", caption=caption)
