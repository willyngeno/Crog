from  flask  import  Flask, request,jsonify
app = Flask(__name__)

JSON = [{'status_name' : 'example_name'},{'current_day' : 'Monday'}, {'utc_time' : '2023-08-21T15:04:05Z'},{'track': 'backend'},{'github_file_url':'https://github.com/username/repo/blob/main/file_name.ext','github_repo_url':'https://github.com/username/repo'},{'status_code':200}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'it works'})

@app.route('/lang',methods=['GET'])
def returnAll():
    return jsonify({'jsonsi':JSON})
@app.route ('/lang/<string:name>', methods=['GET'])
def  returnOne(name):
    langs = [jsonsi for jsonsi in JSON['name'] == name]
    return jsonify({'jsonsi' : langs[0]})
@app.route('/lang', methods=['POST'])
def addOne():
    jsonsi = {'name' : request.json['name']}
    
    JSON.append(jsonsi)
    return jsonify({'JSON' : JSON})

if  __name__ == '__main__':
    app.run(debug=True, port=8080)