# AI Agents for Claude Desktop

This repository contains Model Context Protocol (MCP) servers that extend Claude Desktop's capabilities by connecting to external APIs. These servers act as bridges between Claude and various data sources, enabling Claude to access real-time information and services.

## Available MCP Servers

### 1. Regulations.gov MCP Server

Allows Claude Desktop to interact with the regulations.gov API (v4), enabling searches for regulatory documents, comments, and dockets. This server provides access to the vast repository of federal regulatory materials.

### 2. Weather MCP Server

Provides Claude Desktop with real-time weather forecasts and severe weather alerts using the WeatherAPI.com service. This server enables Claude to answer questions about current and future weather conditions worldwide.

## Features

### Regulations.gov MCP Server (Python Version)

- Search for regulatory documents with filters for search terms, dates, document types, and agencies
- Search for public comments with similar filtering options
- Search for regulatory dockets
- Get detailed information about specific documents, comments, and dockets
- List common agency IDs for easier searching
- Improved error handling with helpful feedback

### Weather MCP Server

- Get detailed weather forecasts for any location worldwide
- Retrieve current conditions, hourly forecasts, and multi-day forecasts
- Check for severe weather alerts and warnings
- Secure API key handling through environment variables

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Required) regulations.gov API key for full access to the regulations.gov API
- (Required) WeatherAPI.com API key for production use of the weather service

## Installation

### Regulations.gov MCP Server

1. Navigate to the regulations_mcp directory:

   ```
   cd regulations_mcp
   ```

2. (Recommended) Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate    # On Windows
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. (Required) Set up your regulations.gov API key in a `.env` file or environment variable:
   ```
   REGULATIONS_GOV_API_KEY=your_api_key_here
   ```

### Weather MCP Server

1. Navigate to the weather_mcp directory:

   ```
   cd weather_mcp
   ```

2. (Recommended) Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate    # On Windows
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. (Required) Set up your WeatherAPI.com API key in a `.env` file or environment variable:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```

## Usage

### Running the Regulations.gov MCP Server

```
cd regulations_mcp
python server.py
```

### Running the Weather MCP Server

```
cd weather_mcp
python server.py
```

## Connecting to Claude Desktop

1. Update your Claude Desktop configuration file:

   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Add both MCP servers to the configuration:

   ```json
   {
     "mcpServers": [
       {
         "name": "Regulations.gov",
         "url": "http://localhost:8000",
         "env": {
           "REGULATIONS_GOV_API_KEY": "your_api_key_here"
         }
       },
       {
         "name": "Weather",
         "url": "http://localhost:8001",
         "env": {
           "WEATHER_API_KEY": "your_api_key_here"
         }
       }
     ]
   }
   ```

3. Restart Claude Desktop to apply the changes

Claude should now be able to use both the Regulations.gov and Weather MCP servers to access real-time data.

## Available Tools

### Regulations.gov MCP Server Tools

- `search_documents` - Search for regulatory documents with filters
- `search_comments` - Search for public comments
- `search_dockets` - Search for regulatory dockets
- `get_document_details` - Get detailed information about a specific document
- `get_comment_details` - Get detailed information about a specific comment
- `get_docket_details` - Get detailed information about a specific docket
- `list_agencies` - List common agency IDs for searching

### Weather MCP Server Tools

- `get_forecast` - Get a detailed weather forecast for a location
- `get_alerts` - Get severe weather alerts for a location

## Development

### Running with Debug Logging

To run either server with more detailed logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Testing the Servers

You can test the servers directly using Python:

```python
# Test Regulations.gov MCP Server
from regulations_mcp.server import search_documents
result = search_documents(agency="EPA", posted_date_from="2024-01-01")
print(result)

# Test Weather MCP Server
from weather_mcp.server import get_forecast
result = get_forecast(location="New York")
print(result)
```

## Additional Resources

- [Regulations.gov API Documentation](https://open.gsa.gov/api/regulationsgov/)
- [WeatherAPI.com Documentation](https://www.weatherapi.com/docs/)
- [Model Context Protocol (MCP) Documentation](https://github.com/anthropics/anthropic-tools)
