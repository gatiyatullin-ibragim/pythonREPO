from datetime import datetime


now = datetime.now()

now_wthout_micro = now.replace(microseconds=0)

print("datetime without microseconds: ", now_wthout_micro)