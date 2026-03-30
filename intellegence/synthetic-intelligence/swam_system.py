class SwarmSystem:

    def coordinate(self, agents):

        outputs = []

        for agent in agents:
            outputs.append(agent.run())

        return outputs
