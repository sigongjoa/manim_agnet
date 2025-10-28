
// --- Basic Three.js Setup ---
const container = document.getElementById('container');
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x111111);

// Use an orthographic camera to get a 2D Manim-like view
const aspect = window.innerWidth / window.innerHeight;
const frustumSize = 10;
const camera = new THREE.OrthographicCamera(
    frustumSize * aspect / -2,
    frustumSize * aspect / 2,
    frustumSize / 2,
    frustumSize / -2,
    1,
    1000
);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
container.appendChild(renderer.domElement);

// --- Scene Objects (will be populated from JSON) ---
const manimObjects = new THREE.Group();
scene.add(manimObjects);

let sceneData = null;

// --- Interactive Elements ---
const angleSlider = document.getElementById('angle_slider');
const angleLabel = document.querySelector('label[for="angle_slider"]');

let angle = 0; // The main variable controlled by the slider

// --- Helper Functions ---
function createLine(points, color = 0xffffff) {
    const material = new THREE.LineBasicMaterial({ color: color });
    // The points are already in the correct format [[x,y,z], [x,y,z], ...]
    // We need to flatten the array and create a BufferAttribute.
    const geometry = new THREE.BufferGeometry();
    const vertices = new Float32Array(points.flat());
    geometry.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
    return new THREE.Line(geometry, material);
}

// --- Load Scene Data and Initialize ---
fetch('scene_data.json')
    .then(response => response.json())
    .then(data => {
        sceneData = data;
        drawStaticScene(data);
        setupInteractiveElements(data);
        animate();
    });

function drawStaticScene(data) {
    // Manim uses a different coordinate system, so we adjust the camera
    camera.position.set(0, 0, 5);
    camera.lookAt(scene.position);

    // Draw Unit Circle and its axes
    const uc = data.unit_circle;
    const circleGeo = new THREE.BufferGeometry().setFromPoints(
        new THREE.Path().absarc(uc.center[0], uc.center[1], uc.radius, 0, Math.PI * 2, false).getPoints(90)
    );
    const circle = new THREE.Line(circleGeo, new THREE.LineBasicMaterial({ color: 0x448aff }));
    manimObjects.add(circle);
    manimObjects.add(createLine([uc.x_axis.start, uc.x_axis.end], 0xaaaaaa));
    manimObjects.add(createLine([uc.y_axis.start, uc.y_axis.end], 0xaaaaaa));

    // Draw Sine Graph and its axes
    const sg = data.sine_graph;
    manimObjects.add(createLine(sg.points, 0xffc107)); // Yellow sine wave
    manimObjects.add(createLine([sg.x_axis.start, sg.x_axis.end], 0xaaaaaa));
    manimObjects.add(createLine([sg.y_axis.start, sg.y_axis.end], 0xaaaaaa));
}

let interactiveElements = null;

function setupInteractiveElements(data) {
    const uc = data.unit_circle;

    const pointOnCircle = new THREE.Mesh(
        new THREE.CircleGeometry(0.08, 32),
        new THREE.MeshBasicMaterial({ color: 0xffffff })
    );

    const radiusLine = createLine([
        uc.center,
        [uc.center[0] + uc.radius, uc.center[1], 0]
    ], 0xffffff);

    const sinLine = createLine([
        [uc.center[0], uc.center[1]],
        [uc.center[0], uc.center[1]]
    ], 0xf44336); // Red for Sine

    const cosLine = createLine([
        [uc.center[0], uc.center[1]],
        [uc.center[0], uc.center[1]]
    ], 0x2196f3); // Blue for Cosine

    const pointOnSine = new THREE.Mesh(
        new THREE.CircleGeometry(0.08, 32),
        new THREE.MeshBasicMaterial({ color: 0xffffff })
    );
    
    const connectLine = createLine([
        [0,0,0], [0,0,0]
    ], 0xaaaaaa);
    connectLine.material.transparent = true;
    connectLine.material.opacity = 0.5;

    interactiveElements = {
        pointOnCircle,
        radiusLine,
        sinLine,
        cosLine,
        pointOnSine,
        connectLine
    };

    Object.values(interactiveElements).forEach(obj => manimObjects.add(obj));
}

function updateScene(angle) {
    if (!sceneData || !interactiveElements) return;

    const uc = sceneData.unit_circle;
    const sg = sceneData.sine_graph;
    const rad = angle * (Math.PI / 180);

    // Update Unit Circle elements
    const x_pos = uc.center[0] + uc.radius * Math.cos(rad);
    const y_pos = uc.center[1] + uc.radius * Math.sin(rad);
    interactiveElements.pointOnCircle.position.set(x_pos, y_pos, 0);

    const radiusPositions = interactiveElements.radiusLine.geometry.attributes.position;
    radiusPositions.setXYZ(0, uc.center[0], uc.center[1], 0);
    radiusPositions.setXYZ(1, x_pos, y_pos, 0);
    radiusPositions.needsUpdate = true;

    const sinLinePos = interactiveElements.sinLine.geometry.attributes.position;
    sinLinePos.setXYZ(0, x_pos, y_pos, 0);
    sinLinePos.setXYZ(1, x_pos, uc.center[1], 0);
    sinLinePos.needsUpdate = true;

    const cosLinePos = interactiveElements.cosLine.geometry.attributes.position;
    cosLinePos.setXYZ(0, x_pos, y_pos, 0);
    cosLinePos.setXYZ(1, uc.center[0], y_pos, 0);
    cosLinePos.needsUpdate = true;

    // Update Sine Graph elements
    const sine_x = sg.origin[0] + rad;
    const sine_y = sg.origin[1] + Math.sin(rad) * uc.radius;
    interactiveElements.pointOnSine.position.set(sine_x, sine_y, 0);
    
    // Update connecting line
    const connectLinePos = interactiveElements.connectLine.geometry.attributes.position;
    connectLinePos.setXYZ(0, x_pos, y_pos, 0);
    connectLinePos.setXYZ(1, sine_x, sine_y, 0);
    connectLinePos.needsUpdate = true;
}

// --- Animation Loop ---
function animate() {
    requestAnimationFrame(animate);
    
    const currentAngle = parseFloat(angleSlider.value);
    angle = currentAngle;
    angleLabel.textContent = `θ = ${(angle * (2*Math.PI/360)).toFixed(2)} rad`;
    updateScene(angle);

    renderer.render(scene, camera);
}

// --- Handle Window Resize ---
window.addEventListener('resize', () => {
    const aspect = window.innerWidth / window.innerHeight;
    camera.left = frustumSize * aspect / -2;
    camera.right = frustumSize * aspect / 2;
    camera.top = frustumSize / 2;
    camera.bottom = frustumSize / -2;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}, false);
