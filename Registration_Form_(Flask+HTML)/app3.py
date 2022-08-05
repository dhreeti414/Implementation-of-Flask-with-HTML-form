from flask import Flask, render_template, request

app3= Flask(__name__)

@app3.route('/',methods=['GET','POST'])
def formfill():
    if request.method == 'POST':
        name= request.form['nme']
        dob=request.form['bday']
        email=request.form['eml']
        city=request.form['cty']
        return "<title>RegForm</title> <h1> Welcome {} <br> Your Date of Birth is: {} <br> Registered Email ID is: {} <br> Your location is: {}</h1>".format(name,dob,email,city)
   
    return render_template('application_form.html')

if __name__=='__main__':
    app3.run(debug=True)