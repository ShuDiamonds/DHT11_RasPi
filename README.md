# DHT11_RasPi
温度・湿度センサの値を取得し, Google Spreadsheet に保存.  Obtaining temperature &amp; humidity sensor values, program sent them Google Spreadsheet
<div style="; position: relative;top:0; left: 100px;"></div>
<img src="https://github.com/ShuDiamonds/Security-camera/blob/master/image/python_illustration.svg" height="150" width="300">

## Main Features
* Strong Reduction of its SD memory occupation with `difference extraction` Technology.
* Reporting a daily bulletin through on Gmail.
* Supervise the [main program](https://github.com/ShuDiamonds/Security-camera/blob/master/demo/demo2.py) by [reporting.py](https://github.com/ShuDiamonds/Security-camera/blob/master/demo/reporting.py).
* Delete one week ago camera data automatically.

## System Overview
<p align="center"> 
<img  src="https://github.com/ShuDiamonds/Security-camera/blob/master/image/Securitycamera_SystemOverview.svg.png"  title="system overview">
</p>
  
## Requirement  
* DHT11:Humidity & Temperature sensor
* Raspberry pi 3  
* ubuntu16.04 or Rasbian
* Python 3.x  
* Web Camera x2
 <p align="center"> 
<img  src="https://github.com/ShuDiamonds/Security-camera/blob/master/image/IMG_20180927_215417.jpg"  title="setting" width="480">
</p>

 
## Setting
###  install python library
```
sudo pip3 install oauth2client
sudo pip3 install gspread

```

### reporting.py property
Set the email infomation to send a daily report through on gmail.
```
from_email = "senderhogehoge@gmail.com" # 送信元のアドレス
to_email = "receiverhogehoge@gmail.com" # 送りたい先のアドレス
username = "sender@gmail.com"           # Gmailのアドレス
password = "mygmailpassword"            # Gmailのパスワード
```
and you have to lower its Google Security level (if not doing that, you can't send email from gmail and recieve the security alart mail from google).

### rename piSETTING.py_template to piSETTING.py
Set the email infomation to send a daily report through on gmail.
```
from_email = "senderhogehoge@gmail.com" # 送信元のアドレス
to_email = "receiverhogehoge@gmail.com" # 送りたい先のアドレス
username = "sender@gmail.com"           # Gmailのアドレス
password = "mygmailpassword"            # Gmailのパスワード
```
and you have to lower its Google Security level (if not doing that, you can't send email from gmail and recieve the security alart mail from google).


## Usage
### Basic Example
```bash
$ python3 demo2.py
```
### report program example
This program provides three function,Reporting on gmail,deleting one week ago camera data, program activity check (every one hour).

```bash
$ python3 reporting.py
```


## Licence

  [MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Related Articles
* [embedded](https://github.com/topics/shu-embedded-systems)
* [Machine Learning data](https://github.com/topics/shu-machine-learning-data)

## Author
  [ShuDiamonds](https://github.com/ShuDiamonds)
