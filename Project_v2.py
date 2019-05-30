import os
import time
import urllib.request
import xml.etree.ElementTree as et

#pth = 'D:\\Python_Project\\'
pth = './'

#os.remove(pth+'F-D0047-093.zip')
#os.path.exists(pth+'F-D0047-093.zip')
print('鄉鎮天氣預報-全臺灣各鄉鎮市區預報資料')
print('更新資料中...')
url ="http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
urllib.request.urlretrieve(url,pth+'F-D0047-093.zip')

if os.path.exists(pth+'F-D0047-093.zip'):
    tt= os.path.getmtime(pth+'F-D0047-093.zip')
    print('資料時間:',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(tt)))
else:
    print('file not exist')

import zipfile
f=zipfile.ZipFile(pth+'F-D0047-093.zip')

class weather:
	def __init__(self):
		pass
	
	def ask_city(self):
		print('請選擇地區編號 1~22 或 0 離開: ')
		print(' 1.台北市  2.高雄市  3.新北市  4.台中市  5.台南市  6.桃園市')
		print(' 7.宜蘭縣  8.新竹縣  9.苗栗縣 10.彰化縣 11.南投縣 12.雲林縣')
		print('13.嘉義縣 14.屏東縣 15.臺東縣 16.花蓮縣 17.澎湖縣 18.基隆市')
		print('19.新竹市 20.嘉義市 21.連江縣 22.金門縣')		
	
	def print_weather(self,myCity):
		# 1.台北市  2.高雄市  3.新北市  4.台中市  5.台南市  6.桃園市
		# 7.宜蘭縣  8.新竹縣  9.苗栗縣 10.彰化縣 11.南投縣 12.雲林縣
		#13.嘉義縣 14.屏東縣 15.臺東縣 16.花蓮縣 17.澎湖縣 18.基隆市
		#19.新竹市 20.嘉義市 21.連江縣 22.金門縣
	 
		xml={'1':'63_72hr_CH.xml','2':'64_72hr_CH.xml','3':'65_72hr_CH.xml','4':'66_72hr_CH.xml','5':'67_72hr_CH.xml','6':'68_72hr_CH.xml','7':'10002_72hr_CH.xml','8':'10004_72hr_CH.xml','9':'10005_72hr_CH.xml','10':'10007_72hr_CH.xml','11':'10008_72hr_CH.xml','12':'10009_72hr_CH.xml','13':'10010_72hr_CH.xml','14':'10013_72hr_CH.xml','15':'10014_72hr_CH.xml','16':'10015_72hr_CH.xml','17':'10016_72hr_CH.xml','18':'10017_72hr_CH.xml','19':'10018_72hr_CH.xml','20':'10020_72hr_CH.xml','21':'09007_72hr_CH.xml','22':'09020_72hr_CH.xml'}

		cityname={'1':'台北市','2':'高雄市','3':'新北市','4':'台中市','5':'台南市','6':'桃園市','7':'宜蘭縣','8':'新竹縣','9':'苗栗縣','10':'彰化縣','11':'南投縣','12':'雲林縣','13':'嘉義縣','14':'屏東縣','15':'臺東縣','16':'花蓮縣','17':'澎湖縣','18':'基隆市','19':'新竹市','20':'嘉義市','21':'連江縣','22':'金門縣'}
		
		print(cityname[myCity],'各區域天氣預報如下：')

		for filename in [xml[myCity]]:
			try:
				report = f.read(filename)
			except:
				break
		f.close()

		xml_namespace = "{urn:cwb:gov:tw:cwbcommon:0.1}"
		root = et.fromstring(report)
		dataset = root.find(xml_namespace + 'dataset')
		locations = dataset.find(xml_namespace + 'locations')
		locations_info = locations.findall(xml_namespace + 'location')

		target_idx = -1
		for idx,ele in enumerate(locations_info):
			locationName = ele[0].text # 取得區名
			target_idx = idx

			# 挑選出目前 location 的氣象資料
			weather_element = locations_info[target_idx][-1] # 取出 Wx (氣象描述)
			block_of_current_time = weather_element[2] # 取出目前時間點的資料

			startTime = block_of_current_time[0].text
			endTime = block_of_current_time[1].text
			description = block_of_current_time[2][0].text

			print(locationName,startTime[:10],startTime[11:16]+'-'+endTime[11:16],':',description)

			
while True:
	myWeather = weather()
	myWeather.ask_city()
	myCity = input()
	try:
		if eval(myCity) == 0:
			break
		elif eval(myCity) in range(1,22+1):
			myWeather.print_weather(myCity)
	except:
		pass
