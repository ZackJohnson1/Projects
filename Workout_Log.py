import datetime

unformated_date = datetime.date.today()
today = unformated_date.strftime("%m/%d/%Y")

class Workout:
    def __init__(self):
        """This function initializes body_parts, key_words and workouk_log...body_parts defines a dictionary containing
        the different body parts and their respective exercises...exercise keywords defines a dictionary containing
        keyword-exercise pairs for all the exercises listed in the body_parts dictionary...workout_log is list that will store
        tuples of the form (body_part, exercise, sets_reps_weight, volume) for each workout that gets logged"""

        self.body_parts = {
            "chest": ["Push-ups", "Bench press", "Incline Bench press", "Dumbbell flys", "Dips"],
            "back": ["Pull-ups", "Lat pulldown", "Bent over rows"],
            "shoulders": ["Overhead press", "Dumbbell raises", "Upright rows"],
            "arms": ["Bicep curls", "Tricep extensions", "Hammer curls"],
            "legs": ["Squats", "Lunges", "Deadlifts"],
            "core": ["Crunches", "Plank", "Russian twists"],
        }

        self.exercise_keywords = {
            "push-ups": "Push-ups",
            "bench press": "Bench press",
            "bp": "Bench press",
            "incline bench press": "Incline Bench press",
            "dumbbell flys": "Dumbbell flys",
            "dips": "Dips",
            "pull-ups": "Pull-ups",
            "lat pulldown": "Lat pulldown",
            "bent over rows": "Bent over rows",
            "overhead press": "Overhead press",
            "dumbbell raises": "Dumbbell raises",
            "upright rows": "Upright rows",
            "bicep curls": "Bicep curls",
            "tricep extensions": "Tricep extensions",
            "hammer curls": "Hammer curls",
            "squats": "Squats",
            "lunges": "Lunges",
            "deadlifts": "Deadlifts",
            "crunches": "Crunches",
            "plank": "Plank",
            "russian twists": "Russian twists"
        }

        self.workout_log = []

    def choose_body_part(self):
        """This function prompts the user to choose a body part from a list of available options"""
        print("Body parts: chest, back, shoulders, arms, legs, core")
        print()
        choice = input("Choose a body part to workout: ").lower()
        print()
        if choice in self.body_parts:
            return choice
        else:
            print("Invalid body part. Please choose from the listed options.")
            return self.choose_body_part()

    def choose_exercise(self, body_part):
        print(f"Exercises for {body_part}: {', '.join(self.body_parts[body_part])}")
        choice = input("Choose an exercise: ").lower()
        if choice in self.exercise_keywords:
            return self.exercise_keywords[choice]
        else:
            print("Invalid exercise. Please choose from the listed options.")
            return self.choose_exercise(body_part)

    def get_sets_reps_weight(self):
        try:
            sets = int(input("Enter the number of sets: "))
            reps = int(input("Enter the number of reps: "))
            weight = int(input("Enter the weight used: "))
            return {"sets": sets, "reps": reps, "weight": weight}
        except ValueError:
            print("ERROR: Integers only!")
            return self.get_sets_reps_weight()
b
    def get_volume(self, sets, reps, weight):
        return int(sets) * int(reps) * int(weight)

    def get_total_volume(self):
        total_volume = 0
        for body_part, exercise, sets_reps_weight, volume in self.workout_log:
            total_volume += volume
        return total_volume

    def log_workout(self, body_part, exercise):
        sets_reps_weight = self.get_sets_reps_weight()
        self.workout_log.append((body_part, exercise, sets_reps_weight, self.get_volume(sets_reps_weight['sets'], sets_reps_weight['reps'], sets_reps_weight['weight'])))
        print(f"{exercise} for {body_part} with sets: {sets_reps_weight['sets']}, reps: {sets_reps_weight['reps']}, weight: {sets_reps_weight['weight']} has been added to your workout log.")

    def start(self):
        while True:
            body_part = self.choose_body_part()
            exercise = self.choose_exercise(body_part)
            self.log_workout(body_part, exercise)
            repeat = input("Would you like to add another exercise? (Y/N) ").lower()
            if repeat != "y":
                break

        if self.workout_log:
            print(f"Workout Log for {today}: ")
            total_volume = 0
            if self.workout_log:
                for body_part, exercise, sets_reps_weight, volume in self.workout_log:
                    print(f"{exercise} for {body_part} with sets: {sets_reps_weight['sets']}, reps: {sets_reps_weight['reps']}, weight: {sets_reps_weight['weight']}, volume: {volume}")
                    total_volume += volume
            print(f"Total Volume: {total_volume}")

def main():
    workout = Workout()
    workout.start()

if __name__ == "__main__":
    workout = Workout()
    workout.start()
