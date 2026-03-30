class StartupKnowledgeGraph:

    def connect(self, idea, markets):

        return {
            "nodes": [idea, markets],
            "relationships": ["solution-for"]
        }
