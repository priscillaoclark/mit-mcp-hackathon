from mcp.server.fastmcp import FastMCP
import requests
import os
import logging
from dotenv import load_dotenv
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("regulations_mcp")

# Load environment variables
load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv("REGULATIONS_GOV_API_KEY")

# For debugging
logger.info("Environment variables check:")
logger.info(f"- API Key available: {'Yes' if API_KEY else 'No'}")

# If no API key is available, use a placeholder for development
if not API_KEY:
    logger.warning("WARNING: REGULATIONS_GOV_API_KEY is not set. Using demo mode with limited functionality.")
    API_KEY = "DEMO_KEY"  # Use a demo key that will work for some basic endpoints

# Base URL for regulations.gov API
BASE_URL = "https://api.regulations.gov/v4"

# Create an MCP server
mcp = FastMCP("Regulations.gov Service")

def make_api_request(endpoint, method="GET", params=None, data=None):
    """Make a request to the regulations.gov API."""
    if params is None:
        params = {}
    
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "X-Api-Key": API_KEY,
        "Content-Type": "application/json"
    }
    
    logger.info(f"Making API request to: {url}")
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, params=params, json=data)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logger.error(f"API request error: {str(e)}")
        
        # Provide more helpful error messages for common issues
        if API_KEY == "DEMO_KEY" and hasattr(e, 'response') and e.response.status_code in [403, 429]:
            logger.error("Demo key has limited access. Please set a valid REGULATIONS_GOV_API_KEY environment variable.")
        
        # Return a structured error response
        error_message = str(e)
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_data = e.response.json()
                if 'errors' in error_data:
                    error_message = '; '.join([err.get('detail', str(err)) for err in error_data['errors']])
            except:
                error_message = f"HTTP {e.response.status_code}: {e.response.text}"
        
        return {"error": error_message}

@mcp.tool()
def search_documents(search_term: str = "", sort: str = "postedDate", posted_date_from: str = "", posted_date_to: str = "", document_type: str = "", docket_id: str = "", agency: str = "", limit: int = 10) -> str:
    """
    Search for documents in regulations.gov.
    
    Args:
        search_term: Keywords to search for
        sort: How to sort results (postedDate, commentDueDate, title, documentType)
        posted_date_from: Filter by posted date (YYYY-MM-DD)
        posted_date_to: Filter by posted date (YYYY-MM-DD)
        document_type: Filter by document type (e.g., 'Notice', 'Rule', 'Proposed Rule')
        docket_id: Filter by docket ID
        agency: Filter by agency ID (e.g., 'EPA', 'FDA', 'DOT')
        limit: Maximum number of results to return (1-50)
    
    Returns:
        A formatted string containing the search results
    """
    # Validate input
    if limit < 1 or limit > 50:
        return "Please provide a limit between 1 and 50."
    
    # Build parameters
    params = {
        "sort": sort,
        "page[size]": limit,
        "page[number]": 1
    }
    
    if search_term:
        params["filter[searchTerm]"] = search_term
    
    if posted_date_from:
        params["filter[postedDate][ge]"] = posted_date_from
    
    if posted_date_to:
        params["filter[postedDate][le]"] = posted_date_to
    
    if document_type:
        params["filter[documentType]"] = document_type
    
    if docket_id:
        params["filter[docketId]"] = docket_id
        
    if agency:
        params["filter[agencyId]"] = agency
    
    # Make API request
    result = make_api_request("/documents", params=params)
    
    # Handle error
    if "error" in result:
        return f"Error searching for documents: {result['error']}"
    
    # Format response
    documents = result.get("data", [])
    
    if not documents:
        return "No documents found matching your criteria."
    
    formatted_result = "Documents found:\n\n"
    
    for doc in documents:
        attributes = doc.get("attributes", {})
        formatted_result += f"Title: {attributes.get('title', 'No title')}\n"
        formatted_result += f"Document ID: {doc.get('id', 'No ID')}\n"
        formatted_result += f"Type: {attributes.get('documentType', 'Unknown type')}\n"
        formatted_result += f"Posted Date: {attributes.get('postedDate', 'Unknown date')}\n"
        
        if "commentEndDate" in attributes:
            formatted_result += f"Comment Due Date: {attributes.get('commentEndDate')}\n"
        
        formatted_result += f"Docket ID: {attributes.get('docketId', 'No docket ID')}\n"
        formatted_result += "\n"
    
    return formatted_result

