from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy wallet
wallet = {
    "USD": 1000,
    "BTC": 0
}

BTC_PRICE = 100  # Dummy price (later API se laenge)

@app.route("/")
def home():
    return "🚀 Trading App Running"

@app.route("/balance")
def balance():
    return jsonify(wallet)

@app.route("/buy", methods=["POST"])
def buy():
    amount = float(request.json.get("amount", 0))

    if amount > wallet["USD"]:
        return jsonify({"error": "Insufficient USD"}), 400

    btc_bought = amount / BTC_PRICE
    wallet["USD"] -= amount
    wallet["BTC"] += btc_bought

    return jsonify({
        "message": "Buy successful",
        "wallet": wallet
    })

@app.route("/sell", methods=["POST"])
def sell():
    btc = float(request.json.get("btc", 0))

    if btc > wallet["BTC"]:
        return jsonify({"error": "Insufficient BTC"}), 400

    usd_gained = btc * BTC_PRICE
    wallet["BTC"] -= btc
    wallet["USD"] += usd_gained

    return jsonify({
        "message": "Sell successful",
        "wallet": wallet
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
