import math

def get_direction_using_geo_points(p1_lat, p1_long, p2_lat, p2_long):
	delta_p1 = p2_lat - p1_lat
	delta_p2 = p2_long - p1_long
	geo_points_in_degrees = math.atan2(delta_p1, delta_p2) * (180//math.pi)
	if geo_points_in_degrees < 0:
		final_geo_points_degree = 360 + geo_points_in_degree
	else:
		final_geo_points_degree = geo_points_in_degrees
	direction_short_names = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
	direction_lookup = int(round(final_geo_points_degree/45))
	print(direction_short_names[direction_lookup], final_geo_points_degree)
	return direction_short_names[direction_lookup], final_geo_points_degree

get_direction_using_geo_points(30.510,40.112,50.11,80.0221)

		



