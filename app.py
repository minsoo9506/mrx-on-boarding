from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def show_name():
    name = request.args.get("name")
    if name != "minsoo":
        return jsonify({"Answer" : "Hi"})
    else:
        return jsonify({"Erro" : "Who are u"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")