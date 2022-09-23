import speedtest
import datetime

s = speedtest.Speedtest()
while True:
    time = datetime.datetime.now().strftime("%H:%M:%S")
    downspeed = round((round(s.download()) / 1048576), 2)
    upspeed = round((round(s.upload()) / 1048576), 2)
    print(f"time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")

# from distutils.command.upload import upload
# from turtle import down
# import speedtest

# s = speedtest.Speedtest()
# down = test.download()
# upload = test.upload()

# print(f"Download speed: {down}")
# print(f"Upload speed: {upload}")

