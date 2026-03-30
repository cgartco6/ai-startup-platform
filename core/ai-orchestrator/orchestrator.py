from agents.registry import AgentRegistry

class AIOrchestrator:

    def __init__(self):
        self.registry = AgentRegistry()

    async def run_startup_pipeline(self, idea):

        research = await self.registry.run("research-agent", idea)

        business = await self.registry.run(
            "business-plan-agent",
            research
        )

        website = await self.registry.run(
            "website-builder-agent",
            business
        )

        marketing = await self.registry.run(
            "marketing-agent",
            website
        )

        return {
            "research": research,
            "business": business,
            "website": website,
            "marketing": marketing
        }
