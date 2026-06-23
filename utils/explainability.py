def explain(subject):

    reasons = []

    subject_lower = subject.lower()

    if "urgent" in subject_lower:
        reasons.append("Contains urgency keyword")

    if "exclusive" in subject_lower:
        reasons.append("Contains exclusivity keyword")

    if "update" in subject_lower:
        reasons.append("Contains update-related wording")

    if "opportunity" in subject_lower:
        reasons.append("Highlights an opportunity")

    if "action required" in subject_lower:
        reasons.append("Encourages immediate action")

    if "follow-up" in subject_lower:
        reasons.append("Indicates continued communication")

    if "last chance" in subject_lower:
        reasons.append("Creates scarcity")

    if "don't miss" in subject_lower:
        reasons.append("Creates urgency and attention")

    if "discuss" in subject_lower:
        reasons.append("Encourages engagement")

    if "?" in subject:
        reasons.append("Creates curiosity")

    if len(subject) < 60:
        reasons.append("Concise subject line")

    return reasons