@mcp.tool()
def search_comments(search_term: str = "", sort: str = "postedDate", posted_date_from: str = "", posted_date_to: str = "", docket_id: str = "", agency: str = "", limit: int = 10) -> str:
    """
    Search for comments in regulations.gov.
    
    Args:
        search_term: Keywords to search for
        sort: How to sort results (postedDate, title)
        posted_date_from: Filter by posted date (YYYY-MM-DD)
        posted_date_to: Filter by posted date (YYYY-MM-DD)
        docket_id: Filter by docket ID
        agency: Filter by agency ID (e.g., 'EPA', 'FDA', 'DOT')
        limit: Maximum number of results to return (1-50)
    
    Returns:
        A formatted string containing the search results
    """
    # Validate input
    if limit < 1 or limit > 50:
        return "Please provide a limit between 1 and 50."
    
    # Build parameters
    params = {
        "sort": sort,
        "page[size]": limit,
        "page[number]": 1
    }
    
    if search_term:
        params["filter[searchTerm]"] = search_term
    
    if posted_date_from:
        params["filter[postedDate][ge]"] = posted_date_from
    
    if posted_date_to:
        params["filter[postedDate][le]"] = posted_date_to
    
    if docket_id:
        params["filter[docketId]"] = docket_id
        
    if agency:
        params["filter[agencyId]"] = agency
    
    # Make API request
    result = make_api_request("/comments", params=params)
    
    # Handle error
    if "error" in result:
        return f"Error searching for comments: {result['error']}"
    
    # Format response
    comments = result.get("data", [])
    
    if not comments:
        return "No comments found matching your criteria."
    
    formatted_result = "Comments found:\n\n"
    
    for comment in comments:
        attributes = comment.get("attributes", {})
        formatted_result += f"Title: {attributes.get('title', 'No title')}\n"
        formatted_result += f"Comment ID: {comment.get('id', 'No ID')}\n"
        formatted_result += f"Posted Date: {attributes.get('postedDate', 'Unknown date')}\n"
        formatted_result += f"Docket ID: {attributes.get('docketId', 'No docket ID')}\n"
        
        if "comment" in attributes:
            comment_text = attributes.get("comment", "").strip()
            if len(comment_text) > 200:
                comment_text = comment_text[:200] + "..."
            formatted_result += f"Comment: {comment_text}\n"
        
        formatted_result += "\n"
    
    return formatted_result

@mcp.tool()
def search_dockets(search_term: str = "", sort: str = "title", agency: str = "", limit: int = 10) -> str:
    """
    Search for dockets in regulations.gov.
    
    Args:
        search_term: Keywords to search for
        sort: How to sort results (title, lastModifiedDate)
        agency: Filter by agency ID (e.g., 'EPA', 'FDA', 'DOT')
        limit: Maximum number of results to return (1-50)
    
    Returns:
        A formatted string containing the search results
    """
    # Validate input
    if limit < 1 or limit > 50:
        return "Please provide a limit between 1 and 50."
    
    # Build parameters
    params = {
        "sort": sort,
        "page[size]": limit,
        "page[number]": 1
    }
    
    if search_term:
        params["filter[searchTerm]"] = search_term
    
    if agency:
        params["filter[agencyId]"] = agency
    
    # Make API request
    result = make_api_request("/dockets", params=params)
    
    # Handle error
    if "error" in result:
        return f"Error searching for dockets: {result['error']}"
    
    # Format response
    dockets = result.get("data", [])
    
    if not dockets:
        return "No dockets found matching your criteria."
    
    formatted_result = "Dockets found:\n\n"
    
    for docket in dockets:
        attributes = docket.get("attributes", {})
        formatted_result += f"Title: {attributes.get('title', 'No title')}\n"
        formatted_result += f"Docket ID: {docket.get('id', 'No ID')}\n"
        formatted_result += f"Agency: {attributes.get('agencyId', 'Unknown agency')}\n"
        
        if "modifyDate" in attributes:
            formatted_result += f"Last Modified: {attributes.get('modifyDate')}\n"
        
        formatted_result += "\n"
    
    return formatted_result

