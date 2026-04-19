def recommend_path(analysis):
    recs = []
    weakest = min(analysis, key=lambda x: analysis[x]["average"])

    resources = {
        "Maths": ("Algebra, Calculus", "maths_notes.pdf", "https://www.youtube.com/watch?v=8mAITcNt710"),
        "ML": ("Regression, Classification", "ml_notes.pdf", "https://www.youtube.com/watch?v=GwIo3gDZCVQ"),
        "OOPS": ("Inheritance, Polymorphism", "oops_notes.pdf", "https://www.youtube.com/watch?v=SiBw7os-_zI"),
        "CN": ("OSI, TCP/IP", "cn_notes.pdf", "https://www.youtube.com/watch?v=qiQR5rTSshw")
    }

    for sub, data in analysis.items():
        avg = data["average"]
        trend = data["trend"]

        topics, pdf, yt = resources[sub]

        if avg < 50:
            action = "Revise basics + practice daily"
        elif trend == "Declining":
            action = "Revise + take mock tests"
        elif trend == "Improving" and avg > 75:
            action = "Move to advanced level"
        else:
            action = "Practice moderate questions"

        recs.append({
            "subject": sub,
            "topics": topics,
            "action": action,
            "pdf": pdf,
            "youtube": yt
        })

    return recs, weakest