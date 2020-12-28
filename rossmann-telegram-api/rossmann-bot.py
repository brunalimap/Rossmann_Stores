import os
import json
import requests
import pandas as pd

from flask import Flask,request,Response

#constants
TOKEN = '1487443252:AAFW1SZ_LhsrUgD0WwX5Kea7lEB5k6MgPk0'

#Info about  the Bot
#https://api.telegram.org/bot1487443252:AAFW1SZ_LhsrUgD0WwX5Kea7lEB5k6MgPk0/getMe
        
#get updates
#https://api.telegram.org/bot1487443252:AAFW1SZ_LhsrUgD0WwX5Kea7lEB5k6MgPk0/getUpdates

#send message
#https://api.telegram.org/bot1487443252:AAFW1SZ_LhsrUgD0WwX5Kea7lEB5k6MgPk0/sendMessage?chat_id=877434838&text=Hi Bruna, I am doing good, thanks!

def send_message(chat_id,text):
    url ='https://api.telegram.org/bot{}/'.format(TOKEN)
    url = url + 'sendMessage?chat_id={}'.format(chat_id)
    
    r = requests.post(url,json={'text':text})
    print('Status Code {}'.format(r.status_code))
    return None

def load_dataset(store_id):
    #loading test dataset
    df10 = pd.read_csv('test.csv')
    df_store_raw = pd.read_csv('store.csv')

    #merge test dataset + store
    df_test = pd.merge(df10,df_store_raw, how='left', on='Store')

    #choose store for prediction
    df_test = df_test[df_test['Store'] == store_id]
    
    if not df_test.empty:
        #remove closed days
        df_test = df_test[df_test['Open'] != 0]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop('Id',axis=1)

        #convert Dataframe to json
        data = json.dumps(df_test.to_dict(orient='records'))
        
    else:
        data = 'error'
        
    return data
#https://sales-rossmann-prediction.herokuapp.com/rossmann/predict
def predict(data):
    #API Call
https://git.heroku.com/sales-rossmann-telegram-bot.git
    url = 'https://git.heroku.com/sales-rossmann-telegram-bot.git'
    header = {'Content-type': 'application/json'}
    data = data

    r = requests.post(url,data=data, headers=header)
    print('Status Code {}'.format(r.status_code))

    d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys())
    return d1

def parse_message(message):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']
    
    store_id = store_id.replace('/','')
    
    try:
        store_id = int(store_id)
        
    except ValueError:
        store_id = 'error'
    
    return chat_id, store_id

#API initialize
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def index():
       
    
    if request.method =='POST':
        message = request.get_json()
        
        
        # parses message comming from json
        chat_id, store_id = parse_message(message)
        
        if store_id != 'error':
            
            #loading data
            data = load_dataset(store_id)
            
            if data !='error':
            
                #prediction
                d1 = predict(data)

                #calculates
                d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

                #send message
                msg = 'The estimated total amount sales in the store number {}  is of US${:,.2f} for next 6 week.'.format( 
                d2['store'].values[0], 
                d2['prediction'].values[0])

                send_message(chat_id,msg)
                return Response('ok',status=200)

            else:    
                send_message(chat_id,'Store not Available, please type again Store ID.')
                return Response('ok',status=200)
        
        elif(store_id == 'start'):
             send_message(chat_id,'Hi! What store number do you want to forecast sales for the next 6 weeks?'
                return Response('ok',status=200)
        
            
                             
        else:    
            send_message(chat_id,'This is not number store. Please  try again /n Example: /12')
            return Response('ok',status=200)
    
    else:
        return '<h1> Sales Rossmann Telegram Bot </h1> '

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
