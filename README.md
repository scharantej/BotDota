## Flask Application Design for Autonomous Dota 2 Agents

### HTML Files
- **index.html**:
    - Main page to control and monitor the agents.
    - Contains fields for setting game parameters, starting/stopping matches, and displaying match results.

- **agent\_control.html**:
    - Embedded in index.html to control individual agents.
    - Provides buttons to toggle agent abilities, change movement, etc.

- **game\_results.html**:
    - Displays the outcome of matches, including win/loss status, scores, and other relevant statistics.

### Routes

- **index**:
    - Renders the index.html page.

- **start\_match**:
    - Accepts parameters from index.html (e.g., teams, match duration).
    - Spawns the autonomous agents and starts a new match.

- **stop\_match**:
    - Stops the currently ongoing match.

- **agent\_control**:
    - Updates the movement or abilities of a specific agent.

- **get\_game\_results**:
    - Returns the results of the match in JSON format.

- **static\_files**:
    - Serves static files such as scripts, stylesheets, and images necessary for the application's frontend.