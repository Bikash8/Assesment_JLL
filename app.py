from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

    
@app.route('/api/<string:typee>/<string:data>/', methods=['GET'])
def get_sub(typee,data):
    filename = "Brill_Global_eBooks_TitleList.csv"
    fields = []
    res = []
    print(data)
    if typee == "subject":
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                if data in row[3]:
                    res.append(row)
    if typee == "YearPublished":
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                if data in row[2]:
                    res.append(row)
    if typee == "author":
        data = data.replace("+", " ")
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                if data in row[0]:
                    res.append(row)
    if typee == "name":
        data = data.replace("+", " ")
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                if data in row[1]:
                    res.append(row)
    return jsonify(res)  # result convert to JSON then return


if __name__ == '__main__': # main function To run the flask app
    app.run()
