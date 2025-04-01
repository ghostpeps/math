import streamlit as st

pages = [
  st.Page(page="pi.py", title="𝜋"),
  st.Page(page="e.py", title="𝑒"),
  st.Page(page="phi.py", title="Φ"),
  st.Page(page="eipi.py", title="𝑒^i𝜋"),
  st.Page(page="sqrt2.py", title="√2"),
  st.Page(page="i.py", title="i"),
  st.Page(page="y.py", title="γ"),
  st.Page(page="zeta3.py", title="ζ(3)"),
  st.Page(page="g.py", title="G"),
  st.Page(page="a.py", title="α"),
  st.Page(page="d.py", title="δ"),
  st.Page(page="omega.py", title="Ω"),
  st.Page(page="h.py", title="h"),
  st.Page(page="l.py", title="L"),
  st.Page(page="c.py", title="c"),
  st.Page(page="k.py", title="k"),
  st.Page(page="tau.py", title="τ"),
  st.Page(page="ii.py", title="iⁱ"),
  st.Page(page="alephnull.py", title="ℵ₀"),
  st.Page(page="two-to-the-power-of-alephnull.py", title="2^ℵ₀"),
  st.Page(page="ieipi.py", title="i𝑒^i𝜋")
]
pgs = st.navigation(pages)
pgs.run()
