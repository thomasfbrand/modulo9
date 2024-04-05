def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
    progress = params['progress']
    speed = params['speed']

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    SPEED_THRESHOLD = 1.5

    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3 
    
        
    if not all_wheels_on_track:
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        reward = 0.5
    else:
        reward = 1.0

    TOTAL_NUM_STEPS = 300

    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0
    
    return float(reward)