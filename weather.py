import urllib.request
import json
import time
import sys

req = urllib.request.Request("http://d1.weather.com.cn/satellite2015/JC_YT_DL_WXZXCSYT_4A.html?jsoncallback=readSatellite&callback=jQuery18208455971171376718_" + str(round(time.time() * 1000)) + "&_=" + str(round(time.time() * 1000)))
req.add_header('Referer', 'http://www.weather.com.cn/satellite/')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')

with urllib.request.urlopen(req) as f:
    data = f.read().decode('utf-8')
    data = data[14:-1]
    j = json.loads(data.replace('\'','\"'))
    for a in j['radars']:
        print(a['ft'])
        urllib.request.urlretrieve("http://pi.weather.com.cn/i/product/pic/l/sevp_nsmc_" + a['fn'] + "_lno_py_" + a['ft'] + ".jpg", sys.path[0] + "/weather/" + a['ft'] + ".jpg")