@mcp.tool()
def get_document_details(document_id: str) -> str:
    """
    Get detailed information about a specific document.
    
    Args:
        document_id: The document ID
    
    Returns:
        A formatted string containing the document details
    """
    # Make API request
    result = make_api_request(f"/documents/{document_id}")
    
    # Handle error
    if "error" in result:
        return f"Error retrieving document details: {result['error']}"
    
    # Format response
    document = result.get("data", {})
    
    if not document:
        return f"No document found with ID: {document_id}"
    
    attributes = document.get("attributes", {})
    
    formatted_result = "Document Details:\n\n"
    formatted_result += f"Title: {attributes.get('title', 'No title')}\n"
    formatted_result += f"Document ID: {document.get('id', 'No ID')}\n"
    formatted_result += f"Type: {attributes.get('documentType', 'Unknown type')}\n"
    formatted_result += f"Posted Date: {attributes.get('postedDate', 'Unknown date')}\n"
    
    if "commentEndDate" in attributes:
        formatted_result += f"Comment Due Date: {attributes.get('commentEndDate')}\n"
    
    formatted_result += f"Docket ID: {attributes.get('docketId', 'No docket ID')}\n"
    
    if "agencyId" in attributes:
        formatted_result += f"Agency: {attributes.get('agencyId')}\n"
    
    if "summary" in attributes and attributes["summary"]:
        summary = attributes["summary"]
        if len(summary) > 500:
            summary = summary[:500] + "..."
        formatted_result += f"\nSummary: {summary}\n"
    
    return formatted_result

@mcp.tool()
def get_comment_details(comment_id: str) -> str:
    """
    Get detailed information about a specific comment.
    
    Args:
        comment_id: The comment ID
    
    Returns:
        A formatted string containing the comment details
    """
    # Make API request
    result = make_api_request(f"/comments/{comment_id}")
    
    # Handle error
    if "error" in result:
        return f"Error retrieving comment details: {result['error']}"
    
    # Format response
    comment = result.get("data", {})
    
    if not comment:
        return f"No comment found with ID: {comment_id}"
    
    attributes = comment.get("attributes", {})
    
    formatted_result = "Comment Details:\n\n"
    formatted_result += f"Title: {attributes.get('title', 'No title')}\n"
    formatted_result += f"Comment ID: {comment.get('id', 'No ID')}\n"
    formatted_result += f"Posted Date: {attributes.get('postedDate', 'Unknown date')}\n"
    formatted_result += f"Docket ID: {attributes.get('docketId', 'No docket ID')}\n"
    
    if "comment" in attributes:
        formatted_result += f"\nComment Text:\n{attributes.get('comment', 'No comment text')}\n"
    
    return formatted_result

@mcp.tool()
def get_docket_details(docket_id: str) -> str:
    """
    Get detailed information about a specific docket.
    
    Args:
        docket_id: The docket ID
    
    Returns:
        A formatted string containing the docket details
    """
    # Make API request
    result = make_api_request(f"/dockets/{docket_id}")
    
    # Handle error
    if "error" in result:
        return f"Error retrieving docket details: {result['error']}"
    
    # Format response
    docket = result.get("data", {})
    
    if not docket:
        return f"No docket found with ID: {docket_id}"
    
    attributes = docket.get("attributes", {})
    
    formatted_result = "Docket Details:\n\n"
    formatted_result += f"Title: {attributes.get('title', 'No title')}\n"
    formatted_result += f"Docket ID: {docket.get('id', 'No ID')}\n"
    formatted_result += f"Agency: {attributes.get('agencyId', 'Unknown agency')}\n"
    
    if "modifyDate" in attributes:
        formatted_result += f"Last Modified: {attributes.get('modifyDate')}\n"
    
    # Get additional information about documents in this docket
    doc_params = {
        "filter[docketId]": docket_id,
        "page[size]": 5,
        "page[number]": 1
    }
    
    doc_result = make_api_request("/documents", params=doc_params)
    
    if "error" not in doc_result:
        documents = doc_result.get("data", [])
        
        if documents:
            formatted_result += f"\nRecent Documents in this Docket ({len(documents)}):\n"
            
            for doc in documents:
                doc_attrs = doc.get("attributes", {})
                formatted_result += f"- {doc_attrs.get('title', 'No title')} ({doc.get('id', 'No ID')})\n"
    
    return formatted_result

# Add a resource to provide general information about the regulations.gov service
@mcp.resource("regulations://info")
def get_regulations_info() -> str:
    """Get information about the regulations.gov service"""
    return """
    Regulations.gov MCP Service
    
    This service provides access to the regulations.gov API, allowing you to search for and retrieve information about:
    - Documents: Proposed rules, final rules, notices, and other regulatory documents
    - Comments: Public comments submitted in response to regulatory documents
    - Dockets: Collections of documents, comments, and other materials related to a regulatory action
    
    Available tools:
    - search_documents: Search for regulatory documents
    - search_comments: Search for public comments
    - search_dockets: Search for regulatory dockets
    - get_document_details: Get detailed information about a specific document
    - get_comment_details: Get detailed information about a specific comment
    - get_docket_details: Get detailed information about a specific docket
    
    Example usage:
    - Search for recent EPA documents
    - Find comments about a specific regulation
    - Get details about a docket of interest
    """

if __name__ == "__main__":
    # Run the server
    mcp.run()
