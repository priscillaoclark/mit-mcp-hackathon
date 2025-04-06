import sys
import os
from server import get_forecast, get_alerts

# Test the get_forecast function
print("Testing get_forecast for Boston, MA...")
forecast = get_forecast("Boston, MA", 1)
print(forecast)
print("\n" + "-"*50 + "\n")

# Test the get_alerts function
print("Testing get_alerts for Miami, FL...")
alerts = get_alerts("Miami, FL")
print(alerts)
