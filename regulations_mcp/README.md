# Regulations.gov MCP Server

A Model Context Protocol (MCP) server that provides access to the regulations.gov API, allowing you to search for and retrieve information about regulatory documents, comments, and dockets.

## Features

- Search for regulatory documents, comments, and dockets with filters for:
  - Search terms
  - Date ranges (defaults to past year for better results)
  - Document types
  - Agencies
  - Docket IDs
- Get detailed information about specific documents, comments, and dockets
- List common agency IDs for easier searching
- Improved error handling and helpful feedback
- Easy integration with Claude Desktop

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- regulations.gov API key (optional, will use DEMO_KEY if not provided)

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

### Available Tools

The server provides the following tools for interacting with the regulations.gov API:

- `search_documents`: Search for regulatory documents with filters for search term, sort order, posted date, document type, docket ID, and agency
- `search_comments`: Search for public comments with similar filters
- `search_dockets`: Search for regulatory dockets
- `get_document_details`: Get detailed information about a specific document
- `get_comment_details`: Get detailed information about a specific comment
- `get_docket_details`: Get detailed information about a specific docket
- `list_agencies`: List common agency IDs that can be used for searching

### Tips for Effective Searching

- Use date filters to find more recent documents (defaults to past year if not specified)
- Search by agency ID (e.g., 'EPA', 'FDA', 'SEC') to narrow results
- Use specific keywords in search_term to find relevant documents
- Try different sort options (postedDate, title) to see different results

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

## Integrating with Claude Code

You can also use this MCP server with Claude Code. Here's how to set it up:

1. Start the Regulations.gov MCP server on your local machine:
   ```bash
   python server.py
   ```

2. Create a `.claude.yaml` file in your project directory with the following content:
   ```yaml
   mcp_servers:
     - name: Regulations.gov
       url: http://localhost:8000
       env:
         REGULATIONS_GOV_API_KEY: your_api_key_here
   ```

3. Replace `your_api_key_here` with your actual regulations.gov API key.

4. Install and configure Claude Code:

   a. Install the Claude Code CLI if you haven't already:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

   b. Log in to Claude Code:
   ```bash
   claude login
   ```

   c. Add the Regulations.gov MCP server to Claude Code:
   ```bash
   claude mcp add --name "Regulations.gov" --url "http://localhost:8000"
   ```

   d. Verify the MCP server is added:
   ```bash
   claude mcp list
   ```

5. Use the Claude Code CLI to interact with the Regulations.gov MCP server:
   ```bash
   claude code "Find recent EPA regulations about air quality"
   ```

For more details, refer to the [Claude Code documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials).

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
