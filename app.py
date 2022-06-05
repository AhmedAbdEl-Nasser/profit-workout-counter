from flask import Flask, request, jsonify
# from biceps import Workout
# import werkzeug

app = Flask(__name__)

# @app.route('/upload', methods=['GET', 'POST'])
@app.route('/')
@app.route('/index')
@app.route('/homepage')
def calculate():
    # workout = Workout()
    # result = workout.workout_detection(number=1, video=video)
    # print(result)
    # return 'ok'

    # Post request
    # if request.method == 'POST':
    #     videofile = request.files['workoutVideo']  # Important key
    #     videoname = werkzeug.utils.secure_filename(videofile.filename)
    #     videofile.save(videoname)
    #     workout = biceps.Workout()
    #     result = workout.workout_detection(number=1, video=videoname)
    #     print(result)
    #     return jsonify({
    #         "message": "Video uploaded successfully, workout detection results: " + str(result)
    #     })
    return jsonify({
        "message": "Hello"
    })

if __name__ == "__main__":
    app.run()