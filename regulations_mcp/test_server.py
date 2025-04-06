import sys
import os
from server import search_documents, search_comments, search_dockets, get_document_details, list_agencies

# Test the search_documents function
print("Testing search_documents for EPA documents from 2024...")
documents = search_documents(agency="EPA", posted_date_from="2024-01-01", limit=5)
print(documents)
print("\n" + "-"*50 + "\n")

# Test the search_comments function
print("Testing search_comments for FDA comments from 2024...")
comments = search_comments(agency="FDA", posted_date_from="2024-01-01", limit=5)
print(comments)
print("\n" + "-"*50 + "\n")

# Test the search_dockets function
print("Testing search_dockets for EPA dockets...")
dockets = search_dockets(agency="EPA", limit=5)
print(dockets)
print("\n" + "-"*50 + "\n")

# Test the list_agencies function
print("Testing list_agencies...")
agencies = list_agencies()
print(agencies)
print("\n" + "-"*50 + "\n")

# Test get_document_details with a document ID from the search results
# Uncomment and replace with an actual document ID after running the first test
# print("Testing get_document_details...")
# document_id = "EPA-HQ-OAR-2004-0233-0122"  # Replace with an actual document ID
# document_details = get_document_details(document_id)
# print(document_details)
