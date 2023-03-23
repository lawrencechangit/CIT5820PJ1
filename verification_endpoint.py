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
    content=request.get_json(silent=True)
    
    #json_string=json.dumps(content)
    #contentPyth=json.loads(json_string)
    
    #signature=contentPyth['sig']
    #payload = json.dumps(contentPyth['payload'])
    #pk=contentPyth['payload']['pk']
    #platform=contentPyth['payload']['platform']
    
    signature=content['sig']
    pk=content['pk]
    platform=content['payload']['platform']
    payload = json.dumps(content['payload'])
    
    result = False

    if platform == 'Ethereum':
        eth_encoded_msg = eth_account.messages.encode_defunct(text=payload)
        eth_sig_obj = signature
        if eth_account.Account.recover_message(eth_encoded_msg, signature = eth_sig_obj) == pk:
            result = True

    elif platform == 'Algorand':
        if algosdk.util.verify_bytes(payload.encode('utf-8'), signature, pk):
            result = True

    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')

