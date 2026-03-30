from core.agent_runtime.runtime import Agent

class IdeaAgent(Agent):

    async def execute(self, user_prompt):

        prompt = f"""
        Generate startup ideas based on:

        {user_prompt}

        Provide:
        - market
        - problem
        - solution
        - revenue model
        """

        return await self.model.generate(prompt)
