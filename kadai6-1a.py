import requests

APP_ID = "f115604c2cffd332562ba2c788990d649c9d1d4e"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"#エンドポイント
params = {
    "appId": APP_ID,
    "statsDataId":"0003440002",#年度別の全国の旅客人（単位：キロ
    "cdArea":"00000",
    "cdCat01": "100",
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)