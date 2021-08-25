import COVID19Py
from pynotifier import Notification
covid19=COVID19Py.COVID19(data_source="jhu")
latest=covid19.getLatest()
string = "Confirmed :"+str(+latest["confirmed"])+"\nRecovered :"+str(latest["recovered"])+"\nDeaths :"+str(latest["deaths"])
Notification(title="Today COVID19 News updates.",description=string,duration=10,).send()





