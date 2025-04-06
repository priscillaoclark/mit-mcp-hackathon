# Regulations.gov MCP Server for Claude Desktop

This project provides a Model Control Protocol (MCP) server that allows Claude Desktop to interact with the regulations.gov API (v4). The server acts as a bridge between Claude and the regulations.gov API, enabling Claude to search for documents, comments, and dockets, as well as post comments.

## Features

- Search for documents on regulations.gov
- Get detailed information about specific documents
- Search for comments
- Get detailed information about specific comments
- Search for dockets
- Get detailed information about specific dockets
- Post comments to regulations.gov
- Get submission keys for posting comments
- Get file upload URLs for attaching files to comments

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- regulations.gov API key

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   npm install
   ```
3. Create a `.env` file in the root directory with your regulations.gov API key:
   ```
   REGULATIONS_GOV_API_KEY=your_api_key_here
   PORT=3000 # Optional, defaults to 3000
   ```

## Usage

1. Start the server:
   ```
   npm start
   ```
2. The server will be available at `http://localhost:3000`
3. The MCP manifest will be available at `http://localhost:3000/manifest`
4. The OpenAPI specification will be available at `http://localhost:3000/openapi.json`

## Connecting to Claude Desktop

1. Open Claude Desktop
2. Go to Settings > Tools
3. Click "Add Tool"
4. Enter the manifest URL: `http://localhost:3000/manifest`
5. Click "Add Tool"

Claude should now be able to use the regulations.gov API through this MCP server.

## API Endpoints

- `GET /documents` - Search for documents
- `GET /documents/{documentId}` - Get document by ID
- `GET /comments` - Search for comments
- `GET /comments/{commentId}` - Get comment by ID
- `GET /dockets` - Search for dockets
- `GET /dockets/{docketId}` - Get docket by ID
- `POST /comments` - Post a comment
- `GET /submission-keys` - Get a submission key for posting comments
- `POST /file-upload-urls` - Get URLs for uploading files

## Development

For development with automatic restarts when files change:

```
npm run dev
```
