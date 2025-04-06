# Weather MCP Server

A Model Context Protocol (MCP) server that provides real-time weather forecasts and severe weather alerts using the WeatherAPI.com service.

## Features

- Get detailed weather forecasts for any location worldwide
- Retrieve current conditions, hourly forecasts, and multi-day forecasts
- Check for severe weather alerts and warnings
- Secure API key handling through environment variables
- Comprehensive error handling with helpful feedback
- Easy integration with Claude Desktop

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) WeatherAPI.com API key for production use

## Installation

1. (Recommended) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate    # On Windows
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. (Optional) Set up your WeatherAPI.com API key:
   - Create a free account at [WeatherAPI.com](https://www.weatherapi.com/)
   - Get your API key from the dashboard
   - Add the API key to your environment variables or create a `.env` file:
     ```
     WEATHER_API_KEY=your_api_key_here
     ```

## Usage

### Running with MCP CLI

If you have the MCP CLI installed, you can run:

```
mcp install server.py
```

This will install the server in Claude Desktop.

### Running with Python

Alternatively, you can run the server directly with Python:

```
python server.py
```

### Available Tools

The server provides the following tools for accessing weather data:

- `get_forecast`: Get a detailed weather forecast for a specified location
  - Includes current conditions, hourly forecasts, and multi-day forecasts
  - Supports location search by city name, postal code, or coordinates
  - Customizable forecast days (1-3 days)

- `get_alerts`: Get severe weather alerts for a specified location
  - Provides critical weather warnings and advisories
  - Includes alert title, severity, urgency, and description
  - Supports the same location formats as get_forecast

### Example Queries

- "What's the weather forecast for New York City?"
- "Are there any severe weather alerts in Miami?"
- "What will the temperature be in San Francisco tomorrow?"
- "Is it going to rain in Seattle this weekend?"

### Connecting to Claude Desktop

1. Create or update your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Add the following configuration:
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "python",
         "args": [
           "/Users/bluebird/develop/ai-agents/weather_mcp/server.py"
         ],
         "cwd": "/Users/bluebird/develop/ai-agents/weather_mcp"
       }
     }
   }
   ```

3. Restart Claude Desktop

## Integrating with Claude Code

You can also use this MCP server with Claude Code. Here's how to set it up:

1. Start the Weather MCP server on your local machine:
   ```bash
   python server.py
   ```

2. Create a `.claude.yaml` file in your project directory with the following content:
   ```yaml
   mcp_servers:
     - name: Weather
       url: http://localhost:8001
       env:
         WEATHER_API_KEY: your_api_key_here
   ```

3. Replace `your_api_key_here` with your actual WeatherAPI.com API key.

4. Install and configure Claude Code:

   a. Install the Claude Code CLI if you haven't already:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

   b. Log in to Claude Code:
   ```bash
   claude login
   ```

   c. Add the Weather MCP server to Claude Code:
   ```bash
   claude mcp add --name "Weather" --url "http://localhost:8001"
   ```

   d. Verify the MCP server is added:
   ```bash
   claude mcp list
   ```

5. Use the Claude Code CLI to interact with the Weather MCP server:
   ```bash
   claude code "What's the weather forecast for New York City?"
   ```

For more details, refer to the [Claude Code documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials).

## Available Tools

- `get_forecast`: Get the weather forecast for a location
  - Parameters:
    - `location`: City name or location (e.g., "San Francisco, CA")
    - `days`: Number of days for the forecast (1-3)

- `get_alerts`: Get severe weather alerts for a location
  - Parameters:
    - `location`: City name or location (e.g., "San Francisco, CA")

## Example Prompts

- "What's the weather forecast for New York City?"
- "Are there any severe weather alerts in Miami right now?"
- "What will the weather be like in Tokyo for the next 3 days?"
