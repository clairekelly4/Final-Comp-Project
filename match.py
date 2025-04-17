def compute_personality_scores(answers):
    # answers is list of first 10 quiz responses on 1-5 scale
    planning     = (answers[0] + answers[5]) / 2
    leadership   = (answers[1] + answers[6]) / 2
    time_mgmt    = (answers[2] + answers[7]) / 2
    collaboration= (answers[3] + answers[8]) / 2
    presentation = (answers[4] + answers[9]) / 2
    return {
        'planning': planning,
        'leadership': leadership,
        'time_mgmt': time_mgmt,
        'collaboration': collaboration,
        'presentation': presentation
    }

def match_users(users, group_size=4, course_code=None):
    # filter users by course code if provided
    eligible = [
        u for u in users
        if course_code is None or u.get('course') == course_code
    ]
    # compute personality traits for each eligible user
    for u in eligible:
        u['traits'] = compute_personality_scores(u['answers'][:10])
    # sort users by their trait values
    eligible.sort(key=lambda u: tuple(u['traits'].values()))
    # chunk sorted users into groups of desired size
    groups = [
        eligible[i:i+group_size]
        for i in range(0, len(eligible), group_size)
    ]
    # simple pass-through, could enforce skill diversity here
    return groups