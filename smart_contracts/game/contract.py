# Create the basic file structure for your smart contract
# smart_contracts/tic_tac_toe/contract.py

from typing import Literal, TypeAlias
from algopy import (
    ARC4Contract,
    arc4,)
Board: TypeAlias = arc4.StaticArray[arc4.Byte, Literal[9]]

# Add game constants
HOST_MARK = 1
GUEST_MARK = 2
