# score_file = open("score.txt", "w", encoding="utf8")
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end=" ")
print(score_file.readline(), end=" ")
print(score_file.readline(), end=" ")
print(score_file.readline(), end=" ")
score_file.close()