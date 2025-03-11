from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/getdata", methods=["POST"])
def getdata():
    try:
        data = request.json  # Expect JSON data
        array = list(map(int, data.get("numbers", "").split()))

        steps = []  # Store sorting steps
        count=0
        for i in range(len(array)):
            min_index = i
            for j in range(i+1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            if min_index != i:
                count=count+1
                array[i], array[min_index] = array[min_index], array[i]
                steps.append({
                    "array": array[:],  # Store current array state
                    "message": f" Step {count} : Swapped {array[min_index]} and {array[i]}",
                    
                    
                })
        if count==0:
            return jsonify({"alreadySort":"array already in sorted order"})

        return jsonify(steps)  # Return sorting steps

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
