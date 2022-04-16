from typing import Dict

studentDict = Dict[str, str]


def validation(student: studentDict) -> bool:
    for student_ID, student_Name in student.items():
        if student_ID == '102':
            return False
    return True


print(validation({'10232': 'Michael Bing'}))
print(validation({'12232': 'David Jones', 12345: 'Jenny Morgan'}))
