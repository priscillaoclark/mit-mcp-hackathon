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

1. Install the required dependencies:
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
