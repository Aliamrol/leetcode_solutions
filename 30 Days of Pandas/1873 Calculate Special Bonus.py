import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != 'M')
    employees['bonus'] = mask * employees['salary']
    return employees[['employee_id', 'bonus']].sort_values('employee_id')
