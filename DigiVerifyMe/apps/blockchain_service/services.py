# blockchain_service/services.py
from web3 import Web3
from django.conf import settings

# Initialize Web3 connection
w3 = Web3(Web3.HTTPProvider(settings.BLOCKCHAIN_NODE_URL))

def submit_blockchain_transaction(user, contract_address, function_name):
    # Load the contract ABI
    contract_abi = settings.CONTRACT_ABI
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    # Build the transaction with the appropriate function call
    tx = contract.functions[function_name]().buildTransaction({
        'nonce': w3.eth.get_transaction_count(user.public_key),
        'gas': 2000000,
        'gasPrice': w3.eth.gas_price,
        'value': 0,
    })
    
    # Sign and send the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, user.private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()

def get_transaction_status(transaction_hash):
    try:
        tx_receipt = w3.eth.get_transaction_receipt(transaction_hash)
        if tx_receipt is None:
            return 'PENDING'
        elif tx_receipt['status'] == 1:
            return 'CONFIRMED'
        else:
            return 'FAILED'
    except Exception as e:
        print(f"Error checking transaction status: {e}")
        return 'UNKNOWN'
