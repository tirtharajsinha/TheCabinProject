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
        ['vcgencmd', 'get_config', 'arm_freq']).decode('utf-8').split("\n")[0]
    maxfreq = subprocess.check_output(
        ['cat', '/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq']).decode('utf-8').split("\n")[0]

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
    sto = 0
    for block in allsto:
        if block["name"] == "mmcblk0":
            sto = block["size"]


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
        'cpu_mem_total': memory.total,
        'cpu_mem_avail': memory.available,
        'cpu_mem_used': memory.used,
        'cpu_mem_free': memory.free,
        'disk_usage_total': disk.total,
        'disk_usage_used': disk.used,
        'disk_usage_free': disk.free,
        'disk_usage_percent': disk.percent,
        'sensor_temperatures': getTemp()
    }

    return system_info_data
