from flask import Flask, request, jsonify
from flask_restful import Api
import json
import eth_account
import algosdk

app = Flask(__name__)
api = Api(app)
app.url_map.strict_slashes = False

@app.route('/verify', methods=['GET','POST'])
def verify():
    content = request.get_json(silent=True)
    
    signature=content['sig']
    pk=content['payload']['pk']
    platform=content['payload']['platform']
    message=content['payload']['message']
    
    result = False #Should only be true if signature validates
    
    if (algosdk.util.verify_bytes(message.encode('utf-8'),signature,pk)):
        result=True
    else if (eth_account.Account.recover_message(message,signature=signature.signature.hex()) == pk):
        result=True
    
    #Check if signature is valid
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
