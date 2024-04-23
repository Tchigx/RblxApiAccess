from flask import Flask, jsonify, request
import json 
import requests
import time 

app = Flask(__name__)

@app.route('/GetAssetBySearch', methods=['GET'])
def handle_endpoint():
    # Access query parameters
    param1 = request.args.get('Category', default=None, type=str)
    param2 = request.args.get('CreatorID', default=None, type=str)
   # param3 = request.args.get('param2', default=None, type=str)
    AllData=[]
    page_number=1
    while True:
        FinalStr=f"https://search.roblox.com/catalog/json?CreatorID={param2}&SortType=3&PageNumber={page_number}&Category={param1}"
        page=requests.get(FinalStr)
        StatusCode=page.status_code

        if StatusCode== 429:
            break
    
        page=page.json()
        if not page:

            break
        
        AllData.extend(page)
        time.sleep(0.5)
        page_number+=1
    # Use the query parameters in your response or processing
    print(StatusCode)
    return jsonify(AllData), StatusCode
    

@app.errorhandler(404)
def page_not_found(e):
    # your error handling logic here
    return 'Page Not Found xd xd xd', 404  

if __name__ == '__main__':
    app.run(debug=True)
