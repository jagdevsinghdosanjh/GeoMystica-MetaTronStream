# setup.ps1
$root = "SacredSolids"

$folders = @(
    "$root/streamlit_app/components",
    "$root/streamlit_app/utils",
    "$root/threejs_visuals/js",
    "$root/threejs_visuals/css",
    "$root/assets/images",
    "$root/assets/symbols"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder -Force
}

# Create placeholder files
New-Item -Path "$root/streamlit_app/main.py" -ItemType File -Force
New-Item -Path "$root/streamlit_app/utils/geometry.py" -ItemType File -Force
New-Item -Path "$root/threejs_visuals/index.html" -ItemType File -Force
New-Item -Path "$root/threejs_visuals/css/styles.css" -ItemType File -Force
New-Item -Path "$root/setup.ps1" -ItemType File -Force
New-Item -Path "$root/README.md" -ItemType File -Force
