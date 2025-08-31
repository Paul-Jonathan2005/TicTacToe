from typing import Literal, Tuple, TypeAlias
from algopy import (
    ARC4Contract, BoxMap, Global, LocalState, OnCompleteAction, Txn, UInt64, arc4,
    gtxn, itxn, op, subroutine, urange
)

Board: TypeAlias = arc4.StaticArray[arc4.Byte, Literal[9]]
HOST_MARK = 1
GUEST_MARK = 2
