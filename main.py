
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import sys

# Create a Flask app
app = Flask(__name__)

# Routes
@app.route('/')
def index():
    # Render the index page
    return render_template('index.html')

@app.route('/start_match', methods=['POST'])
def start_match():
    # Get the parameters from the request
    params = request.form.to_dict()

    # Spawn the autonomous agents and start a new match
    match = start_new_match(params)

    # Return the match ID
    return jsonify({'match_id': match.id})

@app.route('/stop_match', methods=['POST'])
def stop_match():
    # Get the match ID from the request
    match_id = request.form.get('match_id')

    # Stop the match
    stop_match(match_id)

    # Return a success message
    return jsonify({'success': True})

@app.route('/agent_control', methods=['POST'])
def agent_control():
    # Get the agent ID and action from the request
    agent_id = request.form.get('agent_id')
    action = request.form.get('action')

    # Update the agent's movement or abilities
    update_agent(agent_id, action)

    # Return a success message
    return jsonify({'success': True})

@app.route('/get_game_results', methods=['GET'])
def get_game_results():
    # Get the match ID from the request
    match_id = request.args.get('match_id')

    # Get the game results
    results = get_match_results(match_id)

    # Return the results
    return jsonify(results)

@app.route('/static_files/<path:path>')
def static_files(path):
    # Serve static files
    return send_from_directory('static', path)

# Start the app
if __name__ == '__main__':
    app.run()
