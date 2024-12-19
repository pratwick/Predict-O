from django.http.response import HttpResponse
from django.shortcuts import render
from fpdf import FPDF
from django.http import FileResponse
import numpy as np
import pickle
from sklearn.model_selection import RandomizedSearchCV
import sklearn
from sklearn.preprocessing import StandardScaler
import joblib



# Create your views here.



def index(request):
    return render(request,'home.html')


def math(request):
    return render(request,'service.html')


def result(request):
    if request.method == 'POST':
        
        km = int(request.POST['kms'])
        fuel = int(request.POST['fuel_type'])
        if(fuel==0):
            o_fuel = "COMPRESSED NATURAL GAS"
        elif(fuel==1):
            o_fuel = "DIESEL"
        elif(fuel==2):
            o_fuel = "ELECTRIC VEHICLE"
        elif(fuel==3):
            o_fuel = "LIQUID PETROLEUM GAS"
        else:
            o_fuel = "PETROL"
        trans = int(request.POST['trans'])
        if(trans==0):
            o_trans = "MANUAL"
        else:
            o_trans = "AUTOMATIC"
        deal = int(request.POST['dealer'])
        if(deal==0):
            o_deal = "DEALER"
        elif(deal==1):
            o_deal = "INDIVIDUAL"
        else:
            o_deal = "TRUSTMARK DEALER"
        mile = float(request.POST['mileage'])
        engine = int(request.POST['engine'])
        price = int(request.POST['price'])
        power = float(request.POST['max'])
        seat = int(request.POST['seat'])
        comp = int(request.POST['company'])
        if(comp==1):
            o_comp = "AUDI"
        elif(comp==2):
            o_comp = "BMW"
        elif(comp==3):
            o_comp = "BENTLEY"
        elif(comp==4):
            o_comp = "DATSUN"
        elif(comp==5):
            o_comp = "FERRARI"
        elif(comp==6):
            o_comp = "FORCE"
        elif(comp==7):
            o_comp = "FORD"
        elif(comp==8):
            o_comp = "HONDA"
        elif(comp==9):
            o_comp = "HYUNDAI"
        elif(comp==10):
            o_comp = "ISUZU"
        elif(comp==11):
            o_comp = "isuzu"
        elif(comp==12):
            o_comp = "JAGUAR"
        elif(comp==13):
            o_comp = "JEEP"
        elif(comp==14):
            o_comp = "KIA"
        elif(comp==15):
            o_comp = "LAND ROVER"
        elif(comp==16):
            o_comp = "LEXUS"
        elif(comp==17):
            o_comp = "MG"
        elif(comp==18):
            o_comp = "MAHINDRA"
        elif(comp==19):
            o_comp = "MARUTI"
        elif(comp==20):
            o_comp = "MASERATI"
        elif(comp==21):
            o_comp = "MERCEDES-AMG"
        elif(comp==22):
            o_comp = "MERCEDES-BENZ"
        elif(comp==23):
            o_comp = "MINI"
        elif(comp==24):
            o_comp = "NISSAN"
        elif(comp==25):
            o_comp = "PORSCHE"
        elif(comp==26):
            o_comp = "RENAULT"
        elif(comp==27):
            o_comp = "ROLLS-ROYCE"
        elif(comp==28):
            o_comp = "SKODA"
        elif(comp==29):
            o_comp = "TATA"
        elif(comp==30):
            o_comp = "TOYATA"
        elif(comp==31):
            o_comp = "VOLKSWAGEN"
        elif(comp==32):
            o_comp = "VOLVO"
        
        
        age = int(request.POST['age'])
       
        global context
        context = {
    
            'km':str(km),
            'fuel':o_fuel,
            'deal':deal,
            'trans':o_trans,
            'mile':str(mile),
            'engine':str(engine),
            'power':str(power),
            'seat':str(seat),
            'comp':o_comp,
            'age':str(2021-age), 
            'p':str(price),
        }
        
        model = joblib.load('Final_effort.pkl')
        prediction=model.predict([[comp,age,km,deal,fuel,trans,mile,engine,power,seat,price]])
        output=round(prediction[0],2)

        context['result'] = str(output)

        return render(request,'result.html',context)
    

def report(request):
    class PDF(FPDF):
        def header(self):
                
            self.image('static\predicto.jpg',10,8,25)

            self.set_font('helvetica','B',20)

            self.cell(0,10,'Details of Car',border=False,ln=1,align='C')

            self.ln(20)

    pdf = PDF('P','mm','Letter')

    pdf.add_page()

    pdf.set_font('times','B',16)   

    pdf.cell(80,10,'Brand')
    pdf.cell(80,10, context['comp'],ln=1)

    pdf.cell(80,10,'Year of Buying')
    pdf.cell(80,10, context['age'],ln=1)

    pdf.cell(80,10,'Fuel')
    pdf.cell(80,10, context['fuel'],ln=1)

    pdf.cell(80,10,'Transmission')
    pdf.cell(80,10, context['trans'],ln=1)

    pdf.cell(80,10,'Car Kilometers')
    pdf.cell(80,10, context['km'] + 'km',ln=1)

    pdf.cell(80,10,'Engine')
    pdf.cell(80,10, context['engine'] + 'cc',ln=1)

    pdf.cell(80,10,'Power')
    pdf.cell(80,10, context['power'] + 'bhp',ln=1)

    pdf.cell(80,10,'Car Seat')
    pdf.cell(80,10, context['seat'],ln=1)

    pdf.cell(80,10,'On-Road Price')
    pdf.cell(80,10, 'Rs ' + context['p'],ln=1)

    pdf.cell(80,10,'Final Result')
    pdf.cell(80,10,'Rs ' +  context['result'],ln=1)

    pdf.output('Download.pdf')


    return FileResponse(open('Download.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
  


def about(request):
    return render(request,'about.html')