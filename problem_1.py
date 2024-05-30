#Not Boring Movies leetcode 620

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    result=[]
    for i in range(len(cinema)):
        if ((cinema.iloc[i]['id']%2 !=0) & (cinema.iloc[i]['description'] != 'boring')):
            result.append(cinema.iloc[i])
    if len(result)==0:
            return pd.DataFrame([], columns= ['id', 'movie', 'description', 'rating'])
    return pd.DataFrame(result, columns= ['id', 'movie', 'description', 'rating']).sort_values('rating', ascending= False)

#short method
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema['id'] %2 != 0) & (cinema['description'] != 'boring')]
    return df.sort_values('rating', ascending= False)