def classify_hazard(front, left, right, down):
    if down > 120:
        return "drop", "rapid_pulse_both"
    elif front < 20:
        return "front_critical", "fast_both"
    elif front < 50:
        return "front_danger", "medium_both"
    elif left < 50:
        return "left_danger", "medium_left"
    elif right < 50:
        return "right_danger", "medium_right"
    else:
        return "safe", "none"
