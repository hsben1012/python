studentScores = [
    [[87, 90], [80, 88], [91, 82]],
    [[72, 82], [81, 84], [81, 76]],
    [[87, 84], [79, 86], [85, 89]],
    [[88, 85], [82, 83], [71, 68]],
    [[79, 82], [80, 78], [71, 76]],
    [[88, 80], [80, 88], [91, 82]],
    [[87, 90], [70, 77], [91, 96]],
    [[83, 90], [70, 88], [81, 82]]
]

for x in range(len(studentScores)):
    totalScore = 0
    for y in range(len(studentScores[x])):
        print(studentScores[x][y][0], "---", studentScores[x][y][1])
        totalScore += studentScores[x][y][0] * 0.4 + studentScores[x][y][1] * 0.6
    averageScore = totalScore / 3
    print(f"#{x+1}: {averageScore:6.2f}")
    print()
