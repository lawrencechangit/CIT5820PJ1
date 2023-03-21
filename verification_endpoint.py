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

    signature = int(content['sig'],16)
    pk = content['payload']['pk']
    platform = content['payload']['platform']
    message = content['payload']['message']
    print(signature, pk, platform, message)
    result = False

    # Check if signature is valid

    if (platform == 'Ethereum'):
        eth_encoded_msg = eth_account.messages.encode_defunct(text=message)
        eth_sig_obj = signature
        print(eth_sig_obj)
        if eth_account.Account.recover_message(eth_encoded_msg, signature=eth_sig_obj) == pk:
            result = True

    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
