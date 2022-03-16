import pandas as pd
import datetime
import json
from flask import *
app=Flask(__name__)
@app.route('/',methods=['Get'])
def Date():
    x = datetime.datetime.now()
    day=x.strftime("%d")
    month=x.strftime("%m")
    date=month+'-'+day
    date_dict = {'Date': date} 
    date_dict_ = json.dumps(date_dict)
    return date_dict_
    
if(__name__=='__main__'):
    app.run(port=7777)




