import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])][['name']].rename(columns={'name':'Customers'})
    return df



    # result = customers.merge(orders, how = 'left', left_on = 'id', right_on = 'customerId')
    # return result[result['customerId'].isna()][['name']].rename(columns={'name':'Customers'})

    