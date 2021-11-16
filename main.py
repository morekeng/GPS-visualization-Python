from gps_class import GPSVis

vis = GPSVis(data_path='Updated_GPS_14.csv',
             map_path='map.png',  # Path to map downloaded from the OSM.
             points=(51.53125, -0.06740, 51.52840, -0.05841)) # Two coordinates of the map (upper left, lower right)

vis.create_image(color=(0, 0, 255), width=3)  # Set the color and the width of the GNSS tracks.
vis.plot_map(output='save')

print()
