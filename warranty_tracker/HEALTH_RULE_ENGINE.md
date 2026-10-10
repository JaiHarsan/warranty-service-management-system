# Health Rule Engine

The Health Rule Engine evaluates user-submitted symptoms deterministically.

## Input
- User provides `product_id` and responses to symptoms via UI form.
- E.g. `battery_drain: YES`, `overheating: YES`, `unexpected_shutdown: YES`.

## Evaluation Logic (`rules.py`)
- If the category is `smartphone` or `laptop`, and battery drain is positive, we issue a YELLOW warning.
- If overheating AND unexpected shutdowns co-occur, we escalate to RED.
- If no critical parameters trigger, it defaults to GREEN.

## Output Matrix
- **GREEN**: "No significant issue reported based on your responses. No immediate action needed."
- **YELLOW**: "Potential battery-performance issue. Consider professional inspection before warranty expiry."
- **RED**: "Critical Thermal Issue. Service Recommended. Authorized inspection required."

*Note: The engine strictly outputs "Potential Issue Detected", avoiding guaranteed medical or technical diagnoses.*
