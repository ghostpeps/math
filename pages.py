import streamlit as st

exp = st.latex(r"e^{i\pi}")
pgs = st.navigation([
  st.Page(page="pi.py", title="π"),
  st.Page(page="e.py", title="e"),
  st.Page(page="phi.py", title="Φ"),
  st.Page(page="eipi.py", title=exp)
])
pgs.run()
