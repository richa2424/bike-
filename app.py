#django
#flask
#streamlit
#fast api
#rest api
#front end --> html/css
#backend --> python flask is a web framework 


from flask import Flask , render_template, url_for, request
import joblib # type: ignore

import pandas as pd 

# import mysql.connector # type: ignore

# Connect to the database
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="bike_predicted_data"

# )
# if conn.is_connected():
#     print("hm connect ho chuke ")
# else:
#     print("not conn")    

# mysql_cursor = conn.cursor()
# query = "INSERT INTO bike_predictions (owner_name, brand_name, kms_driven_bike, age_bike, power_bike, prediction) VALUES (%s, %s, %s, %s, %s, %s)"

model = joblib.load('model.lb')
app = Flask(__name__)


@app.route('/')                    # (/) --> home route 
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contactus():
    return render_template('contact.html')

@app.route('/history')
def history():
    # Create a cursor object
    # mysql_cursor = conn.cursor()                 #dictionary=True

    # try:
    #     # Execute the SELECT query to fetch historical data
    #     query = "SELECT * FROM bike_predictions"
    #     mysql_cursor.execute(query)

    #     # Fetch all the results
    #     historical_data = mysql_cursor.fetchall()

    # except mysql.connector.Error as error:
    #     print("Error:", error)
    #     historical_data = []

    # finally:
    #     pass
    #     # # Close the cursor
    #     mysql_cursor.close()
    #     conn.close()

    # Pass the historical data to the history.html template for rendering
    return render_template("history.html", historical_data="historical_data")



@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        brand_name = request.form['brand_name']
        owner_name=int(request.form['owner'])
        age_bike=int(request.form['age'])
        power_bike= int(request.form['power'])
        kms_driven_bike= int(request.form['kms_driven'])
        bike_numbers={'TVS': 0,
                        'Royal Enfield': 1,
                        'Triumph': 2,
                        'Yamaha': 3,
                        'Honda': 4,
                        'Hero': 5,
                        'Bajaj': 6,
                        'Suzuki': 7,
                        'Benelli': 8,
                        'KTM': 9,
                        'Mahindra': 10,
                        'Kawasaki': 11,
                        'Ducati': 12,
                        'Hyosung': 13,
                        'Harley': 14,
                        'Jawa': 15,
                        'BMW': 16,
                        'Indian': 17,
                        'Rajdoot': 18,
                        'LML': 19,
                        'Yezdi': 20,
                        'MV': 21,
                        'Ideal': 22}
        
        brand_name_encode=bike_numbers[brand_name]

        print(owner_name,brand_name_encode,kms_driven_bike,age_bike,power_bike)
        lst=[[owner_name,brand_name_encode,kms_driven_bike,age_bike,power_bike]]  #sequence order
        pred = model.predict(lst)
        pred = pred[0]
        pred = round(pred, 2)
        # user_data = (str(owner_name),str(brand_name),kms_driven_bike,age_bike,power_bike,pred)


    #     try:
    # # Execute the query with user data
    #         mysql_cursor.execute(query, user_data)
    #         print("row is instered :", mysql_cursor.rowcount)
    
    # # Commit the transaction
    #         conn.commit()

    #     except mysql.connector.Error as error:
    #         print("Error:", error)

    #     finally:
    # # Close the cursor and connection
    #         mysql_cursor.close()
    #         conn.close()
        return render_template("project.html",prediction=str(pred))
    



    
   


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)




#  mysql_cursor = conn.cursor(dictionary=True)

#     try:
#         # Execute the SELECT query to fetch historical data
#         query = "SELECT * FROM bike_predictions"
#         mysql_cursor.execute(query)

#         # Fetch all the results
#         historical_data = mysql_cursor.fetchall()

#     except mysql.connector.Error as error:
#         print("Error:", error)
#         historical_data = []

#     finally:
#         # Close the cursor
#         mysql_cursor.close()

#     # Pass the historical data to the history.html template for rendering
#     return render_template("history.html", historical_data=historical_data)
# form tag laga le user se brand name ka input leke phir history uss brand name ke according show karna hai aur ussko aur presentable banana hai