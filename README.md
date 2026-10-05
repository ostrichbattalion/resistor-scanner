# Resistor Scanner

A computer-vision tool that reads the colour bands on a through-hole resistor from
an image or a live camera feed and calculates its resistance value.

## How it works

1. Isolate the resistor body and sample a line across the colour bands.
2. Classify each band colour against the standard resistor colour code.
3. Decode the band sequence into a resistance value (with tolerance).
4. Optionally overlay the reading on a live video feed (HUD).

## Files

- `resistor_scanner.py` — main detection and decoding pipeline
- `color_classifier.py` — maps sampled pixels to colour-code bands
- `video_capture_and_HUD.py` — live camera feed with an on-screen readout
- `new_graphs.py` — visual debugging of the colour sampling

## Running

```bash
pip install opencv-python numpy matplotlib
python resistor_scanner.py          # single image
python video_capture_and_HUD.py     # live camera
```

A small computer-vision project built while studying — OpenCV, colour-space work
and real-world image noise.
