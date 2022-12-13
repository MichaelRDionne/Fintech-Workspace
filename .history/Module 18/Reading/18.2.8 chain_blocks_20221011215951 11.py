import streamlit as st
from dataclasses import dataclass
from typing import List
from datetime import datetime
import hashlib
from typing import Any

# Creating a data class called Block
@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        return sha.hexdigest()

# Create the data class Pychain
@dataclass
class PyChain:
    chain: List[Block]

    def add_block(self, block):
        self.chain += [block]

# Create a new instance of the Block class
new_block = Block(data="new_block", creator_id=42, prev_hash=prev_block_hash)

# Add the new block to the chain
pychain.add_block(new_block)
print(pychain)


@st.cache(allow_output_mutation=True)
def setup():
    return PyChain([Block(data="Genesis", creator_id=0)])

pychain = setup()