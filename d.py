import streamlit as st
import pandas as pd

delta = r"\delta"
frac = r"\frac{10}{\pi - 1}"
n = r"n"
an = r"a_n"
ratio = r"\frac{\alpha_{n-1} - \alpha_{n-2}}{\alpha_n - \alpha_{n-1}}"
st.title(f"${delta}$")
st.write(f"${delta}$ represents the limit of the ratio of distances between successive bifurcation points in a period-doubling scenario. The following is the formula for it.")
st.latex(r"\delta = \lim_{n \to \infty} \frac{\alpha_{n-1} - \alpha_{n-2}}{\alpha_n - \alpha_{n-1}}")
st.write(f"It is approximately equal to ${frac}$. Bellow is the limiting ratio of each bifurcation interval to the next between every period doubling, of a one-parameter map.")
st.latex(r"x_{i + 1} = f(x_i)")
df = pd.DataFrame(
    {
        f"${n}$": ["1", "2", "3", "4", "5", "6", "7", "8"],
        "Period": ["2", "4", "8", "16", "32", "64", "128", "256"],
        f"Bifurcation parameter (${an}$)": ["0.75", "1.25", "1.3680989", "1.3940462", "1.3996312", "1.4008286", "1.4010853", "1.4011402"],
        f"Ratio ${ratio}$": ["", "", "4.2337", "4.5515", "4.6458", "4.6639", "4.6682", "4.6689"],
    }
)
st.table(df)
