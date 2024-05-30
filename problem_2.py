#Biggest Single Number leetcode 619

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    dictionary={}
    for i in range(len(my_numbers)):
        number = my_numbers.iloc[i]['num']
        if number not in dictionary:
            dictionary[number] = 1
        else:
            dictionary[number] +=1
    result = []
    for key, value in dictionary.items():
        if value ==1:
            result.append(key)
    result.sort(reverse= True)
    if len(result)== 0:
        return pd.DataFrame([None], columns= [ 'num'])
    return pd.DataFrame([result[0]], columns= ['num'])

#shorter way
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    singleOccurence= my_numbers.groupby('num')['num'].transform(len)==1
    df = my_numbers[singleOccurence].sort_values('num', ascending= False)
    if len(df) == 0:
        return pd.DataFrame([None], columns= [ 'num'])
    return pd.DataFrame([df.iloc[0]])