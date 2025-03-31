import streamlit as st

url = "https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt"
pi = r"\pi"
st.title(f"${pi}$")
st.write(f"${pi}$ (pronounced paɪ) is a constant. It is the ratio of a circle's circumference to its diameter. It is approximately equal to 3.14. ${pi}$ day is on March 14th because March is the 3rd month of the year and the 14th because it corresponds to the 14 in 3.14. Ultimate ${pi}$ day was on March 14th, 1592, at 6:53 AM. The following picture shows the parts of a circle and how to find the circumference and area.")
st.image("circle.png")
st.write(f"This is how to solve for ${pi}$:")
st.latex(r"\pi = \frac{C}{d}")
exp = exp = r"3\frac{80376924307}{567663097408}"
st.write(f"The exact value of π as a mixed number is ${exp}$.")
st.write(f"Here is a video to memorize the digits of ${pi}$:")
st.video(data="https://youtu.be/xsrJdSaiD9U?si=fXITLboT5BUW1I1k", loop=False)
st.write(r"Click [here](%s)" % url + " to see one billion digits of $\pi$.")
