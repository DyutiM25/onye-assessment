import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def parse_query(text):
    doc = nlp(text.lower())

    # Initialize placeholders
    condition = None
    age = None
    age_sign = None

    # Extract medical condition from keywords
    for token in doc:
        if "diabet" in token.text:
            condition = "diabetes"
            break
        elif "asthma" in token.text:
            condition = "asthma"
            break
        elif "hypertens" in token.text:
            condition = "hypertension"
            break
        elif "cancer" in token.text:
            condition = "cancer"
            break
        elif "obes" in token.text:
            condition = "obesity"
            break
        elif "flu" in token.text:
            condition = "flu"
            break
        elif "covid" in token.text:
            condition = "covid"
            break

    # Extract age and comparison
    for i, token in enumerate(doc):
        if token.like_num:
            age = token.text
            if i > 0:
                prev_token = doc[i - 1]
                if prev_token.text in ["over", "above", "older", "greater"]:
                    age_sign = ">"
                elif prev_token.text in ["under", "below", "younger", "less"]:
                    age_sign = "<"

    return {
        "resourceType": "Patient",
        "query": {
            "condition": condition,
            "age": f"{age_sign or '='}{age}" if age else None
        }
    }

# Test with example inputs
if __name__ == "__main__":
    queries = [
        "Show me all diabetic patients over 50",
        "List asthma patients under 18",
        "Find patients with hypertension aged above 60",
        "Show cancer patients older than 70",
        "Get patients who are over 30 and have obesity"
    ]

    for q in queries:
        print(f"\nInput: {q}")
        print("Output:", parse_query(q))
