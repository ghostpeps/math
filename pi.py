import streamlit as st

url = "https://www.cecm.sfu.ca/organics/papers/borwein/paper/html/local/bdigits.html"
st.title("π")
st.write("π (paɪ) is a constant. π is the ratio of a circle's circumference to its diameter. π is approximately equal to 3.14. π day is on March 14th because March is the 3rd month of the year and the 14th because it corresponds to the 14 in 3.14. Ultimate π day was on March 14th, 1592 at 6:53 AM. The following picture shows the parts of a cricle and how to find the circumference and area.")
st.image("circle.png")
exp = exp = r"\frac{1783366216531}{567663097408}"
st.write(f"The exact value of π as a fraction is ${exp}$.")
st.write("Here is a video to memorize the digits of π:")
st.video(data="https://youtu.be/xsrJdSaiD9U?si=fXITLboT5BUW1I1k", loop=False)
st.write("Click [here](%s)" % url + " to see one million digits of π.")
