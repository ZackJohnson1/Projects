def calculate_bodypart_volume(exercise_volumes, bodypart):
    total_volume = 0
    for exercise, volume in exercise_volumes.items():
        if exercise in bodypart_exercise_mapping and bodypart_exercise_mapping[exercise] == bodypart:
            total_volume += volume
    return total_volume

# A mapping of exercise to bodypart
bodypart_exercise_mapping = {
    "planks": "core",
    "crunches": "core",
    "squats": "legs",
    "deadlifts": "legs",
    "push ups": "upper body",
    "pull ups": "upper body",
}

# Example usage
exercise_volumes = {
    "planks": 200,
    "crunches": 200,
    "squats": 100,
    "deadlifts": 100,
    "push ups": 100,
    "pull ups": 100,
}

core_volume = calculate_bodypart_volume(exercise_volumes, "core")
legs_volume = calculate_bodypart_volume(exercise_volumes, "legs")
upper_body_volume = calculate_bodypart_volume(exercise_volumes, "upper body")

print(f"Core volume: {core_volume}")
print(f"Legs volume: {legs_volume}")
print(f"Upper body volume: {upper_body_volume}")
