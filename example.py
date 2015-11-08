import datetime
import forecastio
import pytz
import operator
import tkinter


Tk = tkinter.Tk()
message = 'What The Weather'

#Sets window Options
Tk.wm_title("TITLE WEATER")
Tk.resizable(width='FALSE', height='FALSE')
Tk.wm_geometry("%dx%d%+d%+d" % (720, 480, 0, 0))
myfile = open("output.txt","w")

#Method run by item button
def press():
    Instruction.config(text='Button Pressed')

def eiei():
    print("eiei")

def test():
    """
    Run load_forecast() with the given lat, lng, and time arguments.
    """
    #Our API key
    api_key = "5c5a1a440d3b0e89239368a9a8fb251b"
    #latitude - The latitude of the location for the forecast
    lat = 13.7522222
    #longitude - The longitude of the location for the forecast
    lng = 100.4938889
    #datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
    year = 2015
    month = 11
    day = 8
    hour = 1
    minute = 22
    second = 33
    current_time = datetime.datetime.now()
    time = current_time
    #specific date
    #time = datetime.datetime(year, month, day, hour, minute, second, 44, pytz.UTC)
    forecast = forecastio.load_forecast(api_key, lat, lng, time=time)
    day = time.day
    the_dict = dict()
    the_list = list()
    for i in range(7):
        forecast2 = forecastio.load_forecast(api_key, lat, lng, time=time)
        by_hour2 = forecast2.hourly()
        print("DAY:",day,time.strftime("%B"), file=myfile)
        for hourly_data_point in by_hour2.data:
            the_weather = ""+str(hourly_data_point)[30:].split(' at')[0].strip()
            the_list.append(the_weather)
        d = dict()
        for c in the_list:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        sorted_d = sorted(d.items(), key=operator.itemgetter(0))
        sorted_d.reverse()
        print (sorted_d, file=myfile)
        #myfile.write(sorted_d)
        forecast2 = forecastio.load_forecast(api_key, lat, lng, time=datetime.datetime(2015, 11, day, 1, 22, 33, 44, pytz.UTC))
        print(forecast2.hourly().summary, file=myfile)
        #myfile.write(forecast2.hourly().summary)
        time += datetime.timedelta(days=1)
        day = time.day
        the_list = list()
    myfile.close()
    #Reset day for next method
    day = time.day
    print("===========Currently Data=========")
    print(forecast.currently())
    #print("===========Hourly Data=========")
    by_hour = forecast.hourly()
    #print("Hourly Summary: %s" % (by_hour.summary))
    #print("bhs",by_hour.summary)
    for hourly_data_point in by_hour.data:
        break
        #print(hourly_data_point)
        #print(str(hourly_data_point)[30:].split(' at')[0])
    #print("===========Daily Data=========")
    by_day = forecast.daily()
    #API no longer support this point
    #print("Daily Summary: %s" % (by_day.summary))
    for daily_data_point in by_day.data:
        break
        print(daily_data_point)


#if __name__ == "__main__":
    #main()
#label
Instruction = tkinter.Label(Tk, text=message, font='size, 20')
Instruction.pack()

#item button
item = tkinter.Button(Tk, command=test,height = 10, width = 20,text="Check Out!").pack()


#Background
#Tk.configure(background=Theme.GUI_bg)
Tk.mainloop()
