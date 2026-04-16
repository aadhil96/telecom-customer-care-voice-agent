# In-memory databases
SUBSCRIPTIONS_DB = {"subscriptions": {}, "next_id": 1}

PLANS_DB = {
    "daily_1gb": {
        "name": "Daily 1GB Plan",
        "price": 1.50,
        "data": "1GB",
        "validity": "1 day",
        "description": "1GB data valid for 24 hours"
    },
    "weekly_5gb": {
        "name": "Weekly 5GB Plan",
        "price": 5.99,
        "data": "5GB",
        "validity": "7 days",
        "description": "5GB data valid for 7 days"
    },
    "monthly_20gb": {
        "name": "Monthly 20GB Plan",
        "price": 15.99,
        "data": "20GB",
        "validity": "30 days",
        "description": "20GB data valid for 30 days"
    }
}


def get_plan_info(plan_name):
    plan = PLANS_DB.get(plan_name.lower())
    if plan:
        return plan
    return {"error": f"Plan '{plan_name}' not found"}


def subscribe_plan(customer_name, plan_name):
    plan = PLANS_DB.get(plan_name.lower())
    if not plan:
        return {"error": f"Plan '{plan_name}' not found"}

    sub_id = SUBSCRIPTIONS_DB["next_id"]
    SUBSCRIPTIONS_DB["next_id"] += 1

    subscription = {
        "id": sub_id,
        "customer": customer_name,
        "plan": plan["name"],
        "price": plan["price"],
        "status": "active"
    }

    SUBSCRIPTIONS_DB["subscriptions"][sub_id] = subscription

    return {
        "subscription_id": sub_id,
        "message": f"{plan['name']} activated for {customer_name}",
        "price": plan["price"],
        "status": "active"
    }


def check_subscription(subscription_id):
    sub = SUBSCRIPTIONS_DB["subscriptions"].get(int(subscription_id))
    if sub:
        return sub
    return {"error": f"Subscription {subscription_id} not found"}


FUNCTION_MAP = {
    "get_plan_info": get_plan_info,
    "subscribe_plan": subscribe_plan,
    "check_subscription": check_subscription
}