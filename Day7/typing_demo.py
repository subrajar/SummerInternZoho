from typing import Dict
studentDict = Dict[str, str]


def validation(student: studentDict) -> bool:
    for student_ID, student_Name in student.items():
        if (not isinstance(student_ID, str)) or (not isinstance(student_Name, str)):
            return False
    return True


print(validation({'10232': 'Michael Bing'}))
print(validation({'12232': 'David Jones', 12345: 'Jenny Morgan'}))