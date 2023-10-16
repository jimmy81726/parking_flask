import requests
from datetime import datetime


# 即時取得opendata,處理成所需要的資訊
def get_parkinginfo(sort=None):
    url = "https://hispark.hccg.gov.tw/OpenData/GetParkInfo"
    resp = requests.get(url)
    datas = resp.json()
    values = []
    for data in datas:
        values.append((list(data.values())))
    # values為二維串列包含opendata的所有資訊
    all_values = []
    numbers = [1, 2, 3, 4, 5, 8, 9, 10, 11, 20]
    # 利用numbers當引子只取自己所需要的資訊
    for value in values:
        eachpark_list = []
        for i in numbers:
            # 時間格式需要修改所以另外處理
            if i == 20:
                time_str = value[i].split(".")
                time = time_str[0]
                time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
                eachpark_list.append(time)
            else:
                eachpark_list.append(value[i])
        # 多一行作為之後當連結去評論頁面
        eachpark_list.append("評論")
        all_values.append(eachpark_list)
    # 當選擇不同的,會將回傳的串列值做排序
    if sort == 1:
        all_values = sorted(all_values, key=lambda x: x[5], reverse=True)
    elif sort == 2:
        all_values = sorted(all_values, key=lambda x: x[7], reverse=True)
    columns = [
        "停車場名",
        "地址",
        "營運時間",
        "平日收費方式",
        "假日收費方式",
        "汽車剩餘車位",
        "汽車總車位",
        "機車剩餘車位",
        "機車總車位",
        "最後更新時間",
        "評論",
    ]
    return all_values, columns
