from client import CrossModalCreativeCampaignPlannerClient

def main():
    client = CrossModalCreativeCampaignPlannerClient()
    res = client.plan_campaign({"primary_color": "#0066FF", "tone": "bold"}, ["Tech Founders", "DevOps Leads"])
    print(f"Readiness Score: {res['campaign_readiness_score']}/10")
    print("Creative Concepts:", res["creative_concepts"])
    print("Asset Matrix Grid:", res["asset_matrix_grid"])

if __name__ == "__main__":
    main()
