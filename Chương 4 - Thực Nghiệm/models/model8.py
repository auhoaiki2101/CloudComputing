def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    SPEED_THRESHOLD = 1.0 

    
   # Tính 3 điểm đánh dấu cách đường trung tâm các khoảng cách khác nhau
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Thưởng cao hơn nếu xe gần đường trung tâm hơn và ngược lại
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # có khả năng gặp sự cố / sắp đi chệch hướng

    if not all_wheels_on_track:
		# Phạt nếu xe đi chệch hướng
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
		# Phạt nếu xe đi quá chậm
        reward = reward + 0.5
    else:
		# Thưởng cao nếu xe đi đúng hướng và đi nhanh
        reward = reward + 1.0

    return float(reward)
