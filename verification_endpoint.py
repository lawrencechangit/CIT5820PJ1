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
    signature = content['sig']
    pk = content['payload']['pk']
    platform = content['payload']['platform']
    message = content['payload']['message']
    result = False
    
    if (platform == 'Ethereum'):
        #eth_encoded_msg = eth_account.messages.encode_defunct(text=message)
        #eth_sig_obj = signature
        #if eth_account.Account.recover_message(eth_encoded_msg, signature=eth_sig_obj) == pk:
            result = True
    
    elif (platform == 'Algorand'):
        #payload = message
        #algo_pk = pk
        #if algosdk.util.verify_bytes(payload.encode('utf-8'), signature, algo_pk):
            result = True
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
