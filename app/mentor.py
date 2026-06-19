def get_mentor_advice(weak_subject, trend, goal):

    advice = f"Your weakest subject is {weak_subject} and the trend is {trend}.\n\n"

    if weak_subject == "Maths":
        advice += "Focus on Algebra and Calculus.\n\n"

    elif weak_subject == "ML":
        advice += "Practice Regression and Classification concepts.\n\n"

    elif weak_subject == "OOPS":
        advice += "Revise Inheritance and Polymorphism.\n\n"

    elif weak_subject == "CN":
        advice += "Strengthen OSI and TCP/IP concepts.\n\n"

    if goal == "AI Engineer":
        advice += "Since your goal is AI Engineer, build a strong foundation in Mathematics and Machine Learning."

    elif goal == "Data Scientist":
        advice += "Since your goal is Data Scientist, focus on Statistics, Python and Data Analysis."

    elif goal == "Software Engineer":
        advice += "Since your goal is Software Engineer, strengthen DSA, OOP and DBMS."

    elif goal == "Web Developer":
        advice += "Since your goal is Web Developer, focus on HTML, CSS, JavaScript and Flask."

    else:
        advice += "Since your goal is Data Analyst, focus on SQL, Excel and Power BI."

    return advice