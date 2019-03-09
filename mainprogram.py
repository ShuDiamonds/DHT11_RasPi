#!/usr/bin/python3
# -*- Coding: utf-8 -*-

import RPi.GPIO as GPIO
import dht11
import time
import datetime
import sys


import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

def write_Googlespreadsheet(tmp):
    #init google spreadsheet
    credentials = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet.json', scope)
    gc = gspread.authorize(credentials)
    workbook1 = gc.open('TemperatureAndHumidity')
    worksheet=workbook1.sheet1
    worksheet.append_row(tmp)
def debugprint(text):
    with open("debug.txt", "a") as f:
            f.write(datetime.now().strftime("%Y_%m_%d %H:%M:%S ")+text+"\n")
    return
def main():
    
    # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    # read data using pin 14
    instance = dht11.DHT11(pin=14)


    
    
    csv_colmnsname=["time","Temperature","Humidity"]
    
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + datetime.datetime.now().strftime("%Y_%m_%d %H:%M:%S"))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            
            #write Google Spreadsheet
            tmp=[datetime.datetime.now().strftime("%Y_%m_%d %H:%M:%S"),result.temperature,result.humidity]
            try:
                write_Googlespreadsheet(tmp)
                
            except ZeroDivisionError as e:
                print(e)
                debugprint(str(e))
            
            
        time.sleep(60*10)


if __name__ == "__main__":
    with open("debug.txt", "a") as f:
        f.write(datetime.datetime.now().strftime("%Y_%m_%d")+":"+str(sys.version)+"\n")
    time.sleep(20)
    main()