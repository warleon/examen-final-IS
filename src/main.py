from flask import Flask, request, jsonify

app = Flask(__name__)

messages={}


@app.route("/message/<topic>", methods=["GET"])
def get_message(topic):
	if topic in messages:
		return jsonify(messages[topic])
	else:
		return jsonify([])

@app.route("/message", methods=["POST"])
def set_message():
	try:
		topic = request.json['topic']
		message = request.json['message']
		if topic not in messages:
			messages[topic]=[]

		messages[topic].append(message)
		return jsonify({"status":"ok"})
	except:
		return jsonify({"status":"fail"})

if __name__ == '__main__':
    app.run(debug=True)