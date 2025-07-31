import logging
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
import algokit_utils
from algokit_utils import (
    EnsureBalanceParameters,
    TransactionParameters,
    ensure_funded,
)
from algokit_utils.beta.algorand_client import AlgorandClient
from algokit_utils.beta.client_manager import AlgoSdkClients

logger = logging.getLogger(__name__)

def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.tictactoe.tic_tac_toe_client import (
        TicTacToeClient,
    )
    
    app_client = TicTacToeClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )
    
    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )
