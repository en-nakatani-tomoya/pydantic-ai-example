from dataclasses import dataclass
from pydantic_ai import Agent, RunContext, Tool


@dataclass
class Coin:
    name: str


@dataclass
class MaximalistComment:
    coin: Coin

    def __str__(self):
        return f"BUY {self.coin.name} !"


class BlockChainDataBase:
    _coin_mapping: dict[int, Coin] = {
        1: Coin(name="BTC"),
        2: Coin(name="ETH"),
        3: Coin(name="XRP"),
    }

    def get_coin_name(self, market_cap_rank: int) -> Coin:
        return self._coin_mapping[market_cap_rank]


@dataclass
class CoinAnalystDependency:
    market_cap_rank: int
    db: BlockChainDataBase


def fetch_coin_name(ctx: RunContext[CoinAnalystDependency]) -> str:
    """Fetch the coin name from the database"""
    try:
        return ctx.deps.db.get_coin_name(ctx.deps.market_cap_rank)
    except KeyError:
        return f"Not found {ctx.deps.market_cap_rank} ranked coin in the database"


if __name__ == "__main__":
    agent_tools = [Tool(fetch_coin_name)]
    agent = Agent("openai:gpt-4o", tools=agent_tools)

    trader_prompt = "I wanna buy high market cap coin"

    for rank in [1, 2, 3, 4]:
        deps = CoinAnalystDependency(market_cap_rank=rank, db=BlockChainDataBase())
        result = agent.run_sync(trader_prompt, deps=deps, result_type=MaximalistComment)
        print(result.data)
