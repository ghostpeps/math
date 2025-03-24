import streamlit as st

pgs = st.navigation([
  st.Page(page="pi.py", title="π"),
  st.Page(page="e.py", title="_e_"),
  st.Page(page="phi.py", title="Φ"),
  st.Page(page="eipi.py", title="e^iπ")
])
pgs.run()
