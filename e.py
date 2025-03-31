import streamlit as st

url = "https://zacharyratliff.org/files/eMillionDigits.txt"
e = r"e"
st.title(f"${e}$")
st.write(f"${e}$ (pronounced ē), also known as Euler's number (pronounced **oy**·lrz nəmbər), is a constant that is at the base of a natural logarithm and exponential function. It is approximately equal to 2.71. ${e}$-day is on February 7th, while Ultimate ${e}$-day was on February 7th, 1828 at 6:28 PM. Below is how to solve for it.")
st.latex(r"e = \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n")
st.write("Or")
st.latex(r"e = \sum_{n=0}^{\infty} \frac{1}{n!}")
st.write(r"Click [here](%s)" % url + " to see one million digits of $e$.")
