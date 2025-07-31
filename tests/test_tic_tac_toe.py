import pytest
from algokit_utils import get_localnet_algod_client
from algosdk.atomic_transaction_composer import TransactionWithSigner
from algokit_utils.beta.algorand_client import AlgorandClient
from algokit_utils.beta.client_manager import AlgoSdkClients
from algokit_utils import (
    EnsureBalanceParameters,
    TransactionParameters,
    ensure_funded,
)
from algosdk.util import algos_to_microalgos

@pytest.fixture
def algorand():
    algod_client = get_localnet_algod_client()
    return AlgorandClient.from_clients(AlgoSdkClients(algod_client))

def test_tic_tac_toe_game(algorand):
    # Test creating a game
    # Test joining a game
    # Test making moves
    # Test win conditions
    pass
def test_double_join_prevention(algorand):
    # Setup game and join as guest
    # Attempt to join again as the same guest, expect failure
    pass
def test_invalid_move_occupied_cell(algorand):
    # Setup game, make a move, then try to move to the same cell, expect failure
    pass
def test_draw_condition(algorand):
    # Play a full game resulting in a draw, assert is_over and is_draw are set
    pass
def reset_game_state():
    # Logic to reset or re-initialize contract state for isolated tests
    pass
def test_host_cannot_join_as_guest(algorand):
    # Host creates game, then tries to join as guest, expect failure
    pass
def test_only_host_can_delete_game(algorand):
    # Guest tries to delete game, expect failure
    pass
