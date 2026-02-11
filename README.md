![](microscopi.png)


# Microscopi

**Microscopi** is an open-source digital microscope measurement tool for
Linux.

It allows real-time measurement, calibration, coordinate export and
PCB-oriented workflows using any V4L2 compatible camera (USB
microscopes, webcams, etc).

Designed for precision work in electronics, mechanical prototyping and
laboratory environments.

------------------------------------------------------------------------

## ✨ Features

-   Real-time distance, radius and rectangle measurement
-   XY coordinate measurement
-   Calibration in mm or inches
-   Display units: mm, inch, mil (thousandth of an inch)
-   Configurable precision (0.0 / 0.00 / 0.000)
-   Define custom origin (0,0)
-   Export modes:
    -   PNG (image only)
    -   3D (PNG + CSV in mm)
    -   PCB (PNG + CSV in mil)
-   CSV export includes:
    -   Label
    -   Measurement type
    -   Color code
    -   Coordinates (relative to origin)
    -   Measured value
-   Persistent overlay with visibility toggle
-   UTF-8 text rendering (FreeType)
-   Rotation support (0° / 90° / 180° / 270°)

------------------------------------------------------------------------

## 📦 Dependencies (Debian)

Microscopi requires:

- python3
- python3-opencv (with FreeType support)
- python3-tk
- gettext

Install with:

sudo apt install python3 python3-opencv python3-tk gettext

If OpenCV was built **without FreeType support**, the program will not
start.

------------------------------------------------------------------------


## Installation

### Debian / Ubuntu
Download the .deb from Releases and install:

sudo dpkg -i microscopi_0.9.0-1_amd64.deb
sudo apt -f install

### From source
pip install .

------------------------------------------------------------------------

## 🚀 Running

Basic usage:

    python3 microscopi.py

With custom parameters:

    python3 microscopi.py -d 2 -r 1280x720 -n 2 --unit mm

### Command line options

  Option             Description
  ------------------ ---------------------------------
  `-d`               Video device index (default: 2)
  `-r`               Resolution (e.g. 1280x720)
  `-n`               Number of decimals
  `--unit`           Default unit (mm or in)
  `--no-draw-live`   Disable live preview drawing

------------------------------------------------------------------------

## 📏 Typical Workflow

1.  Rotate image if needed.
2.  Calibrate using a known reference.
3.  Select measurement mode (DIS / RAD / SQR / XY).
4.  Add measurement with label.
5.  Optionally define origin (0,0).
6.  Export using PNG / 3D / PCB.

------------------------------------------------------------------------

## 📂 Export Modes

### PNG

Saves only the current image with visible overlays.

### 3D

Saves: - PNG image - CSV file in millimeters (1 decimal) - Coordinates
relative to origin

### PCB

Saves: - PNG image - CSV file in mil (integer precision) - Coordinates
relative to origin

------------------------------------------------------------------------

## 📄 CSV Format

CSV contains:

    label,type,color,x1,y1,x2,y2,value

Coordinates are: - Relative to defined origin - In mm (3D mode) - In mil
(PCB mode)

------------------------------------------------------------------------

## ⚠ Known Limitations

-   If rotation is changed after measurements are taken, saved overlays
    may not align perfectly.
-   Calibration must be performed before accurate export.

------------------------------------------------------------------------

## 📌 Version

Current version: **0.9.0**

------------------------------------------------------------------------

## 📜 License

MIT License

------------------------------------------------------------------------

## Roadmap

- [x] Debian package
- [x] i18n
- [x] CSV export
- [ ] Geometry improvements
- [ ] Measurement editing
- [ ] Hardware profile presets
- [ ] Debian official submission

------------------------------------------------------------------------

## 👤 Author

Created by Jordi Orts\
Open source contribution inspired by the Debian community.
