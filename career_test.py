import json

class CareerPsychometricTest:
    def __init__(self):
        self.questions = self.load_questions()
        self.categories = [
            "Realistic",
            "Investigative",
            "Artistic",
            "Social",
            "Enterprising",
            "Conventional",
        ]
        self.results = {category: 0 for category in self.categories}

    def load_questions(self):
        """Define or load questions for the assessment."""
        return [
            {
                "question": "I enjoy building or repairing things with my hands.",
                "weights": {"Realistic": 2},
            },
            {
                "question": "Solving complex problems or puzzles excites me.",
                "weights": {"Investigative": 2},
            },
            {
                "question": "I like expressing myself through art, music, or writing.",
                "weights": {"Artistic": 2},
            },
            {
                "question": "Helping and teaching others is very fulfilling to me.",
                "weights": {"Social": 2},
            },
            {
                "question": "I am motivated by leading projects and persuading people.",
                "weights": {"Enterprising": 2},
            },
            {
                "question": "I prefer tasks that involve organizing information and details.",
                "weights": {"Conventional": 2},
            },
        ]

    def run_test(self):
        """Run the assessment interactively."""
        print("\nCareer Interest Psychometric Test")
        print("Rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree)\n")
        options = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]

        for i, q in enumerate(self.questions, 1):
            print(f"{i}. {q['question']}")
            for idx, option in enumerate(options, 1):
                print(f"   {idx}. {option}")
            while True:
                try:
                    choice = int(input("Your answer (1-5): "))
                    if 1 <= choice <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Enter a number.")
            for category, weight in q["weights"].items():
                self.results[category] += (choice - 3) * weight

    def get_result(self):
        """Display the dominant career interest area."""
        dominant = max(self.results.items(), key=lambda x: x[1])[0]
        descriptions = {
            "Realistic": "You enjoy hands-on activities and working with tools or machines.",
            "Investigative": "You thrive on analyzing information and solving problems.",
            "Artistic": "You are creative and enjoy self-expression through various art forms.",
            "Social": "You feel fulfilled when helping, teaching, or supporting others.",
            "Enterprising": "You like leading and persuading people to achieve goals.",
            "Conventional": "You prefer structured tasks and working with data or details.",
        }

        print("\nYour Scores:")
        for cat, score in self.results.items():
            print(f"{cat}: {score}")
        print(f"\nSuggested Career Interest: {dominant}")
        print(descriptions[dominant])

if __name__ == "__main__":
    test = CareerPsychometricTest()
    test.run_test()
    test.get_result()
