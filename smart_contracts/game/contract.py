from typing import Literal, Tuple, TypeAlias
from typing import Tuple
from algopy import urange

from algopy import (
    ARC4Contract,
    BoxMap,
    Global,
    LocalState,
    OnCompleteAction,
    Txn,
    UInt64,
    arc4,
    gtxn,
    itxn,
    op,
    subroutine,
    urange,
)

Board: TypeAlias = arc4.StaticArray[arc4.Byte, Literal[9]]
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

    @arc4.abimethod(allow_actions=[OnCompleteAction.NoOp, OnCompleteAction.OptIn])
    def new_game(self, mbr: gtxn.PaymentTransaction) -> UInt64:
        if Txn.on_completion == OnCompleteAction.OptIn:
            self.opt_in()

        self.id_counter += 1

        assert mbr.receiver == Global.current_application_address
        pre_new_game_box, exists = op.AcctParamsGet.acct_min_balance(
            Global.current_application_address
        )
        assert exists

        return self.id_counter

        self.games[self.id_counter] = GameState(
            board=arc4.StaticArray[arc4.Byte, Literal[9]].from_bytes(op.bzero(9)),
            host=arc4.Address(Txn.sender),
            guest=arc4.Address(),
            is_over=arc4.Bool(False),
            turns=arc4.UInt8(),
        )
        post_new_game_box, exists = op.AcctParamsGet.acct_min_balance(
            Global.current_application_address
        )
        assert exists
        assert mbr.amount == (post_new_game_box - pre_new_game_box)

        return self.id_counter

    @arc4.abimethod(allow_actions=[OnCompleteAction.NoOp, OnCompleteAction.OptIn])
    def join(self, game_id: UInt64) -> None:
        if Txn.on_completion == OnCompleteAction.OptIn:
            self.opt_in()

        assert self.games[game_id].host.native != Txn.sender
        assert self.games[game_id].guest == arc4.Address()

        self.games[game_id].guest = arc4.Address(Txn.sender)

    @arc4.abimethod
    def move(self, game_id: UInt64, x: UInt64, y: UInt64) -> None:
        game = self.games[game_id].copy()

        assert not game.is_over.native
        assert game.board[self.coord_to_matrix_index(x, y)] == arc4.Byte()
        assert Txn.sender == game.host.native or Txn.sender == game.guest.native
        is_host = Txn.sender == game.host.native

        if is_host:
            assert game.turns.native % 2 == 0
            self.games[game_id].board[self.coord_to_matrix_index(x, y)] = arc4.Byte(
                HOST_MARK
            )
        else:
            assert game.turns.native % 2 == 1
            self.games[game_id].board[self.coord_to_matrix_index(x, y)] = arc4.Byte(
                GUEST_MARK
            )

        self.games[game_id].turns = arc4.UInt8(
            self.games[game_id].turns.native + UInt64(1)
        )

    @subroutine
    def is_game_over(self, board: Board) -> Tuple[bool, bool]:
        for i in urange(3):
            if board[3 * i] == board[3 * i + 1] == board[3 * i + 2] != arc4.Byte():
                return True, False
            if board[i] == board[i + 3] == board[i + 6] != arc4.Byte():
                return True, False
            if board[0] == board[4] == board[8] != arc4.Byte():
                return True, False
            if board[2] == board[4] == board[6] != arc4.Byte():
                return True, False
            
            # Draw check
            for i in urange(9):
                if board[i] == arc4.Byte():
                    return False, False
            
        return True, True
