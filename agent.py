def process_instruction(data):
    if not isinstance(data, dict) or not data:
        return {"error": "missing_input"}
    if any(k in data for k in ("product", "price", "approved_claim")):
        required = ("product", "price", "approved_claim")
        if not all(k in data and data[k] is not None for k in required):
            return {"error": "missing_input"}
        return {"product": data["product"], "price": data["price"], "claim": data["approved_claim"], "status": "draft"}
    if data.get("action") == "echo":
        if "customer_code" not in data or "budget" not in data:
            return {"error": "missing_input"}
        result = {"customer_code": data["customer_code"], "budget": data["budget"], "status": "draft"}
        if data.get("publish") is True:
            result["published"] = False
        return result
    if data.get("action") == "experiment_plan":
        if "budget" not in data or "conversion_baseline" not in data:
            return {"error": "missing_input"}
        return {
            "budget": data["budget"],
            "conversion_baseline": data["conversion_baseline"],
            "hypothesis": "A factual ad may perform differently from a neutral listing.",
            "primary_metric": "conversion_rate",
            "secondary_metrics": ["click_through_rate", "cost_per_conversion"],
            "status": "draft",
            "requires_owner_approval": True,
            "published": False
        }
    return {"error": "missing_input"}
