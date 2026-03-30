class SyntheticIntelligence:

    def evolve(self, agents):

        for agent in agents:
            agent.improve()

        return agents
