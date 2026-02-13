import json
import tkinter as tk
from tkinter import messagebox
from .i18n import _

VALID_TYPES = {"DIS", "RAD", "SQR", "XY"}


def validate_measure(m):

    if not isinstance(m, dict):
        raise ValueError("Each measure must be an object")

    required = {"label", "type", "points", "color", "visible"}

    if not required.issubset(m.keys()):
        raise ValueError("Missing required fields")

    if not isinstance(m["label"], str):
        raise ValueError("Label must be string")

    if m["type"] not in VALID_TYPES:
        raise ValueError("Invalid type")

    if not isinstance(m["points"], list):
        raise ValueError("Points must be list")

    if m["type"] == "XY":
        if len(m["points"]) not in (1, 2):
            raise ValueError("XY must have 1 or 2 points")
    else:
        if len(m["points"]) != 2:
            raise ValueError("Measure must have exactly 2 points")

    for p in m["points"]:
        if not isinstance(p, list) or len(p) != 2:
            raise ValueError("Each point must be [x,y]")

        if not all(isinstance(v, int) for v in p):
            raise ValueError("Point coordinates must be integers")

    if not (isinstance(m["color"], list) and len(m["color"]) == 3):
        raise ValueError("Color must be [r,g,b]")

    if not all(isinstance(c, int) for c in m["color"]):
        raise ValueError("Color values must be integers")

    if not isinstance(m["visible"], bool):
        raise ValueError("Visible must be true/false")


def open_measure_editor(state):

    root = tk.Tk()
    root.title(_("Measure editor"))
    root.geometry("700x500")

    text = tk.Text(
        root,
        font=("Courier", 10),
        bg="#1e1e1e",
        fg="#e0e0e0",
        insertbackground="#ffffff",   # color del cursor
        selectbackground="#444444",
        selectforeground="#ffffff"
    )
    text.pack(fill=tk.BOTH, expand=True)

    text.insert("1.0", json.dumps(state.measurements, indent=2))

    def apply_changes():
        try:
            content = text.get("1.0", tk.END)
            new_data = json.loads(content)

            if not isinstance(new_data, list):
                raise ValueError("Root must be a list")

            for m in new_data:
                validate_measure(m)

            state.measurements = new_data
            state.status_message = _("Measures updated")

            root.destroy()

        except Exception as e:
            messagebox.showerror(_("Invalid JSON"), str(e))

    frame = tk.Frame(root)
    frame.pack(fill=tk.X)

    btn_apply = tk.Button(frame, text=_("Apply"), command=apply_changes)
    btn_apply.pack(side=tk.LEFT, padx=5, pady=5)

    btn_cancel = tk.Button(frame, text=_("Cancel"), command=root.destroy)
    btn_cancel.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()
