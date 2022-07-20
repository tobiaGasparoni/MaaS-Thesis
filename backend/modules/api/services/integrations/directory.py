from api.services.integrations.modules import diet_prices

def solve(integration, answers, data):
    if integration.ID == "cc38e1d6-ab22-48c4-8480-9a1039bb1372":
        return diet_prices.solve(answers, data)
