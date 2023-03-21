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
    /*
    {'sig': '0x3718eb506f445ecd1d6921532c30af84e89f2faefb17fc8117b75c4570134b4967a0ae85772a8d7e73217a32306016845625927835818d395f0f65d25716356c1c', 
 'payload': 
   {'message': 'Ethereum test message', 
    'pk': '0x9d012d5a7168851Dc995cAC0dd810f201E1Ca8AF', 
    'platform': 'Ethereum'}}
   */

    signature=content['sig']
    pk=content['payload']['pk']
    platform=content['payload']['platform']
    message=content['payload']['message']

    result=False

    #Check if signature is valid

    if(platform=='Ethereum'){
      eth_encoded_msg = eth_account.messages.encode_defunct(text=message)
      eth_sig_obj = signature


      if eth_account.Account.recover_message(eth_encoded_msg,signature=eth_sig_obj.signature.hex()) == pk:
        result=True 
    }

    #else if(platform=="Algorand"){
      #if (algosdk.util.verify_bytes(message.encode('utf-8'),signature,pk)):
          #result=True
    #}

    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')
