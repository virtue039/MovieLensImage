import pandas as pd
import requests


# 随机ip代理获取
url = 'http://localhost:5555/all'
res = requests.get(url)
data = pd.DataFrame()

data.to_csv('./url.txt', sep='\n', index=False)
