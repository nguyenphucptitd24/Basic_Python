if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append((name, score))
    score_set = set()
    for student in records:
        score_set.add(student[1])
    second_lowest_score = sorted(score_set)[1]
    def custom_sort(student):
        return (student[1], student[0])
    sorted_records = sorted(records, key=custom_sort)
    for student in sorted_records:
        if student[1] == second_lowest_score:
            print(student[0])