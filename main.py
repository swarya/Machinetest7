import pandas as pd
from fastapi import FastAPI

email = FastAPI()

# Function to perform scam detection (dummy function for demonstration)
def detect_scam(text: str) -> bool:
    # Replace this with your actual scam detection logic
    scam_keywords = ["scam", "fraud", "phishing", "spam"]
    for keyword in scam_keywords:
        if keyword in text.lower():
            return True
    return False

@email.post("/check_scam")
async def check_scam(text_data: dict):
    try:
        text = text_data["text"]
    except KeyError:
        return {"error": "Field 'text' is required"}

    # Perform scam detection
    is_scam = detect_scam(text)

    return {"text": text, "is_spam": is_scam}

# Read the CSV file
df = pd.read_csv("emails.csv")

# Run the FastAPI server
if __name__ == "_main_":
    import uvicorn
    uvicorn.run(email, host="127.0.0.1", port=8000)