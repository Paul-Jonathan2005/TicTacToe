# Create the basic file structure for your smart contract
# smart_contracts/tic_tac_toe/contract.py

from typing import Literal, TypeAlias
from algopy import (
    ARC4Contract,
    arc4,
    BoxMap,
    LocalState,
    UInt64,
    Txn,
    subroutine,
    OnCompleteAction,
)

Board: TypeAlias = arc4.StaticArray[arc4.Byte, Literal[9]]

# Add game constants
HOST_MARK = 1
GUEST_MARK = 2


class GameState(arc4.Struct, kw_only=True):
    board: Board
    host: arc4.Address
    guest: arc4.Address
    is_over: arc4.Bool
    turns: arc4.UInt8


class TicTacToe(ARC4Contract):
    def __init__(self) -> None:
        self.id_counter = UInt64(0)

        self.games_played = LocalState(UInt64)
        self.games_won = LocalState(UInt64)

        self.games = BoxMap(UInt64, GameState)

    @subroutine
    def opt_in(self) -> None:
        self.games_played[Txn.sender] = UInt64(0)
        self.games_won[Txn.sender] = UInt64(0)

    @subroutine
    def coord_to_matrix_index(self, x: UInt64, y: UInt64) -> UInt64:
        return 3 * y + x

    @arc4.baremethod(allow_actions=[OnCompleteAction.CloseOut])
    def close_out(self) -> None:
        pass
