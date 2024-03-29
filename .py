import pyttsx3
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import PySimpleGUI as sg
sg.theme('SandyBeach')
excel = pd.read_excel('C:/Users/crt23/Downloads/crop.xlsx', header = 0)
print(excel)
print(excel.shape)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.runAndWait()
le = preprocessing.LabelEncoder()
crop = le.fit_transform(list(excel["CROP"]))
NITROGEN = list(excel["NITROGEN"])
PHOSPHORUS = list(excel["PHOSPHORUS"])
POTASSIUM = list(excel["POTASSIUM"])
TEMPERATURE = list(excel["TEMPERATURE"])
HUMIDITY = list(excel["HUMIDITY"])
PH = list(excel["PH"])
RAINFALL = list(excel["RAINFALL"])
features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))
features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL])
features = features.transpose()
print(features.shape)
print(crop.shape)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(features, crop)
layout =[[sg.Text('                          Crop  Recommendation  System🌿', font=("Cooper black", 40), text_color='salmon4')],
         [sg.Text('                                      🎃🌵🌲🌳🍃🌽🌿☘️🍀🎍🥕🌼🌞🌴🪵🌱🥀🌹🪴🍃🍂🍁🌾🌻🍃🍁', font=("Times", 25), text_color = 'green')],
         [sg.Text('Enter the following details :-', font=("Helvetica", 20),text_color = 'black')],
         [sg.Text('Enter ratio of Nitrogen.... in the soil:                             ', font=("Times", 29)), sg.InputText(font=("Times",20), size = (35,1),background_color='khaki3')],
         [sg.Text('Enter ratio of Phosphorous in the soil:                           ', font=("Times", 29)), sg.InputText(font=("Times", 20),size = (35,1),background_color='khaki3')],
         [sg.Text('Enter ratio of Potassium.... in the soil:                           ', font=("Times", 29)), sg.InputText(font=("Times", 20),size = (35,1),background_color='khaki3')],
         [sg.Text('Enter average Temperature value around the field:        ', font=("Times", 29)), sg.InputText(font=("Times", 20),size = (35,1),background_color='khaki3'), sg.Text('*C', font=("Helvetica", 20))],
         [sg.Text('Enter average percentage of Humidity around the field.:', font=("Times", 29)), sg.InputText(font=("Times", 20),size = (35,1),background_color='khaki3'), sg.Text('%', font=("Helvetica", 20))],
         [sg.Text('Enter PH value of the soil.:                                            ', font=("Times", 29)), sg.InputText(font=("Times", 20),size = (35,1),background_color='khaki3')],
         [sg.Text('Enter average amount of Rainfall around the field:        ', font=("Times", 29) ), sg.InputText(font=("Times", 20),size = (35,1),background_color='khaki3'),sg.Text('mm', font=("Helvetica", 20))],
         [sg.Text(size=(50,1),font=("Cooper black",20) , text_color = 'salmon4', key='-OUTPUT1-' )],
        [sg.Button('SUBMIT', font=("Helvetica", 20)),sg.Button('EXIT', font=("Helvetica", 20))],
    [sg.Push(), sg.Button('Unsplash', key='LINK1'), sg.Push()],
    [sg.Text('Unsplash', justification='center', expand_x=True, font=('Courier New', 20, 'underline'), enable_events=True, key='LINK2')],
]
window = sg.Window('Crop Recommendation Assistant', layout).finalize()
window.Maximize()
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event in ('LINK1', 'LINK2'):
        import webbrowser
        webbrowser.open("https://unsplash.com/wallpapers")
        continue

    print(values[0])
    nitrogen_content =         values[0]                                                                                                        # Taking input from the user about nitrogen content in the soil.
    phosphorus_content =       values[1]                                                                                                        # Taking input from the user about phosphorus content in the soil.
    potassium_content =        values[2]                                                                                                        # Taking input from the user about potassium content in the soil.
    temperature_content =      values[3]                                                                                                        # Taking input from the user about the surrounding temperature.
    humidity_content =         values[4]                                                                                                        # Taking input from the user about the surrounding humidity.
    ph_content =               values[5]                                                                                                        # Taking input from the user about the ph level of the soil.
    rainfall =                 values[6]                                                                                                        # Taking input from the user about the rainfall.
    predict1 = np.array([nitrogen_content,phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content, rainfall])  # Converting all the data that we collected from the user into a array form to make further predictions.
    print(predict1)                                                                                                                             # Printing the data after being converted into a array form.
    predict1 = predict1.reshape(1,-1)                                                                              # Reshaping the input data so that it can be applied in the model for getting accurate results.
    print(predict1)                                                                                                # Printing the input data value after being reshaped.
    predict1 = model.predict(predict1)                                                                             # Applying the user input data into the model.
    print(predict1)                                                                                                # Finally printing out the results.
    crop_name = str()
    if predict1 == 0:                                                                                              # Above we have converted the crop names into numerical form, so that we can apply the machine learning model easily. Now we have to again change the numerical values into names of crop so that we can print it when required.
            crop_name = 'Apple(ఆపిల్)'
    elif predict1 == 1:
            crop_name = 'Banana(అరటి సాగు)'
    elif predict1 == 2:
            crop_name = 'Blackgram(మినుము సాగు)'
    elif predict1 == 3:
            crop_name = 'Chickpea(శనగలు సాగు)'
    elif predict1 == 4:
            crop_name = 'Coconut(కొబ్బరి సాగు)'
    elif predict1 == 5:
            crop_name = 'Coffee(కాఫీ సాగు)'
    elif predict1 == 6:
            crop_name = 'Cotton(పత్తి సాగు)'
    elif predict1 == 7:
            crop_name = 'Grapes(ద్రాక్ష సాగు)'
    elif predict1 == 8:
            crop_name = 'Jute(జనపనార సాగు)'
    elif predict1 == 9:
            crop_name = 'Kidneybeans(రాజ్‌మా)'
    elif predict1 == 10:
            crop_name = 'Lentil(పప్పు)'
    elif predict1 == 11:
            crop_name = 'Maize(మొక్కజొన్న)'
    elif predict1 == 12:
            crop_name = 'Mango(మామిడి)'
    elif predict1 == 13:
            crop_name = 'Mothbeans(బొబ్బర్లు)'
    elif predict1 == 14:
            crop_name = 'Mungbeans(పెసలు)'
    elif predict1 == 15:
            crop_name = 'Muskmelon(కర్బూజ)'
    elif predict1 == 16:
            crop_name = 'Orange(నారింజ)'
    elif predict1 == 17:
            crop_name = 'Papaya(బొప్పాయి)'
    elif predict1 == 18:
            crop_name = 'Pigeonpeas(కందులు)'
    elif predict1 == 19:
            crop_name = 'Pomegranate(దానిమ్మ)'
    elif predict1 == 20:
            crop_name = 'Rice(వరి)'
    elif predict1 == 21:
            crop_name = 'Watermelon(పుచ్చకాయ)'

    if int(humidity_content) >=1 and int(humidity_content)<= 33 :                                                # Here I have divided the humidity values into three categories i.e low humid, medium humid, high humid.
            humidity_level = 'low humid'
    elif int(humidity_content) >=34 and int(humidity_content) <= 66:
            humidity_level = 'medium humid'
    else:
            humidity_level = 'high humid'

    if int(temperature_content) >= 0 and int(temperature_content)<= 6:                                           # Here I have divided the temperature values into three categories i.e cool, warm, hot.
            temperature_level = 'cool'
    elif int(temperature_content) >=7 and int(temperature_content) <= 25:
            temperature_level = 'warm'
    else:
            temperature_level= 'hot'

    if int(rainfall) >=1 and int(rainfall) <= 100:                                                              # Here I have divided the humidity values into three categories i.e less, moderate, heavy rain.
            rainfall_level = 'less'
    elif int(rainfall) >= 101 and int(rainfall) <=200:
            rainfall_level = 'moderate'
    elif int(rainfall) >=201:
            rainfall_level = 'heavy rain'

    if int(nitrogen_content) >= 1 and int(nitrogen_content) <= 50:                                             # Here I have divided the nitrogen values into three categories.
            nitrogen_level = 'less'
    elif int(nitrogen_content) >=51 and int(nitrogen_content) <=100:
            nitrogen_level = 'not to less but also not to high'
    elif int(nitrogen_content) >=101:
            nitrogen_level = 'high'

    if int(phosphorus_content) >= 1 and int(phosphorus_content) <= 50:                                         # Here I have divided the phosphorus values into three categories.
            phosphorus_level = 'less'
    elif int(phosphorus_content) >= 51 and int(phosphorus_content) <=100:
            phosphorus_level = 'not to less but also not to high'
    elif int(phosphorus_content) >=101:
            phosphorus_level = 'high'

    if int(potassium_content) >= 1 and int(potassium_content) <=50:                                           # Here I have divided the potassium values into three categories.
            potassium_level = 'less'
    elif int(potassium_content) >= 51 and int(potassium_content) <= 100:
            potassium_level = 'not to less but also not to high'
    elif int(potassium_content) >=101:
            potassium_level = 'high'

    if float(ph_content) >=0 and float(ph_content) <=5:                                                        # Here I have divided the ph values into three categories.
            phlevel = 'acidic'
    elif float(ph_content) >= 6 and float(ph_content) <= 8:
            phlevel = 'neutral'
    elif float(ph_content) >= 9 and float(ph_content) <= 14:
            phlevel = 'alkaline'

    print(crop_name)
    print(humidity_level)
    print(temperature_level)
    print(rainfall_level)
    print(nitrogen_level)
    print(phosphorus_level)
    print(potassium_level)
    print(phlevel)

    speak("Sir according to the data that you provided to me. The ratio of nitrogen in the soil is  " + nitrogen_level + ". The ratio of phosphorus in the soil is  " + phosphorus_level + ". The ratio of potassium in the soil is  " + potassium_level + ". The temperature level around the field is  " + temperature_level + ". The humidity level around the field is  " + humidity_level + ". The ph type of the soil is  " + phlevel + ". The amount of rainfall is  " + rainfall_level )  # Making our program to speak about the data that it has received about the crop in front of the user.
    window['-OUTPUT1-'].update('The best crop that you can grow : ' + crop_name )                                     # Suggesting the best crop after prediction.
    speak("The best crop that you can grow is  " + crop_name)


window.close()
