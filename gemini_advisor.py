import os
import time
from google import genai


def explain_prediction(vehicle_id, sensors, risk_level, days_to_failure):
    try:
        key = os.getenv("GEMINI_API_KEY", "")
        if not key:
            raise ValueError("No key")
        client = genai.Client(api_key=key)

        for attempt in range(3):  # retry up to 3 times
            try:
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=f"""You are an automotive expert for a logistics fleet manager.
Vehicle {vehicle_id} sensors: {sensors}
ML prediction: {risk_level} risk, failure in {days_to_failure} days.
Explain in 3 simple sentences a non-technical manager understands.
End with one clear action."""
                )
                return response.text
            except Exception as e:
                if "429" in str(e) and attempt < 2:
                    time.sleep(5)  # wait 5 seconds then retry
                    continue
                raise
    except Exception as e:
        return f"Vehicle {vehicle_id} shows {risk_level} risk. Failure expected in {days_to_failure} days. Recommend scheduling maintenance soon."