import matplotlib.pyplot as plt

# Example x_coordinate range (replace with your actual pixel positions)
x_coordinate = list(range(10, 160))

# Color dictionary with light and dark RGB tuples
colors = {
    "black": {"light": (0, 0, 0), "dark": (20, 20, 20)},
    "brown": {"light": (156, 102, 51), "dark": (71, 53, 38)},
    "red": {"light": (255, 0, 0), "dark": (204, 0, 0)},
    "orange": {"light": (255, 102, 0), "dark": (255, 51, 0)},
    "yellow": {"light": (255, 255, 0), "dark": (255, 204, 102)},
    "green": {"light": (0, 255, 0), "dark": (30, 200, 50)},
    "blue": {"light": (0, 0, 255), "dark": (40, 73, 86)},
    "violet": {"light": (200, 0, 255), "dark": (110, 0, 51)},
    "gray": {"light": (128, 128, 128), "dark": (73, 65, 62)},
    "white": {"light": (255, 255, 255), "dark": (250, 250, 250)},
}

# Create figure and 3 subplots for R, G, B channels stacked vertically
fig, (axR, axG, axB) = plt.subplots(3, 1, sharex=True, figsize=(12, 10))

# To assign slightly different shades for dark lines to distinguish from light lines
dark_line_colors = {
    "black": "#141414",
    "brown": "#473526",
    "red": "#cc0000",
    "orange": "#ff3300",
    "yellow": "#ffcc66",
    "green": "#1ec832",
    "blue": "#284956",
    "violet": "#6e0033",
    "gray": "#49413e",
    "white": "#fafafa",
}

# Plot each color for each channel
for color_name, rgb_vals in colors.items():
    # Unpack light and dark RGB values
    light = rgb_vals["light"]
    dark = rgb_vals["dark"]

    # Repeat the values across all x positions
    R_light = [light[0]] * len(x_coordinate)
    G_light = [light[1]] * len(x_coordinate)
    B_light = [light[2]] * len(x_coordinate)

    R_dark = [dark[0]] * len(x_coordinate)
    G_dark = [dark[1]] * len(x_coordinate)
    B_dark = [dark[2]] * len(x_coordinate)

    # Plot red channel
    axR.plot(x_coordinate, R_light, label=f'{color_name} light', color=f'{color_name}')
    axR.plot(x_coordinate, R_dark, label=f'{color_name} dark', color=dark_line_colors[color_name])
    axR.fill_between(x_coordinate, R_dark, R_light, color=color_name, alpha=0.2)

    # Plot green channel
    axG.plot(x_coordinate, G_light, label=f'{color_name} light', color=f'{color_name}')
    axG.plot(x_coordinate, G_dark, label=f'{color_name} dark', color=dark_line_colors[color_name])
    axG.fill_between(x_coordinate, G_dark, G_light, color=color_name, alpha=0.2)

    # Plot blue channel
    axB.plot(x_coordinate, B_light, label=f'{color_name} light', color=f'{color_name}')
    axB.plot(x_coordinate, B_dark, label=f'{color_name} dark', color=dark_line_colors[color_name])
    axB.fill_between(x_coordinate, B_dark, B_light, color=color_name, alpha=0.2)

# Set labels and titles
axR.set_ylabel('Red Intensity')
axR.set_title('Red Channel')
axG.set_ylabel('Green Intensity')
axG.set_title('Green Channel')
axB.set_ylabel('Blue Intensity')
axB.set_title('Blue Channel')
axB.set_xlabel('Pixel Position')

# Optional: Add legends (can be large with many lines)
# To avoid overcrowding, show legends only for the first color or disable them
# axR.legend(loc='upper right', fontsize='small')
# axG.legend(loc='upper right', fontsize='small')
# axB.legend(loc='upper right', fontsize='small')

plt.tight_layout()
plt.show()
