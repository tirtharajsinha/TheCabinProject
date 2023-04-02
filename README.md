# <img src="static/favicon.png" align="left" width="35px">TheCabinProject

### <img src="static/raspberrry_pi_logo.png" align="left" width="25px"> RaspberryPi Server dashboard

#### Normal sixe apps with dark mode

<img src="Screenshots\dark_mode_normal.png">

#### compact sixe apps with light mode

<img src="Screenshots\light_mode_compact.png">

#### Control Center

<img src="Screenshots\Control_center.png">

#### Application manager to pin/unpin app and edit

<img src="Screenshots\app_manager.png">

#### Flagship Appearance manager

<img src="Screenshots\appearance_page.png">

#### Server hardware and software monitor dashboard

<img src="Screenshots\monitor.png">

### Requirements

1. Raspberry Pi
2. Os installed
3. python
4. python3-pip

## installation

```
pip3 install -r requirements.txt
```

## Run

```
python3 manage.py runserver 0.0.0.0:8000
```

In case you want to run the app from port 80, run the below comand.
As port 80 requires sudo permission. This method is insecure. Use this if you know what you are doing.

```
sudo -E python3 manage.py runserver 0.0.0.0:80
```
