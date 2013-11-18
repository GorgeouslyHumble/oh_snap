from oh_snap import app
from oh_snap.modules.api import API
from oh_snap.modules.storage import Storage
from flask import Flask, request, render_template

#API - Just the groundwork. I won't have these routes do anything yet
@app.route('/api/v1/guide')
@app.route('/api/v1/guide/<uuid>')
def return_guide_json(uuid=None):
	return 'hello'

@app.route('/api/v1/guide_list')
def return_guides_json():
	return 'hello'

@app.route('/api/v1/top_guides')
def return_top_guides_json():
	return 'hello'

@app.route('/api/v1/store_guides')
def store_guides():
  store = Storage()

  store.store_guides_from_top()

  return 'success'

#UI routes

#HELLO WORLD
@app.route('/')
def index():
	return render_template('index.html')

#A route for inspecting a single guide
@app.route('/guide')
@app.route('/guide/<uuid>')
def return_guide(uuid=None):
	request = API()
	guide_json = request.retrieve_guide(uuid)

	return render_template('guide.html', guide_json=guide_json)

#A route for aggregating all the guides
@app.route('/guides')
def return_guides():
	request = API()
	guide_list_params = {'time_point' : 'latest', 'limit' : '100'}
	guide_list_json = request.retrieve_guide_list(**guide_list_params)

	return render_template('guides.html', guide_list_json=guide_list_json)

#A route for aggregating the top guides
@app.route('/top_guides')
def return_top_guides():
	return render_template('top_guides.html')
