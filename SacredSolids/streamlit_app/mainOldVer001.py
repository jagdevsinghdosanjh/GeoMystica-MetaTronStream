import streamlit as st
import numpy as np
import plotly.graph_objects as go
from pathlib import Path
from sympy import Eq
from sympy.abc import V, E, F

from components.sacred_viewer import show_3d_viewer
from components.solid_selector import get_solid, symbolic_description
from components.solid_selector import select_solid

# --- Page Setup ---
st.set_page_config(page_title="SacredSolids", layout="wide")

# --- Custom CSS Injection ---
css_path = Path("assets/styles.css")
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)
else:
    st.warning("Custom styles not found.")

# --- Optional UI Extras ---
try:
    from streamlit_extras.add_vertical_space import add_vertical_space
except ImportError:
    def add_vertical_space(n): st.write("\n" * n)

add_vertical_space(1)

# --- Title ---
st.markdown('<h1 class="main-title">SacredSolids: Platonic Geometry Explorer</h1>', unsafe_allow_html=True)

# --- Solid Selection ---
solid_name = st.sidebar.selectbox("Choose a Platonic Solid", ["Tetrahedron", "Cube", "Octahedron", "Dodecahedron"])
vertices, faces = get_solid(solid_name)

# --- 3D Viewer Embed ---
try:
    show_3d_viewer(solid_name)
except FileNotFoundError as e:
    st.error(f"3D viewer not found: {e}")

# --- Plotly Visualization ---
def plot_solid(vertices, faces, name):
    fig = go.Figure()

    for face in faces:
        face_vertices = vertices[face]
        x, y, z = face_vertices[:, 0], face_vertices[:, 1], face_vertices[:, 2]
        x = np.append(x, x[0])
        y = np.append(y, y[0])
        z = np.append(z, z[0])
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(color='royalblue', width=4),
            name="Face"
        ))

    fig.add_trace(go.Scatter3d(
        x=vertices[:, 0], y=vertices[:, 1], z=vertices[:, 2],
        mode='markers',
        marker=dict(size=5, color='orange'),
        name='Vertices'
    ))

    fig.update_layout(
        title=f"{name} Visualization",
        margin=dict(l=0, r=0, b=0, t=40),
        scene=dict(aspectmode='data')
    )
    return fig

# --- Symbolic Description ---
if vertices is not None:
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    fig = plot_solid(vertices, faces, solid_name)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    eq, values = symbolic_description(solid_name)
    st.subheader("Symbolic Description")
    st.latex(eq)
    st.write(f"Vertices (V): {values.get('V')}, Edges (E): {values.get('E')}, Faces (F): {values.get('F')}")

st.markdown("---")
st.caption("Built with 🔷 by Jagdev Singh Dosanjh")
