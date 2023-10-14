import requests


def get_parkinginfo():
    url = "https://hispark.hccg.gov.tw/OpenData/GetParkInfo"
    resp = requests.get(url)
    datas = resp.json()
    values = []
    for data in datas:
        values.append((list(data.values())))
    all_values = []
    numbers = [1, 2, 3, 4, 5, 8, 9, 10, 11, 20]
    for value in values:
        eachpark_list = []
        for i in numbers:
            eachpark_list.append(value[i])
        all_values.append(eachpark_list)
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
    ]
    return all_values, columns
