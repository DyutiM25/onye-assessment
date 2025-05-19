from flask import Flask, request, jsonify
from flask_cors import CORS
from fhir_query_parser import parse_query
import re

app = Flask(__name__)
CORS(app)

@app.route("/parse", methods=["POST"])
def parse():
    data = request.get_json()
    query_text = data.get("query", "")

    result = parse_query(query_text)

    # Get condition and age filter
    condition = result['query'].get('condition') or "unknown"
    age_string = result['query'].get('age')

    age_filter = None
    age_operator = None

    # ✅ Handle age ranges (e.g., "40-60")
    if isinstance(age_string, str) and "-" in age_string:
        parts = age_string.split("-")
        try:
            age_filter = (int(parts[0]), int(parts[1]))  # Tuple: (min, max)
            age_operator = "range"
        except:
            age_filter = None

    # ✅ Handle >, <, >=, <=, =
    elif isinstance(age_string, str):
        match = re.match(r"(>=|<=|>|<|=)?\s*(\d+)", age_string.strip())
        if match:
            age_operator = match.group(1) or "="
            age_filter = int(match.group(2))

    # ✅ Define all test patients (6 conditions)
    patients = [
        # Diabetes
        {"name": "John Doe", "age": 55, "condition": "diabetes"},
        {"name": "Jane Smith", "age": 60, "condition": "diabetes"},
        {"name": "Alice Johnson", "age": 67, "condition": "diabetes"},
        {"name": "Bob Williams", "age": 72, "condition": "diabetes"},

        # Hypertension
        {"name": "Chris Green", "age": 45, "condition": "hypertension"},
        {"name": "Mia King", "age": 52, "condition": "hypertension"},
        {"name": "Ethan Wright", "age": 65, "condition": "hypertension"},

        # Asthma
        {"name": "Lily Turner", "age": 30, "condition": "asthma"},
        {"name": "Noah Scott", "age": 40, "condition": "asthma"},
        {"name": "Sophia Clark", "age": 38, "condition": "asthma"},

        # Cancer
        {"name": "Olivia Adams", "age": 70, "condition": "cancer"},
        {"name": "Lucas Baker", "age": 68, "condition": "cancer"},
        {"name": "Amelia Hughes", "age": 75, "condition": "cancer"},

        # Covid
        {"name": "Henry Foster", "age": 50, "condition": "covid"},
        {"name": "Chloe Stewart", "age": 45, "condition": "covid"},
        {"name": "Mason Phillips", "age": 63, "condition": "covid"},

        # Flu
        {"name": "Ella Simmons", "age": 35, "condition": "flu"},
        {"name": "Logan Parker", "age": 29, "condition": "flu"},
        {"name": "Zoe Rivera", "age": 41, "condition": "flu"}
    ]

    # ✅ Helper function for age filtering
    def age_matches(age):
        if age_filter is None:
            return True
        if age_operator == "range" and isinstance(age_filter, tuple):
            return age_filter[0] <= age <= age_filter[1]
        if age_operator == ">":
            return age > age_filter
        elif age_operator == "<":
            return age < age_filter
        elif age_operator == ">=":
            return age >= age_filter
        elif age_operator == "<=":
            return age <= age_filter
        elif age_operator == "=":
            return age == age_filter
        return False

    # ✅ Final filter (safe `.lower()` checks)
    filtered_patients = [
        p for p in patients
        if p.get("condition", "").lower() == condition.lower()
        and age_matches(p["age"])
    ]

    return jsonify({"patients": filtered_patients})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
