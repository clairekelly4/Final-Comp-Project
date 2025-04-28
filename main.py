from quiz import load_form_data, get_individual_scores
from match import match_students

def main():
    """
    main function to load google form data, match students into groups, and print the final groups
    :return:
    """
    df = load_form_data() # data from google sheet

    students = get_individual_scores(df)

    # asks the user how many students they want per group
    while True:
        try:
            group_size = int(input("How many students per group? (e.g. 3, 4, 5): "))
            if group_size < 2:
                print("Please enter a group size of at least 2.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    groups = match_students(students, group_size)

    print("\nGroup Assignments:")
    for i, group in enumerate(groups, start=1):
        print(f"\nGroup {i}:")
        for name in group:
            print(f" - {name}")


if __name__ == "__main__":
    main()
