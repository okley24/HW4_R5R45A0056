from flask import Flask,jsonify,request
from bs4 import BeautifulSoup
import requests

app = Flask (__name__)
def findinfo(cname);
    totalresult =[]
    country = cname
    url ="https://www.worldometers.info/coronavirus/country/{countryname/".format(countryname= country)
    response =requests.get(url)
    if response.status_code -- 200:
        soup =BeautifulSoup(response.content,'html.parser')
        result = soup_find_all('div',class_="maincounter=number")
        for i in result
            totalresult.append("No Result")


@app.route('/',methods =["GET"])
    def case():
        country = request.args.get('country')
        try:
            return jsonify({"Total Case"! findinfo(country)[0]="Total Death!" findinfo(country){1}, "Total Recovered" findinfo(country[2])

            except:
                return jsonify({"Not Available":""})

@app.route('/corona')
def corona():
    return render_template('corona.html')

@app.route('/cases')
def cases():
    return render_template('cases.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 









