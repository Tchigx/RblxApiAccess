from flask import Flask, jsonify, request
import json 
import requests

app = Flask(__name__)

@app.route('/GetAssetBySearch', methods=['GET'])
def handle_endpoint():
    # Access query parameters
    param1 = request.args.get('param1', default=None, type=str)
    param2 = request.args.get('param2', default=None, type=str)
    param3 = request.args.get('param2', default=None, type=str)
    FinalStr=""
    if param1=="Decal":
        print()
    #  FinalStr=f"https://catalog.roblox.com/v1/search/items?category=8&creatorTargetId={param2}&includeNotForSale=true&limit=120"
    elif param1=="Audio":
        print()
        #FinalStr=f"https://catalog.roblox.com/v1/search/items?category=9&creatorTargetId={param2}&includeNotForSale=true&limit=120"

    page=requests.get(FinalStr)


    # You can set default values and types for the parameters
    #page=requests.get("https://catalog.roblox.com/v1/search/items?category=8&creatorTargetId=2837719&includeNotForSale=true&limit=120") 
   


    # Use the query parameters in your response or processing
    return jsonify({'param1': param1, 'param2': param2}), 200

if __name__ == '__main__':
    app.run(debug=True)
