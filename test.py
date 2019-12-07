import requests
import time
import re
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

#datetime.now().strftime('%Y/%m/%d') #2019/12/06
Date  = datetime.now().strftime('%Y/%m/%d') #2019/12/06
Date2 = datetime.now().strftime('%Y-%m-%d') #2019-12-06
min   = int(datetime.now().strftime('%M') )
hur   = int(datetime.now().strftime('%H') )
if min >= 30:
    min = '00'
    hur+=1
else:
    min = '00'
Time = str(hur) + ':' +min
print(Time)


form_data = {
    'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
    # 'StartStationName': '台北站',
    'EndStation':'9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
    # 'EndStationName': '台南站',
    'DepartueSearchDate':'2019/12/30',
    'DepartueSearchTime':'15:30',
    'SearchType':'S'
}

url = 'http://www.thsrc.com.tw/tw/TimeTable/Search'
response_post = requests.post(url,data = form_data)


# 用json解析, 並分析資料結構
data = json.loads(response_post.text)
# print(data)
trainItem = data['data']['DepartureTable']['TrainItem']

# 所有班車(train_number)
train_numbers = []
# 所有出發時間(departure_time)
departure_times = []
# 所有到達時間(arrival_time)
arrival_times = []
# 所有行車時間(duration)
duration = []
# 折扣
d_early = []
d_colle = []
d_group = []




for item in trainItem:
    train_numbers.append(item['TrainNumber'])
    departure_times.append(item['DepartureTime'])
    arrival_times.append(item['DestinationTime'])
    duration.append(item['Duration'])
    # early = 0
    # colle = 0
    # group = 0
    # for i in item['Discount']:
    #     if i['Name'] == '早鳥':
    #         d_early.append({'Name':i['Name'],'Value':i['Value']})
    #         early = 1
    #     elif i['Name'] == '大學生':
    #         d_colle.append({'Name':i['Name'],'Value':i['Value']})
    #         colle = 1
    #     elif i['Name'] == '25人團體':
    #         group = 1
    #         d_group.append({'Name':i['Name'],'Value':i['Value']})
        
    # if early == 0:
    #     d_early.append({'Name':'早鳥','Value':"No"})
    # if colle == 0:
    #     d_colle.append({'Name':'大學生','Value':"No"})
    # if group == 0:
    #     d_group.append({'Name':'25人團體','Value':"No"})
                     
        # print("-----------------------------")
    # print("end")
        
    # discount.append(item['Discount'][0][0]['Value'])
# print( discount[0][0]['Value'] )


print( len(d_early) )
print( len(d_colle) )
print( len(d_group) )
highway_df = pd.DataFrame({
    '車次': train_numbers,
    '出發時間': departure_times,
    '到達時間': arrival_times,
    '行車時間': duration,
    },
    columns = ['車次', '出發時間', '到達時間', '行車時間']
)

print(highway_df)





