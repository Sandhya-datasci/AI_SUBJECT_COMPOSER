def compare_subjects(subject_a, subject_b, ranked):

    scores = dict(ranked)

    score_a = scores.get(subject_a, 0)
    score_b = scores.get(subject_b, 0)

    if score_a > score_b:
        winner = subject_a

    elif score_b > score_a:
        winner = subject_b

    else:
        winner = "Tie"

    confidence = round(
        abs(score_a - score_b),
        2
    )

    return winner, confidence