import urllib.request, json 

sensors = [5331 , 7789, 8554, 8733, 15462, 17079]
vals = []
for s in sensors:
    addr = "http://api.luftdaten.info/static/v1/sensor/{sensor}/".format(sensor=s)
    with urllib.request.urlopen(addr) as url:
        data = json.loads(url.read().decode())
        print(data)
