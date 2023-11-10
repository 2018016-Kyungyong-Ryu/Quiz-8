import pandas as pd
import numpy as np

indexing = [1,2,3,4,5]
column = ["이름", '나이', '성별']
data = np.array([['한상우', '김영동', '김민성', '이웅섭', '박태형'], [26,23,23,22,23], ['남', '남', '남', '남', '남']]).transpose()

df= pd.DataFrame(data, index=indexing, columns=column)
input_number = int(input("숫자를 입력하세요 : "))

print(df)
