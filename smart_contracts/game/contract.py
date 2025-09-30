from typing import Literal, TypeAlias
from algopy import ARC4Contract, BoxMap, LocalState, UInt64, arc4

Board: TypeAlias = arc4.StaticArray[arc4.Byte, Literal[9]]
HOST_MARK = 1
GUEST_MARK = 2

class GameState(arc4.Struct, kw_only=True):
    board: Board
    host: arc4.Address
    guest: arc4.Address
    is_over: arc4.Bool
    turns: arc4.UInt8
