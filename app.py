from flask import Flask, request, jsonify
from bot import detect_question, send_message

app = Flask(__name__)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.get_json()

    # Handle Slack's URL verification challenge
    if data.get("type") == "url_verification":
        return jsonify({"challenge": data.get("challenge")})

    # Handle incoming events (basic structure)
    if data.get("type") == "event_callback":
        event = data.get("event")

         # Ignore messages from bots (including this one)
        if event.get("bot_id"):
            return "", 200
        
        text = event.get("text")
        print("Received event:", event)
        # print("This is the message:" , text)

        # Detects if incoming message is a question
        if text:
            is_question = detect_question(text)
            if is_question:
                print("Alert! Message: ", text, " is a question.")
                send_message(event.get("channel"), "Alert! Message: " +  text + " is a question.")
            else:
                print("Message received, but not a question:", text)

    return "", 200

if __name__ == "__main__":
    app.run(port=3000)
