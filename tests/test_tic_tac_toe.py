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
    pass
def test_double_join_prevention(algorand):
    pass
def test_invalid_move_occupied_cell(algorand):
    pass
def test_draw_condition(algorand):
    pass
def reset_game_state():
    pass
def test_host_cannot_join_as_guest(algorand):
    pass
def test_only_host_can_delete_game(algorand):
    pass
def test_game_state_persistence(algorand):
    pass
def test_opt_in_initializes_state(algorand):
    pass
