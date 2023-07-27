from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def temperature():
    return render_template("index.html")

@app.route('/temper',methods=['POST','GET'])
def temp_check():
    first=int(request.form['temp1'])
    second =int(request.form['temp2'])
    temp = float(request.form['temperature'])
    if first==1 and second==1 :
        result = temp
        unit=1
    elif first==2 and second==2 :
        result = temp
        unit=2
    elif first==3 and second==3 :
        result = temp
        unit=3
    elif first==1 and second==2:
        result = temp*9/5+32
        unit=2
    elif first==1 and second==3:
        result = temp+273
        unit=3
    elif first==2 and second==1:
        result = (temp-32)*5/9
        unit=1
    elif first==2 and second==3:
        result = (temp-32)*5/9+273
        unit=3
    elif first==3 and second==1:
        result = temp-273
        unit=1
    elif first==3 and second==2:
        result = (temp-273)*9/5+32
        unit=2
    print(temp)
    return render_template("index.html",result=result,unit=unit)
    
if __name__=='__main__':
    app.run(debug=True)