@app.route("/getslides", methods=['POST'])  # Just to check the server is running
    return jsonify({"slides": user_data[:-1]})


@app.route("/register", methods=['POST'])  # Register
username
password
        return jsonify({'response': 'success'})



@app.route("/login", methods=['POST'])  # Login
username
password
 jsonify({'response': 'success',
                            'version': ver,
                            'user': user[0][0]})
jsonify({'response': 'failed',
                            'version': ver,
                            'error': "Invalid Password!"})
jsonify({'response': 'failed',
                        'version': ver,
                        'error': "User doesn't exist!"})



@app.route("/get_image_number", methods=['POST'])  # Get image Number

jsonify({'response': 'completed'})
jsonify({'response': 'slide_completed'})
jsonify({'response': 'success', 'image_name': empty_label_images[0]})

@app.route("/get_image", methods=['POST'])
raw image




@app.route("/give_label", methods=['POST'])

username = user_data["username"]
    imname = user_data["image_name"]
    label = user_data['label']

    return jsonify({'response': 'success', 'id': str(id_)})


@app.route("/update_label", methods=['POST'])


    return jsonify({'response': 'success', 'id': str(user_data['id'])})


@app.route("/get_history", methods=['POST'])
    username = user_data["username"]
    slide = user_data["slide"]

        return jsonify({"data": history})
@app.route("/reset_slide", methods=['POST'])
    return jsonify({'response': 'success'})
