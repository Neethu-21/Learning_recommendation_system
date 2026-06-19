def recommend_path(analysis, goal, study_time):

    recs = []

    weakest = min(
        analysis,
        key=lambda x: analysis[x]["average"]
    )

    resources = {
        "Maths": (
            "Algebra, Calculus",
            "maths_notes.pdf",
            "https://www.youtube.com/watch?v=8mAITcNt710"
        ),
        "ML": (
            "Regression, Classification",
            "ml_notes.pdf",
            "https://www.youtube.com/watch?v=GwIo3gDZCVQ"
        ),
        "OOPS": (
            "Inheritance, Polymorphism",
            "oops_notes.pdf",
            "https://www.youtube.com/watch?v=SiBw7os-_zI"
        ),
        "CN": (
            "OSI, TCP/IP",
            "cn_notes.pdf",
            "https://www.youtube.com/watch?v=qiQR5rTSshw"
        )
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

    # ---------------- ROADMAP ----------------

    # ---------------- ROADMAP ----------------

    if goal == "Data Scientist":

        if study_time == "1 Hour":
            roadmap = [
                "Week 1 → Python Fundamentals",
                "Week 2 → Statistics",
                "Week 3 → NumPy",
                "Week 4 → Machine Learning Basics"
        ]

        elif study_time == "2 Hours":
            roadmap = [
                "Week 1 → Python + Statistics",
                "Week 2 → NumPy + Pandas",
                "Week 3 → Data Visualization",
                "Week 4 → Machine Learning Basics"
        ]

        else:
            roadmap = [
                "Week 1 → Python + Statistics + NumPy",
                "Week 2 → Pandas + Visualization",
                "Week 3 → Machine Learning",
                "Week 4 → End-to-End Data Science Project"
        ]


    elif goal == "AI Engineer":

        if study_time == "1 Hour":
            roadmap = [
                "Week 1 → Python",
                "Week 2 → Mathematics",
                "Week 3 → Machine Learning",
                "Week 4 → Deep Learning Basics"
        ]

        elif study_time == "2 Hours":
            roadmap = [
                "Week 1 → Python + Math",
                "Week 2 → Machine Learning",
                "Week 3 → Deep Learning",
                "Week 4 → Neural Networks"
        ]

        else:
            roadmap = [
                "Week 1 → Python + Math + NumPy",
                "Week 2 → Machine Learning",
                "Week 3 → Deep Learning + TensorFlow",
                "Week 4 → AI Mini Project"
        ]


    elif goal == "Software Engineer":

        if study_time == "1 Hour":
            roadmap = [
                "Week 1 → Data Structures",
                "Week 2 → OOP Concepts",
                "Week 3 → DBMS",
                "Week 4 → Problem Solving"
        ]

        elif study_time == "2 Hours":
            roadmap = [
                "Week 1 → Data Structures",
                "Week 2 → OOP + DBMS",
                "Week 3 → Operating Systems",
                "Week 4 → Mini Project"
        ]

        else:
            roadmap = [
                "Week 1 → DSA Intensive",
                "Week 2 → DBMS + OS",
                "Week 3 → System Design Basics",
                "Week 4 → Full Project Development"
        ]


    elif goal == "Web Developer":

        if study_time == "1 Hour":
            roadmap = [
                "Week 1 → HTML",
                "Week 2 → CSS",
                "Week 3 → JavaScript",
                "Week 4 → Flask Basics"
        ]

        elif study_time == "2 Hours":
            roadmap = [
                "Week 1 → HTML + CSS",
                "Week 2 → JavaScript",
                "Week 3 → Flask",
                "Week 4 → Deployment"
            ]

        else:
            roadmap = [
                "Week 1 → HTML CSS JavaScript",
                "Week 2 → Flask",
                "Week 3 → Database Integration",
                "Week 4 → Full Stack Project"
            ]


    else:  # Data Analyst

        if study_time == "1 Hour":
            roadmap = [
                "Week 1 → Excel",
                "Week 2 → SQL",
                "Week 3 → Power BI",
                "Week 4 → Dashboards"
            ]

        elif study_time == "2 Hours":
            roadmap = [
                "Week 1 → Excel + SQL",
                "Week 2 → Power BI",
                "Week 3 → Data Cleaning",
                "Week 4 → Analytics Project"
            ]

        else:
            roadmap = [
                "Week 1 → Excel + SQL + Power BI",
                "Week 2 → Data Visualization",
                "Week 3 → Analytics Case Studies",
                "Week 4 → End-to-End Analytics Project"
            ]
    return recs, weakest, roadmap