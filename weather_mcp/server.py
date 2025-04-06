from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Get API key from environment variables (optional, we'll use a free API if not available)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Create an MCP server
mcp = FastMCP("Weather Service")

@mcp.tool()
def get_forecast(location: str, days: int = 1) -> str:
    """
    Get the weather forecast for a location.
    
    Args:
        location: City name or location (e.g., "San Francisco, CA")
        days: Number of days for the forecast (1-3)
    
    Returns:
        A string containing the weather forecast
    """
    # Validate input
    if days < 1 or days > 3:
        return "Please provide a number of days between 1 and 3."
    
    # Use WeatherAPI.com (they have a free tier)
    url = "https://api.weatherapi.com/v1/forecast.json"
    
    params = {
        "key": WEATHER_API_KEY or "YOUR_API_KEY",  # Replace with your API key if not using env var
        "q": location,
        "days": days,
        "aqi": "no",
        "alerts": "no"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        data = response.json()
        
        # Format the response
        result = f"Weather forecast for {data['location']['name']}, {data['location']['country']}:\n\n"
        
        for day in data['forecast']['forecastday']:
            date = day['date']
            condition = day['day']['condition']['text']
            max_temp_c = day['day']['maxtemp_c']
            min_temp_c = day['day']['mintemp_c']
            max_temp_f = day['day']['maxtemp_f']
            min_temp_f = day['day']['mintemp_f']
            
            result += f"Date: {date}\n"
            result += f"Condition: {condition}\n"
            result += f"Temperature: {min_temp_c}°C to {max_temp_c}°C ({min_temp_f}°F to {max_temp_f}°F)\n\n"
        
        return result
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {str(e)}"

@mcp.tool()
def get_alerts(location: str) -> str:
    """
    Get severe weather alerts for a location.
    
    Args:
        location: City name or location (e.g., "San Francisco, CA")
    
    Returns:
        A string containing any active weather alerts
    """
    # Use WeatherAPI.com (they have a free tier)
    url = "https://api.weatherapi.com/v1/forecast.json"
    
    params = {
        "key": WEATHER_API_KEY or "YOUR_API_KEY",  # Replace with your API key if not using env var
        "q": location,
        "days": 1,
        "aqi": "no",
        "alerts": "yes"  # Include alerts
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4XX/5XX responses
        data = response.json()
        
        # Format the response
        location_name = f"{data['location']['name']}, {data['location']['country']}"
        
        if 'alerts' in data and 'alert' in data['alerts'] and data['alerts']['alert']:
            alerts = data['alerts']['alert']
            result = f"Weather alerts for {location_name}:\n\n"
            
            for alert in alerts:
                result += f"Alert: {alert.get('headline', 'Unknown alert')}\n"
                result += f"Severity: {alert.get('severity', 'Unknown')}\n"
                result += f"Time: {alert.get('effective', 'Unknown')} to {alert.get('expires', 'Unknown')}\n"
                result += f"Description: {alert.get('desc', 'No description available')}\n\n"
            
            return result
        else:
            return f"No weather alerts currently active for {location_name}."
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather alerts: {str(e)}"

# Add a resource to provide general information about the weather service
@mcp.resource("weather://info")
def get_weather_info() -> str:
    """Get information about the weather service"""
    return """
    Weather Service MCP
    
    This service provides weather forecasts and alerts using data from WeatherAPI.com.
    
    Available tools:
    - get_forecast: Get the weather forecast for a location
    - get_alerts: Get severe weather alerts for a location
    
    Example usage:
    - Ask for the weather forecast in San Francisco
    - Check for any severe weather alerts in Miami
    """

if __name__ == "__main__":
    # Run the server
    mcp.run()
