# Sau khi điều chỉnh tốc độ và góc lái của xe
def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    # Đọc thông số đầu vào
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Chỉ cần góc lái tuyệt đối
    speed = params['speed']
    is_left_of_center = params['is_left_of_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
    progress = params['progress']
    
    reward = 0.0
    

    if(is_left_of_center == True):
        reward *= 5.0
        
    else:
        reward -= 5.0

    if(distance_from_center <= track_width / 2):
        reward += 2.0
        
    else:
        reward -= 1e-3

    TOTAL_NUM_STEPS = 500

    # Tặng thêm phần thưởng nếu xe chạy nhanh hơn dự kiến mỗi 100 bước
    if ((steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100) :
        reward += 10.0

    SPEED_THRESHOLD = 7.0

    if not all_wheels_on_track:
        # Phạt nếu xe đi chệch hướng
        reward -= 1e-3
    elif speed < SPEED_THRESHOLD:
        # Phạt nếu ô tô đi quá chậm
        reward += 1.55 
    else:
        # Thưởng cao nếu xe đi đúng hướng và đi nhanh
        reward *= 2.0



    # Ngưỡng phạt lái, thay đổi số dựa trên cài đặt không gian hành động của bạn
    ABS_STEERING_THRESHOLD = 30

    # Thưởng phạt nếu xe bẻ lái quá nhiều
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.7

    return float(reward)
