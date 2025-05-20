import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    dataframe = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return dataframe