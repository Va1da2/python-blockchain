"Contains BlickChain class."
from typing import Optional, Dict, Any
from time import time
import json
import hashlib 


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis Block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self,
                  previous_hash: Optional[int]=None,
                  proof:int) -> Dict[str, Any]:
        """
        Create a new Block in the Blockchain.

        :param previous_hash: Hash of previous Block
        :param proof: The proof given by the Proof of Work algorithm
        :return: New Block
        """

        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }
        # Reset the current list of transaction
        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self,
                        sender: str,
                        recipient: str,
                        amount: int) -> int:
        """
        Creates a new transaction to go into the next mined Block

        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the block that will hold this transaction
        """

        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            })

        return self.last_block["index"] + 1

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """
        Creates a SHA-256 hash of a Block.

        :param block: Block
        :return: hash
        """

        # We must make sure that the Dictionary is ordered, or we'll have inconsistent hashes.
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()
        

    @property
    def last_block(self):
        "Returns the last block in the chain."
        return self.chain[-1]


# Example of a Block
# block = {
#     "index": 1,
#     "timestamp": 1506057125.900785,
#     "transactions": [
#         {
#             "sender": "8527147fe1f5426f9dd545de4b27ee00",
#             "recipient": "a77f5cdfa2934df3954a5c7c7da5df1f",
#             "amount": 5,
#         }   
#     ],
#     "proof": 324984774000,
#     "previous_hash": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
# }