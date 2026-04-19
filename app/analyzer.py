def analyze_student(df, student_id):
    student_data = df[df["student_id"] == student_id]

    result = {}

    for subject in student_data["subject"].unique():
        sub = student_data[student_data["subject"] == subject].sort_values("test_no")

        scores = sub["score"].tolist()
        avg = sum(scores)/len(scores)

        if scores[-1] > scores[0]:
            trend = "Improving"
        elif scores[-1] < scores[0]:
            trend = "Declining"
        else:
            trend = "Stable"

        result[subject] = {
            "scores": scores,
            "average": avg,
            "trend": trend
        }

    return result