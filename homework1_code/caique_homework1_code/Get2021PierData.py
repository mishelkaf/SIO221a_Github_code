def Get2021PierData(date_start,date_end,filename):
	# This function returns temperature, pressure and time from the 2021 pier record (http://sccoos.org/thredds/catalog/autoss/catalog.html)
	# date_start and date_end should be on the datetime format
	# Example:
	# If the start date is January 1st 00:02:17, date_start should be datetime.datetime(2021,1,1,0,2,17)  
	# CDL SIO211A 10/02/2022

	# Important packages
	import netCDF4 as nc              # Read nc files
	import datetime                   # Manage time vectors
	import pandas as pd               # Useful to work with DataFrames and also to manage time

	# Loading time
	dat = nc.Dataset(filename)
	time = dat['time'][:]
	
	# Converting time vector
	timev = [str(datetime.datetime(1970,1,1)+datetime.timedelta(seconds=int(d))) for d in time]
	timev = pd.to_datetime(timev)

	# Loading Temperature and Pressure data for the selected time interval
	idx = np.where((timev>=date_start)&(timev<=date_end))[0]
	temp = dat['temperature'][idx]
	pres = dat['pressure'][idx]
	timev = timev[idx]
	
	return pd.DataFrame({'temp':temp,'pres':pres,'time':timev}) # Pier object

