class WebsiteBuilderAgent:

    async def run(self, business):

        site = {
            "homepage": "generated",
            "pricing": business["pricing"],
            "signup": True
        }

        return site
