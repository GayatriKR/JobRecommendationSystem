from neo4j import GraphDatabase

# Neo4j connection details
uri = "bolt://localhost:7687"  # The default URI for local Neo4j connections
username = "neo4j"             # Default username
password = "gayatrikr"     # Replace with your password

# Create a Neo4j driver instance
driver = GraphDatabase.driver(uri, auth=(username, password))

# Test the connection
try:
    with driver.session() as session:
        result = session.run("RETURN 'Connection Successful' AS message")
        for record in result:
            print(record["message"])  # Should print "Connection Successful"
except Exception as e:
    print("Error connecting to Neo4j:", e)

import pandas as pd

# Load the cleaned datasets
user_data = pd.read_csv('path/to/users_cleaned.csv')
job_data = pd.read_csv('path/to/job_postings_cleanedfile.csv')

# Display the first few rows to verify loading
print("User Data Sample:")
print(user_data.head())

print("\nJob Data Sample:")
print(job_data.head())
