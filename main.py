from quiz import load_form_data, get_individual_scores
from match import match_students, score_pair
from dataclasses import dataclass, asdict
import json

@dataclass
class Group: #defines data structure for group
    group_name: str
    members: list

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
    for i, group in enumerate(groups):
        print(f"\nGroup {i + 1}:")

        # get full student objects for names in the group
        group_members = [s for s in students if s["name"] in group]

        # calculate total group compatibility score (sum of all pair scores)
        group_score = 0
        for idx, member1 in enumerate(group_members):
            for member2 in group_members[idx + 1:]:
                group_score += score_pair(member1, member2)

        print(f"Group Compatibility Score: {group_score}")

        for name in group: #prints name of students in the group
            print(f" {name}")

    group_objects = [ #creates a list of group objects
        Group(group_name=f"Group {i+1}", members = group) #creates a group object for every group that is looped through, and sets members of the group
        for i, group in enumerate(groups) #repeat this for each group
    ]

    #saves group assignments into JSON file by converting dataclass to dictionary

    groups_dict_list = [asdict(group) for group in group_objects] #converts group objects into dicts

    with open("group_assignments.json", "w") as f: #save group assignments into JSON file
        json.dump(groups_dict_list, f, indent=1) #uses indents to be more user-friendly

if __name__ == "__main__":
    main()
