class Workout:
    def __init__(self):
        self.body_parts = {
            "chest": ["Push-ups", "Bench press", "Dumbbell flys"],
            "back": ["Pull-ups", "Lat pulldown", "Bent over rows"],
            "shoulders": ["Shoulder press", "Dumbbell raises", "Upright rows"],
            "arms": ["Bicep curls", "Tricep extensions", "Hammer curls"],
            "legs": ["Squats", "Lunges", "Deadlifts"],
            "core": ["Crunches", "Plank", "Russian twists"],
        }
        self.workout_log = []

    def choose_body_part(self):
        print("Body parts: chest, back, shoulders, arms, legs, core")
        choice = input("Choose a body part to workout: ").lower()
        if choice in self.body_parts:
            return choice
        else:
            print("Invalid body part. Please choose from the listed options.")
            return self.choose_body_part()

    def choose_exercise(self, body_part):
        print(f"Exercises for {body_part}: {', '.join(self.body_parts[body_part])}")
        choice = input("Choose an exercise: ").lower()
        if choice in [exercise.lower() for exercise in self.body_parts[body_part]]:
            return [exercise for exercise in self.body_parts[body_part] if exercise.lower() == choice][0]
        else:
            print("Invalid exercise. Please choose from the listed options.")
            return self.choose_exercise(body_part)

    def get_sets_reps_weight(self):
        sets = input("Enter the number of sets: ")
        reps = input("Enter the number of reps: ")
        weight = input("Enter the weight used: ")
        return {"sets": sets, "reps": reps, "weight": weight}

    def log_workout(self, body_part, exercise):
        sets_reps_weight = self.get_sets_reps_weight()
        self.workout_log.append((body_part, exercise, sets_reps_weight))
        print(
            f"{exercise} for {body_part} with sets: {sets_reps_weight['sets']}, reps: {sets_reps_weight['reps']}, weight: {sets_reps_weight['weight']} has been added to your workout log.")

    def start(self):
        while True:
            body_part = self.choose_body_part()
            exercise = self.choose_exercise(body_part)
            self.log_workout(body_part, exercise)
            repeat = input("Would you like to add another exercise? (yes/no) ").lower()
            if repeat != "yes":
                print("No exercises have been logged.")
                print()
                break

        if self.workout_log:
            print("Workout Log:")
            for body_part, exercise, sets_reps_weight in self.workout_log:
                print(f"{exercise} for {body_part} with sets: {sets_reps_weight['sets']}, reps: {sets_reps_weight['reps']}, weight: {sets_reps_weight['weight']}")


def main():
    workout = Workout()
    workout.start()


if __name__ == "__main__":
    workout = Workout()
    workout.start()