
statements = [
    {"statement": "I like having a clear plan before beginning work.", "trait" : "Planner"},
    {"statement": "I like to check in regularly with my group members.", "trait": "Accountable"},
    {"statement": "I like to get started on projects as early as possible.", "trait": "Proactive"},
    {"statement": "I value flexibility and am open to new ideas.", "trait": "Adaptive"},
    {"statement": "I feel most energized when working with other people.", "trait": "Extroverted"},
    {"statement": "I feel more productive when I can work independently.", "trait": "Introverted"},
    {"statement": "I feel stressed if things are unorganized or uncertain.", "trait": "Need For Order"},
    {"statement": "I prefer frequent communication, even for small updates.", "trait": "Communicative"},
    {"statement": "I naturally take the lead in group settings.", "trait": "Leader"},
    {"statement": "I stay calm and composed when there's disagreement.", "trait": "Calm Under Pressure"}
]

def take_quiz(statements: list[dict[str, str]]) -> dict[str, int]:
    """
    Conducts a personality and work-style quiz to assess user traits based on their responses to statements rated on a scale from 1 to 5.
    :param statements: a statement and associated trait
    :return:
    """
    print("Answer on a scale from 1 (Strongly Disagree) to 5 (Strongly Agree)")
    scores: dict[str, int] = {}
    for s in statements:
        trait = s["trait"]
        if trait not in scores:
            scores[trait] = 0

    for s in statements:
        while True:
            try:
                answer: int = int(input(s["statement"] + " "))
                if 1 <= answer <= 5:
                    break
                else:
                    print("Invalid input. Please enter a number 1 to 5.")
            except ValueError:
                print("Invalid input. Please enter a number (1 to 5).")

        scores[s["trait"]] += answer

    return scores


