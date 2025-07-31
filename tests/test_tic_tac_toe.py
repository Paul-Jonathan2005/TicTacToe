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
