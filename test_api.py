import requests
import json

API_KEY = "36f0acf5405650a6a712cc0f9942d8d9"
BASE_URL = "https://api.themoviedb.org/3"


def get_full_show_details(show_id):
    """
    Get ALL available data for a single show
    """
    url = f"{BASE_URL}/tv/{show_id}"
    params = {
        'api_key': API_KEY,
        'append_to_response': 'credits,keywords,content_ratings,external_ids,videos'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


# Test with a popular Netflix show
# Stranger Things = show_id: 66732
# Squid Game = show_id: 93405
# Wednesday = show_id: 119051

print("=" * 80)
print("TESTING: Stranger Things (ID: 66732)")
print("=" * 80)

show_data = get_full_show_details(66732)

if show_data:
    # Pretty print the entire JSON response
    print(json.dumps(show_data, indent=2))

    print("\n" + "=" * 80)
    print("AVAILABLE PARAMETERS:")
    print("=" * 80)

    # List all top-level keys
    for key in show_data.keys():
        value = show_data[key]
        value_type = type(value).__name__

        # Show first few items if it's a list
        if isinstance(value, list):
            print(f"{key}: {value_type} (length: {len(value)})")
            if len(value) > 0:
                print(f"  Example: {value[0]}")
        # Show value if it's simple
        elif isinstance(value, (str, int, float, bool)):
            print(f"{key}: {value}")
        # Show keys if it's a dict
        elif isinstance(value, dict):
            print(f"{key}: {value_type}")
            print(f"  Keys: {list(value.keys())}")
        else:
            print(f"{key}: {value_type}")