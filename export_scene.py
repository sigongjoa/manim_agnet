
import json
import numpy as np
from manim import *

def get_scene_data():
    """
    Uses Manim objects to define a scene and returns its geometric data as a dictionary.
    This data will be exported as JSON for use in a web frontend.
    """
    # Define scene boundaries and parameters
    x_min, x_max = -8, 8
    y_min, y_max = -4, 4
    sine_x_start, sine_x_end = 0, 2 * PI
    n_points_sine = 360

    # --- 1. Unit Circle on the left ---
    circle_center = [-4, 0, 0]
    circle_radius = 1.5
    unit_circle = Circle(radius=circle_radius).move_to(circle_center)
    
    # Axes for the unit circle
    circle_x_axis = Line(
        unit_circle.get_center() + [ -circle_radius - 0.5, 0, 0],
        unit_circle.get_center() + [ circle_radius + 0.5, 0, 0],
        stroke_width=2
    )
    circle_y_axis = Line(
        unit_circle.get_center() + [0, -circle_radius - 0.5, 0],
        unit_circle.get_center() + [0,  circle_radius + 0.5, 0],
        stroke_width=2
    )

    # --- 2. Sine Graph on the right ---
    graph_origin = [1, 0, 0]
    
    # Pre-calculate points for the sine wave
    sine_points = []
    for i in range(n_points_sine + 1):
        angle = (i / n_points_sine) * sine_x_end
        x = graph_origin[0] + angle
        y = graph_origin[1] + np.sin(angle) * circle_radius # Scale sine wave by circle radius
        sine_points.append([x, y, 0])

    # Axes for the sine graph
    graph_x_axis = Line(
        [graph_origin[0], graph_origin[1], 0],
        [graph_origin[0] + sine_x_end + 0.5, graph_origin[1], 0],
        stroke_width=2
    )
    graph_y_axis = Line(
        [graph_origin[0], graph_origin[1] - circle_radius - 0.5, 0],
        [graph_origin[0], graph_origin[1] + circle_radius + 0.5, 0],
        stroke_width=2
    )
    
    # --- 3. Structure data for JSON export ---
    scene_data = {
        "unit_circle": {
            "center": unit_circle.get_center().tolist(),
            "radius": unit_circle.radius,
            "x_axis": {
                "start": circle_x_axis.get_start().tolist(),
                "end": circle_x_axis.get_end().tolist()
            },
            "y_axis": {
                "start": circle_y_axis.get_start().tolist(),
                "end": circle_y_axis.get_end().tolist()
            }
        },
        "sine_graph": {
            "origin": graph_origin,
            "points": sine_points,
            "x_axis": {
                "start": graph_x_axis.get_start().tolist(),
                "end": graph_x_axis.get_end().tolist()
            },
            "y_axis": {
                "start": graph_y_axis.get_start().tolist(),
                "end": graph_y_axis.get_end().tolist()
            }
        }
    }
    
    return scene_data

if __name__ == "__main__":
    data = get_scene_data()
    # Print the JSON data to stdout
    print(json.dumps(data, indent=4))
