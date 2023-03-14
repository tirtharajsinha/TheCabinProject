import subprocess
import os
import psutil
import json


def getTemp():
    temp = subprocess.check_output(
        ['vcgencmd', 'measure_temp']).decode('utf-8').split("\n")[0]
    temp = temp.replace("temp=", "").replace("'C", "°C")
    return temp


def cpuLoad():
    return os.getloadavg()[0]


def getCpuFreq():
    freq = subprocess.check_output(
        ['vcgencmd', 'measure_clock arm']).decode('utf-8').split("\n")[0]
    freq = freq.split("=")[1]
    freq = int(freq)//1000000

    maxfreq = subprocess.check_output(
        ['vcgencmd', 'get_config', 'arm_freq']).decode('utf-8').split("\n")[0]
    maxfreq = maxfreq.split("=")[1]

    return [freq, maxfreq]


def getUptime():
    # uptime
    with open('/proc/uptime', 'r') as f:
        upseconds = float(f.readline().split()[0])
    minutes, seconds = divmod(upseconds, 60)
    hours, minutes = divmod(minutes, 60)

    if upseconds < 60:
        up = "1 min"
    elif hours > 0:
        up = "{}:{} hrs".format(int(hours), int(minutes))
    else:
        up = "{} min".format(minutes)
    return up


def getIp():
    ip = subprocess.check_output(
        ['hostname', '-I']).decode('utf-8').split("\n")[0]
    return ip


def getSSID():
    ssid = subprocess.check_output(
        ['iwgetid', '-r']).decode('utf-8').split("\n")[0]
    if len(ssid) > 11:
        ssid = ssid[:11]
    return ssid


def getServiceDetails():

    # all services
    totalser = os.popen("systemctl list-units | wc -l").read()
    totalser = int(totalser)-7

    # all failed services
    totalfailser = os.popen(
        "systemctl list-units --state failed | wc -l").read()
    totalfailser = int(totalfailser)-6

    return {"totalservices": totalser, "failedservice": totalfailser}


def getStorageDevices():
    # storage

    allsto = subprocess.check_output(['lsblk', '--json']).decode('utf-8')
    allsto = json.loads(allsto)
    allsto = allsto["blockdevices"]

    external = 0
    boot = 0
    for block in allsto:
        for ch in block["children"]:
            if ch["mountpoint"] == "/boot":
                esize = ch["size"]
                if esize[-1] == "M":
                    boot += float(esize[:-1])/1024
                elif esize[-1] == "G":
                    boot += float(esize[:-1])
            elif ch["mountpoint"] == "/":
                esize = ch["size"]
                if esize[-1] == "M":
                    boot += float(esize[:-1])/1024
                elif esize[-1] == "G":
                    boot += float(esize[:-1])
            else:
                esize = ch["size"]
                if esize[-1] == "M":
                    external += float(esize[:-1])/1024
                elif esize[-1] == "G":
                    external += float(esize[:-1])

    if boot < 100:
        boot = round(boot, 2)
    else:
        boot = round(boot, 1)

    if external < 100:
        external = round(external, 2)
    else:
        external = round(external, 1)

    return {
        "internal": boot,
        "extarnal": external
    }


def getEachCpuUsage():
    cpudata = psutil.cpu_percent(interval=2, percpu=True)
    cdata = {}
    for i, data in enumerate(cpudata):
        cdata["core"+str(i+1)] = data
    return cdata


def getUserInfo():
    hostname = os.popen("hostname").read()
    username = os.popen("echo $USER").read()

    data = {
        "hostname": hostname,
        "username": username
    }

    return data


def pidata():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    cpuFreq = getCpuFreq()
    system_info_data = {
        'cpu_percent': psutil.cpu_percent(1),
        'cpu_count': psutil.cpu_count(),
        'cpu_freq': cpuFreq[0],
        'max_cpu_freq': cpuFreq[1],
        'cpu_mem_total': round(int(memory.total)/(1000)**3, 1),
        'cpu_mem_avail': round(int(memory.available)/(1000)**3, 1),
        'cpu_mem_used': round(int(memory.used)/(1000)**3, 1),
        'cpu_mem_free': round(int(memory.free)/(1000)**3, 1),
        'cpu_mem_percent': round((memory.available/memory.total)*100, 0),
        'disk_usage_total': round(int(disk.total)/(1000)**3, 1),
        'disk_usage_used': round(int(disk.used)/(1000)**3, 1),
        'disk_usage_free': round(int(disk.free)/(1000)**3, 1),
        'disk_usage_percent': disk.percent,
        'sensor_temperatures': getTemp(),
        'ip_address': getIp(),
        'totalservices': getServiceDetails()["totalservices"],
        'ssid': getSSID(),
        "storage_devices": getStorageDevices()
    }

    return system_info_data


def pidataReload():
    memory = psutil.virtual_memory()
    cpuFreq = getCpuFreq()
    system_info_data = {
        'cpu_percent': psutil.cpu_percent(1),
        'cpu_freq': cpuFreq[0],

        'cpu_mem_avail': round(int(memory.available)/(1000)**3, 1),
        'cpu_mem_used': round(int(memory.used)/(1000)**3, 1),
        'cpu_mem_free': round(int(memory.free)/(1000)**3, 1),
        'cpu_mem_percent': round((memory.available/memory.total)*100, 0),

        'sensor_temperatures': getTemp()

    }

    return system_info_data
