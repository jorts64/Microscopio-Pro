import cv2
import math

from .constants import LEFT_MENU_W
from .utils import current_measure_text, draw_text


def draw_preview(canvas, state):

    if not state.config.draw_live:
        return

    if len(state.points) < 1 or not state.cursor_pos:
        return

    x1, y1 = state.points[0]

    if len(state.points) == 2:
        x2, y2 = state.points[1]
    else:
        cx, cy = state.cursor_pos
        x2 = cx - LEFT_MENU_W
        y2 = cy

    # Ajustar desplazamiento para canvas
    x1 += LEFT_MENU_W
    x2 += LEFT_MENU_W

    if state.mode == "DIS":
        cv2.line(canvas, (x1, y1), (x2, y2),
                 state.measure_color, 2)

    elif state.mode == "RAD":
        r = int(math.hypot(x2 - x1, y2 - y1))
        cv2.circle(canvas, (x1, y1), r,
                   state.measure_color, 2)

    elif state.mode == "SQR":
        cv2.rectangle(canvas,
                      (min(x1, x2), min(y1, y2)),
                      (max(x1, x2), max(y1, y2)),
                      state.measure_color, 2)

    if len(state.points) == 2:
        text = current_measure_text(state)
        if text:
            draw_text(canvas, text,
                      (x2 + 6, y2),
                      20, state.measure_color)
