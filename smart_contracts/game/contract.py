from typing import Literal, TypeAlias
from algopy import ARC4Contract, BoxMap, LocalState, UInt64, arc4

Board: TypeAlias = arc4.StaticArray[arc4.Byte, Literal[9]]
HOST_MARK = 1
GUEST_MARK = 2
