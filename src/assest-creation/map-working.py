import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# ---------------------------
# Define locations here
# name: (longitude, latitude)
# ---------------------------
locations = {
    "Barcelona, Spain": (-2.1, 41.4),              # Madrid approx (or adjust to Badalona ~2.25, 41.45)
    "Plymouth, UK": (-4.14, 50.37),
    "Cambridge, UK": (0.12, 52.20),
    "Miami, USA": (-80.19, 25.76),
    "Minnesota, USA": (-94.72, 46.68),
}

# ---------------------------
# Create figure
# ---------------------------
fig = plt.figure(figsize=(12, 6), facecolor="#25272b")
ax = plt.axes(projection=ccrs.Robinson())
ax.set_facecolor("none")

# ---------------------------
# Draw map (white land)
# ---------------------------
ax.add_feature(cfeature.LAND, facecolor="white", edgecolor="white")
ax.add_feature(cfeature.OCEAN, facecolor="none")

# Remove borders/gridlines for cleaner look
ax.set_global()

# ---------------------------
# Plot locations
# ---------------------------
for name, (lon, lat) in locations.items():
    ax.plot(
        lon, lat,
        marker='o',
        markersize=7,
        markeredgecolor='#00ffe5',
        markerfacecolor='#00ffe5',
        transform=ccrs.PlateCarree()
    )

# ---------------------------
# Show plot
# ---------------------------
plt.tight_layout()
plt.show()

# ---------------------------
# Export
# ---------------------------
plt.savefig("working-map.png",
            dpi=300,
            facecolor=fig.get_facecolor(),
            bbox_inches='tight')