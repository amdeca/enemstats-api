from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.errors import InvalidId
import re

app = Flask(__name__)
CORS(app)
#Copypaste the connection string from Mongodb Atlas
mongo = MongoClient("connection string")
#Select database
db = mongo['enem_db']
#Select collection
schools = db['schools']

#get school by search parameters
@app.route('/api/schools', methods=['GET'])
def get_school_by_name():
    #named parameters ?q and filter $year
    name = request.args.get('q')
    year = request.args.get('year')
    state = request.args.get('state')
    limit = 10
    
    #prepare regex, case insensitive
    search_string = '.*{}.*'.format(name)
    rgx = re.compile(search_string, re.IGNORECASE)
    
    if state:
        #ommit the _id to prevent error
        query = schools.find({"ESCOLA" : rgx, "NU_ANO" : year, "UF" : state}).sort('ESCOLA').limit(limit)
    else:
        #query collection with regex
        query = schools.find({"ESCOLA" : rgx, "NU_ANO" : year}).sort('ESCOLA').limit(limit)
        
    #Process the data from the query cursor creating a dict
    output = {}
    output['number_of_results'] = query.count()
    #Results key
    results = []
    for school in query:
        results.append(
            {
                'id' : str(school['_id']),
                'year' : school['NU_ANO'],
                'region' : school['REGIAO'],
                'state' : school['UF'],
                'city' : school['MUNICIPIO'],
                'name' : school['ESCOLA'],
                'type' : school['TIPOESCOLA'],
                'avg_ch' : school['MEDIA CH'],
                'avg_cn' : school['MEDIA CN'],
                'avg_lc' : school['MEDIA LC'],
                'avg_math' : school['MEDIA MT'],
                'avg_essay' : school['MEDIA REDACAO']
            }
        )
    output['results'] = results

    return jsonify(output)

#get school by id
@app.route('/api/schools/<school_id>', methods=['GET'])
def get_school_by_id(school_id):
    try:
        query = schools.find_one({'_id': ObjectId(school_id)}, {'_id':0})
        #output = [query]
        result = []
        result.append(
            {
            'city': query['MUNICIPIO'],
            'year': query['NU_ANO'],
            'region': query['REGIAO'],
            'type': query['TIPOESCOLA'],
            'state': query['UF'],
            'school_name': query['ESCOLA'],
            'avg_ch': query['MEDIA CH'], 
            'avg_cn': query['MEDIA CN'], 
            'avg_lc': query['MEDIA LC'], 
            'avg_mt': query['MEDIA MT'], 
            'avg_essay': query['MEDIA REDACAO']
            }
        )

    except InvalidId:
        result = 'ID not found'

    return jsonify({'results' : result})

@app.route('/api/schools/year', methods=['GET'])
def get_school_grades():
    #search parameters
    name = request.args.get('name')
    city = request.args.get('city')
    state = request.args.get('state')
    
    #school name regex
    search_string = '.*{}.*'.format(name)
    rgx = re.compile(search_string, re.IGNORECASE)
    #city regex
    city_rgx = re.compile('.*{}.*'.format(city), re.IGNORECASE)

    query = schools.find({"ESCOLA" : rgx, "MUNICIPIO": city_rgx, "UF" : state}).sort('NU_ANO')
        
    output = {}
    output['number_of_results'] = query.count()
    #Results key
    results = []
    for result in query:
        results.append(
            {
                'id' : str(result['_id']),
                'year' : result['NU_ANO'],
                'region' : result['REGIAO'],
                'state' : result['UF'],
                'city' : result['MUNICIPIO'],
                'name' : result['ESCOLA'],
                'type' : result['TIPOESCOLA'],
                'avg_ch' : result['MEDIA CH'],
                'avg_cn' : result['MEDIA CN'],
                'avg_lc' : result['MEDIA LC'],
                'avg_math' : result['MEDIA MT'],
                'avg_essay' : result['MEDIA REDACAO']
            }
        )
    output['results'] = results

    return jsonify(output)

@app.route('/api/states', methods=['GET'])
def get_grades_by_state():

    col = db['states']

    state = request.args.get('state')
    year = request.args.get('year')

    if state:
        if year:
            query = col.find({"UF" : state, "NU_ANO" : year}).sort('NU_ANO')
        else:
            query = col.find({"UF" : state}).sort('NU_ANO')
    else:
        query = col.find().sort('NU_ANO')

    output = {}
    output['number_of_results'] = query.count()
    #Results key
    results = []
    for result in query:
        results.append(
            {
                'id' : str(result['_id']),
                'year' : result['NU_ANO'],
                'state' : result['UF'],
                'avg_ch' : result['MEDIA CH'],
                'avg_cn' : result['MEDIA CN'],
                'avg_lc' : result['MEDIA LC'],
                'avg_math' : result['MEDIA MT'],
                'avg_essay' : result['MEDIA REDACAO']
            }
        )
    output['results'] = results
    return jsonify(output)

@app.route('/api/national', methods=['GET'])
def get_nation_grades():
    col = db['national']

    year = request.args.get('year')
    if year:
        query = col.find({"NU_ANO" : year}).sort('NU_ANO')
    else:
        query = col.find().sort("NU_ANO")
    
    output = {}
    output['number_of_results'] = query.count()
    #Results key
    results = []
    for result in query:
        results.append(
            {
                'id' : str(result['_id']),
                'year' : result['NU_ANO'],
                'avg_ch' : result['MEDIA CH'],
                'avg_cn' : result['MEDIA CN'],
                'avg_lc' : result['MEDIA LC'],
                'avg_math' : result['MEDIA MT'],
                'avg_essay' : result['MEDIA REDACAO']
            }
        )
    output['results'] = results
    return jsonify(output)

    
if __name__ == "__main__":
    app.run(debug=True)