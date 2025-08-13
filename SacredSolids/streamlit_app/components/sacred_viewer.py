import os
import streamlit.components as components

def show_3d_viewer(solid_name=None):
    """
    Loads and embeds the Three.js viewer from index.html.
    Optionally injects a script to initialize a specific solid.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.join(base_dir, "..", "threejs_visuals", "index.html")
    viewer_path = os.path.normpath(raw_path)

    if not os.path.exists(viewer_path):
        raise FileNotFoundError(f"Viewer HTML not found at: {viewer_path}")

    with open(viewer_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Optional: Inject solid name into viewer via JS
    if solid_name:
        injection = f"""
        <script>
            if (typeof createSolid === 'function') {{
                createSolid("{solid_name.lower()}");
            }}
        </script>
        """
        html_content += injection

    components.html(html_content, height=600, scrolling=False)
