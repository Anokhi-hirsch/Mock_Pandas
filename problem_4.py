import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['order_date']=orders['order_date'].dt.year
    orders= orders[orders['order_date']==2019]
    df = orders.groupby('buyer_id').size().reset_index(name='orders_in_2019')
    df = users.merge(df, left_on= 'user_id', right_on='buyer_id', how='left')
    df['orders_in_2019']= df['orders_in_2019'].fillna(0).astype(int)
    df=df[['user_id', 'join_date', 'orders_in_2019']]
    return df.rename(columns={'user_id': 'buyer_id'})

#other method
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    order_2019= orders[orders['order_date'].dt.year==2019]
    order_count=order_2019.groupby('buyer_id').count().reset_index().rename(columns={'order_id':'orders_in_2019'})
    result=users.merge(order_count,left_on='user_id',right_on='buyer_id', how='left')
    result['orders_in_2019']=result['orders_in_2019'].fillna(0)
    return result[['user_id', 'join_date', 'orders_in_2019']].rename(columns={'user_id':'buyer_id'})