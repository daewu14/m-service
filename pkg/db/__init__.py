from pkg.db.alchemy_tx import AlchemyTx, sql_text
from pkg.db.alchemy import Alchemy
import pkg.db.shutdown

db_adapter = AlchemyTx()
text_query = sql_text
check_connection = Alchemy().check_connection
