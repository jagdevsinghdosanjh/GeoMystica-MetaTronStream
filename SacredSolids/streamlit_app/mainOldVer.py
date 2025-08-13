import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import symbols, Eq # noqa
from sympy.abc import V, E, F # noqa

from components.sacred_viewer import show_3d_viewer
from components.solid_selector import get_solid, symbolic_description
from components.solid_selector import select_solid # noqa
#print("Selected solid:", select_solid("cube"))

# --- Page Setup ---
st.set_page_config(page_title="SacredSolids", layout="wide")
st.title("🔷 SacredSolids: Platonic Geometry Explorer")

# --- Custom CSS ---
try:
    with open("./assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Custom styles not found.")

# --- Optional UI Extras ---
try:
    from streamlit_extras.add_vertical_space import add_vertical_space
except ImportError:
    def add_vertical_space(n): st.write("\n" * n)

add_vertical_space(1)

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
    fig = plot_solid(vertices, faces, solid_name)
    st.plotly_chart(fig, use_container_width=True)

    eq, values = symbolic_description(solid_name)
    st.subheader("🔣 Symbolic Description")
    st.latex(eq)
    st.write(f"Vertices (V): {values.get('V')}, Edges (E): {values.get('E')}, Faces (F): {values.get('F')}")

    st.markdown("---")
    st.caption("Built with ❤️ by Jagdev Singh Dosanjh")
