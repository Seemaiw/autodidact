def get_direction_using_geo_points(p1_lat, p1_long, p2_lat, p2_long):
	delta_p1 = p2_lat - p1_lat
	delta_p2 = p2_long - p2_long
	// changing the points into angle, first Math.atan2(delta_p1, delta_p2) change the value into radian and (180/Math.PI changes it into degree)
	geo_points_in_degrees = Math.atan2(delta_p1, delta_p2) * (180/Math.PI)
	if geo_points_in_degrees < 0:
		final_geo_points_degree = 360 + geo_points_in_degree
	else:
		final_geo_points_degree = geo_points_in_degrees

		



