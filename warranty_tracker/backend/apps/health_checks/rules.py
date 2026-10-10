
def evaluate(category, responses):
    # Basic rule engine
    risk = "GREEN"
    issue = "No significant issue reported based on your responses."
    rec = "No immediate action needed."
    
    if category == "laptop" or category == "smartphone":
        if responses.get("battery_drain") == "YES":
            risk = "YELLOW"
            issue = "Potential battery-performance issue"
            rec = "Consider professional inspection before warranty expiry."
        if responses.get("overheating") == "YES" and responses.get("unexpected_shutdown") == "YES":
            risk = "RED"
            issue = "Critical Thermal Issue"
            rec = "Service Recommended. Authorized inspection required."
            
    if category == "washing_machine":
        if responses.get("water_leakage") == "YES":
            risk = "RED"
            issue = "Water Leakage Detected"
            rec = "Service Recommended. Do not use until inspected."
            
    return risk, issue, rec
