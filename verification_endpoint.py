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

    if (platform == 'Algorand'):
        print(" ")
        payload = message

        algo_pk = pk

        print("Encoded message is ", payload.encode('utf-8'))
        print("Public key is", algo_pk)
        print("Signature is", signature)

        if algosdk.util.verify_bytes(payload.encode('utf-8'), signature, algo_pk):
            print("It verifies!")
            result = True

        else:
            print("Not verified!")
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
