import tkinter as tk
import os 
from tkinter import font
import requests
h = 500
w = 600

os.system('clear')

root = tk.Tk()
canvas = tk.Canvas(root, height =h, width =w)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label =tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

def test(entry):
	print("this is the entry:",entry)

def output_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		final_string = 'City: %s \nConditions: %s \nTemperature (F): %s' % (name,desc,temp)
	except:
		final_string ='there was a error getting value'

	return final_string

def get_wheather(city):
	weather_key = '32b86fc416100b784aa6d48d97dbce23'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	param = {'APPID':weather_key,'q': city, 'units': 'imperial'}
	response = requests.get(url, params= param)
	weather = response.json()
	
	label['text'] = output_response(weather)

frame = tk.Frame(root, bg ='#ffb380',bd =5)
frame.place(relwidth=0.75,relheight=0.1,relx=0.5,rely=0.1,anchor= 'n')

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,text ='get whether',font =40,command = lambda: get_wheather(entry.get()))
button.place(relx=0.75,relheight=1,relwidth=0.25)


#########################

lowerFrame = tk.Frame(root, bg='#ffb380',bd=5)
lowerFrame.place(relwidth=0.75,relheight=0.6,relx=0.5,rely=0.3,anchor='n')

label = tk.Label(lowerFrame,font = ('Corbel Light',20))
label.place(relwidth=1,relheight=1)




root.mainloop()