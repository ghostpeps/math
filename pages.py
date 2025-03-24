import streamlit as st

latex_exp = "e^{i\\pi}"
pgs = st.navigation([
  st.Page(page="pi.py", title="π"),
  st.Page(page="e.py", title="_e_"),
  st.Page(page="phi.py", title="Φ"),
  st.Page(page="eipi.py", title=f"${latex_exp}$")
])
pgs.run()
