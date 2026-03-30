class BusinessPlanAgent:

    async def run(self, research):

        return {
            "model": "subscription",
            "pricing": [5,10,20],
            "target_market": research["market_size"],
            "strategy": "digital first"
        }
