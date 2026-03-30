class Agent:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    async def execute(self, input_data):
        return await self.model.generate(input_data)
