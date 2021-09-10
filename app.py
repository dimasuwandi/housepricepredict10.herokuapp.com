from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    prediction = 0
    if request.method == 'POST':
        model = pickle.load(open('model_house_price.sav','rb'))
        bed = request.form.get('bedrooms')
        bath = request.form.get('bathrooms')
        sqft = request.form.get('sqft')


        params = {'bedrooms':[bed], 'bathrooms':[bath], 'sqft_living': [sqft]}
        print(params)

        if bed == '' or bath == '' or sqft == '' or int(sqft) < 50:
            prediction = 0
        else:
            prediction = int(model.predict(pd.DataFrame(params)))

        print(prediction)


    return render_template('index.html', prediction=prediction)




if __name__ == '__main__':
    app.run(debug=True)