// js/solids.js
function createSolid(type) {
  switch (type) {
    case "tetrahedron": return new THREE.TetrahedronGeometry(1);
    case "cube": return new THREE.BoxGeometry(1, 1, 1);
    case "octahedron": return new THREE.OctahedronGeometry(1);
    case "dodecahedron": return new THREE.DodecahedronGeometry(1);
    case "icosahedron": return new THREE.IcosahedronGeometry(1);
    default: return new THREE.TetrahedronGeometry(1); // fallback
  }
}
