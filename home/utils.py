import subprocess
import os
import psutil
import json


def mainsysteminfo1():
    # measures temp, cpu freq, memory, usage,uptime

    #temp
    temp=subprocess.check_output(['vcgencmd','measure_temp']).decode('utf-8').split("\n")[0]
    temp=temp.replace("temp=","").replace("'C","°C")

    #freq
    cfreq=subprocess.check_output(['vcgencmd','measure_clock','arm']).decode('utf-8').split("\n")[0]
    cfreq=cfreq.split("=")[-1]
    cfreq=int(cfreq) // 1000000
    cfreq=str(cfreq)+"MHz"

    # usage
    usage=os.getloadavg()[0]
    


    #mem
    memT=subprocess.check_output(['grep','MemTotal' ,'/proc/meminfo']).decode('utf-8').split("\n")[0]
    memA=subprocess.check_output(['grep','MemAvailable' ,'/proc/meminfo']).decode('utf-8').split("\n")[0]

    memT=memT.split(" ")[-2]
    memA=memA.split(" ")[-2]
    mem=(int(memT)-int(memA))//1024
    if int(mem)>1024:
        mem=round(int(mem)/1024,2)
        mem=str(mem)+"Gib"
    else:
        mem=str(mem)+"M"
    

    #uptime
    with open('/proc/uptime', 'r') as f:
        upseconds = float(f.readline().split()[0])
    minutes, seconds = divmod(upseconds, 60)
    hours, minutes = divmod(minutes, 60)

    if upseconds<60:
        up="1 min"
    elif hours>0:
        up="{}:{} hrs".format(int(hours),int(minutes))
    else:
        up="{} min".format(min)

    data={
        "temp":temp,
        "freq":cfreq,
        "usage":usage,
        "mem":mem,
        "uptime":up
    }
    return data

def mainsysteminfo2():
    # storage

    allsto=subprocess.check_output(['lsblk','--json']).decode('utf-8')
    allsto=json.loads(allsto)
    allsto=allsto["blockdevices"]
    sto=0
    for block in allsto:
        if block["name"]=="mmcblk0":
            sto=block["size"]

    # all services
    totalser=os.popen("systemctl list-units | wc -l").read()
    totalser=int(totalser)-7  
    
    # all failed services
    totalfailser=os.popen("systemctl list-units --state failed | wc -l").read()
    totalfailser=int(totalfailser)-6 

    return {"storage":sto,"totalservices":totalser,"failedservice":totalfailser}


def getCpuUsage():
    cpudata=psutil.cpu_percent(interval=2,percpu=True)
    cdata={}
    for i,data in enumerate(cpudata):
        cdata["core"+str(i+1)]=data
    return cdata

def systeminfo():
    hostname=os.popen("hostname").read()
    username=os.popen("echo $USER").read()

    data={
        "hostname":hostname,
        "username":username
    }

    return data