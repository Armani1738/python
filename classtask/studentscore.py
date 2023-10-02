def average_score(scores):
    return sum(scores) / len(scores)

exam_scores = []
for i in range(10):
    score = int(input("Enter the score: "))
    exam_scores.append(score)

    print(average_score(exam_scores))
average_score()