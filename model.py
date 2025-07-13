import os
import requests
import time

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
MODEL_VERSION = "db21e45c-5bdf-4b43-9f7c-7b7e7c4b3bfa"

headers = {
    "Authorization": f"Token {r8_F8BktKh3AVZ9r45MQkSAFH5SeRMVFP91QaNuF}",
    "Content-Type": "application/json"
}

def generate_image(prompt):
    url = "https://api.replicate.com/v1/predictions"
    data = {
        "version": MODEL_VERSION,
        "input": {"prompt": prompt}
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 201:
        return "❌ Error: Failed to start prediction."

    prediction_url = response.json()["urls"]["get"]

    while True:
        status_response = requests.get(prediction_url, headers=headers).json()
        if status_response["status"] == "succeeded":
            return status_response["output"][0]
        elif status_response["status"] == "failed":
            return "❌ Image generation failed."
        time.sleep(1)
