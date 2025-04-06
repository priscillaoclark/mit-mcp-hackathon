# Regulations.gov MCP Server

A Model Context Protocol (MCP) server that provides access to the regulations.gov API, allowing you to search for and retrieve information about regulatory documents, comments, and dockets.

## Features

- Search for regulatory documents, comments, and dockets
- Get detailed information about specific documents, comments, and dockets
- Easy integration with Claude Desktop

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- regulations.gov API key (optional, will use DEMO_KEY if not provided)

## Installation

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. (Optional) Set up your regulations.gov API key:
   - Create a free account at [regulations.gov](https://www.regulations.gov/)
   - Get your API key from the developer portal
   - Add the API key to your environment variables or create a `.env` file:
     ```
     REGULATIONS_GOV_API_KEY=your_api_key_here
     ```

## Usage

### Running with Python

You can run the server directly with Python:

```
python server.py
```

### Connecting to Claude Desktop

1. Update your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Add the following configuration:
   ```json
   {
     "mcpServers": {
       "regulations": {
         "command": "/Users/bluebird/.pyenv/shims/python",
         "args": ["/Users/bluebird/develop/ai-agents/regulations_mcp/server.py"],
         "cwd": "/Users/bluebird/develop/ai-agents/regulations_mcp",
         "env": {
           "REGULATIONS_GOV_API_KEY": "your_api_key_here"
         }
       }
     }
   }
   ```

3. Replace `your_api_key_here` with your actual regulations.gov API key
4. Restart Claude Desktop

## Available Tools

- `search_documents`: Search for regulatory documents
- `search_comments`: Search for public comments
- `search_dockets`: Search for regulatory dockets
- `get_document_details`: Get detailed information about a specific document
- `get_comment_details`: Get detailed information about a specific comment
- `get_docket_details`: Get detailed information about a specific docket

## Example Prompts

- "Find recent EPA documents about climate change"
- "Search for comments about vaccine regulations"
- "Get details about docket FDA-2023-N-0001"
- "What are the most recent FDA regulations?"
