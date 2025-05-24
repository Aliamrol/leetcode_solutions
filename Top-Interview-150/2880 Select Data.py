import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student = students[students['student_id']==101].drop(columns=['student_id'])
    return student
    # student = students.loc[students['student_id']==101, ['name', 'age']]
    # return student

# The first approach which has not commented is faster than second approach.