def template_generator(
    keywords,
    intent,
    tone,
    audience
):

    if not keywords:
        keywords = ["opportunity"]

    keyword = keywords[0]

    intent = str(intent).strip().lower()

    # -------------------------
    # JOB APPLICATION
    # -------------------------
    if "job" in intent or "application" in intent:

        return [
            f"Application for {keyword}",
            f"{keyword} Application",
            f"Resume Attached – {keyword}",
            f"Applying for {keyword}",
            f"Interest in {keyword}",
            f"Application Submission for {keyword}",
            f"{keyword} Position Application",
            f"Application for {keyword} Role",
            f"Candidate Application – {keyword}",
            f"Regarding {keyword} Application"
        ]

    # -------------------------
    # FOLLOW UP
    # -------------------------
    elif "follow" in intent:

        return [
            f"Following Up on {keyword}",
            f"Quick Follow-Up Regarding {keyword}",
            f"Checking In About {keyword}",
            f"Follow-Up: {keyword}",
            f"Revisiting {keyword}",
            f"Status Update on {keyword}",
            f"Regarding Our Discussion on {keyword}",
            f"Continued Interest in {keyword}",
            f"Awaiting Feedback on {keyword}",
            f"Following Up Regarding {keyword}"
        ]

    # -------------------------
    # REQUEST
    # -------------------------
    elif "request" in intent:

        return [
            f"Request Regarding {keyword}",
            f"Seeking Assistance with {keyword}",
            f"Could You Review {keyword}?",
            f"Request for Feedback on {keyword}",
            f"Need Your Input on {keyword}",
            f"Support Required for {keyword}",
            f"Question Regarding {keyword}",
            f"Requesting Information About {keyword}",
            f"Guidance Needed for {keyword}",
            f"Seeking Clarification on {keyword}"
        ]

    # -------------------------
    # ANNOUNCEMENT
    # -------------------------
    elif "announcement" in intent:

        return [
            f"Project Update: {keyword}",
            f"Latest Update on {keyword}",
            f"Progress Report: {keyword}",
            f"Status Update: {keyword}",
            f"Recent Developments in {keyword}",
            f"Important Announcement Regarding {keyword}",
            f"Update and Next Steps for {keyword}",
            f"Sharing Progress on {keyword}",
            f"{keyword} Progress Update",
            f"Key Milestones for {keyword}"
        ]

    # -------------------------
    # MARKETING
    # -------------------------
    elif "marketing" in intent:

        return [
            f"New {keyword} Opportunity",
            f"Discover {keyword}",
            f"Introducing {keyword}",
            f"Explore {keyword} Today",
            f"Special Offer: {keyword}",
            f"Exclusive Access to {keyword}",
            f"Don't Miss {keyword}",
            f"Limited Time: {keyword}",
            f"See What's New in {keyword}",
            f"Unlock {keyword}"
        ]

    # -------------------------
    # DEFAULT
    # -------------------------
    else:

        return [
            f"Important Update About {keyword}",
            f"Regarding {keyword}",
            f"Update on {keyword}",
            f"Information About {keyword}",
            f"Discussion Regarding {keyword}",
            f"Status of {keyword}",
            f"Latest News About {keyword}",
            f"Insights on {keyword}",
            f"Overview of {keyword}",
            f"Key Information Regarding {keyword}"
        ]