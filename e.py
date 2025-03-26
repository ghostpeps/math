import streamlit as st

url = "https://zacharyratliff.org/files/eMillionDigits.txt"
st.title("𝑒")
st.write("𝑒 (pronounced ē) also noun as Euler's number (pronounced **oy**·lrz nəmbər) is a constant that is at the base of a natural logarithm and exponential function. It is approximately equal to 2.71. 𝑒-day is on February 7th, while Ultimate 𝑒-day is on February 7th, 1828 at 6:28 PM. Below is how to solve for 𝑒.")
st.latex(r"\lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n")
st.write("Click [here](%s)" % url + " to see one million digits of 𝑒.")
