import os
import time
import urllib.request
import xml.etree.ElementTree as et

pth = 'C:\\Users\\Greg\\Documents\\python_project\\'

os.remove(pth+'F-D0047-093.zip')
#os.path.exists(pth+'F-D0047-093.zip')

url ="http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
urllib.request.urlretrieve(url,pth+'F-D0047-093.zip')

if os.path.exists(pth+'F-D0047-093.zip'):
    tt= os.path.getmtime(pth+'F-D0047-093.zip')
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(tt)))
else:
    print('file not exist')

import zipfile
f=zipfile.ZipFile(pth+'F-D0047-093.zip')
#台北 
for filename in [ '63_72hr_CH.xml']:
#高雄 
# for filename in [ '64_72hr_CH.xml']:
#新北 
# for filename in [ '65_72hr_CH.xml']:
#台中 
# for filename in [ '66_72hr_CH.xml']:
#台南 
# for filename in [ '67_72hr_CH.xml']:
#桃園 
# for filename in [ '68_72hr_CH.xml']:
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
    locationName = ele[0].text # 取得縣市名
#    if locationName == location:
    target_idx = idx

    # 挑選出目前想要 location 的氣象資料
    weather_element = locations_info[target_idx][-1] # 取出 Wx (氣象描述)
    block_of_current_time = weather_element[2] # 取出目前時間點的資料

    startTime = block_of_current_time[0].text
    endTime = block_of_current_time[1].text
    description = block_of_current_time[2][0].text

    print(locationName,startTime[:10],startTime[11:16]+'-'+endTime[11:16],':',description)
