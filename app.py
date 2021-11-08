from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def show_name():
    name = request.get_json()["name"]
    if name == "minsoo":
        return jsonify({"Answer" : "Hi", "name" : name})
    else:
        return jsonify({"Answer" : "Who are u", "name" : name})

if __name__ == "__main__":
    print("Server is running")
    app.run(host="0.0.0.0", port="8080")