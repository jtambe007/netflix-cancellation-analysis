import requests
import pandas as pd
import time
from datetime import datetime

API_KEY = "36f0acf5405650a6a712cc0f9942d8d9"
BASE_URL = "https://api.themoviedb.org/3"


def get_netflix_shows(num_pages=20):
    """
    This function:
    - Loops through 20 pages of Netflix shows
    - Each page has ~20 shows = ~400 total shows
    - Adds a delay to respect rate limits
    - Saves basic info for each show
    """
    shows = []

    for page in range(1, num_pages + 1):
        url = f"{BASE_URL}/discover/tv"
        params = {
            'api_key': API_KEY,
            'with_networks': 213,  # Netflix
            'page': page,
            'sort_by': 'popularity.desc'
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Error on page {page}: {response.status_code}")
            continue

        data = response.json()

        for show in data['results']:
            shows.append({
                'id': show['id'],
                'name': show['name'],
                'first_air_date': show.get('first_air_date'),
                'popularity': show['popularity'],
                'vote_average': show['vote_average'],
                'vote_count': show['vote_count']
            })

        time.sleep(0.25)
        print(f"✓ Fetched page {page}/{num_pages}")

    return pd.DataFrame(shows)


def get_detailed_show_info(show_id):
    """Get ALL useful details for a show"""
    url = f"{BASE_URL}/tv/{show_id}"
    params = {
        'api_key': API_KEY,
        'append_to_response': 'keywords,content_ratings,external_ids'
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    # Extract genres as comma-separated string
    genres = ', '.join([g['name'] for g in data.get('genres', [])])

    # Extract top 5 keywords
    keywords_list = data.get('keywords', {}).get('results', [])
    keywords = ', '.join([k['name'] for k in keywords_list[:5]])

    # Get average episode runtime
    runtime_list = data.get('episode_run_time', [])
    avg_runtime = sum(runtime_list) / len(runtime_list) if runtime_list else None

    # Calculate show age in days
    first_air = data.get('first_air_date')
    last_air = data.get('last_air_date')
    show_age_days = None
    days_since_last_episode = None

    if first_air:
        try:
            first_date = datetime.strptime(first_air, '%Y-%m-%d')
            show_age_days = (datetime.now() - first_date).days
        except:
            pass

    if last_air:
        try:
            last_date = datetime.strptime(last_air, '%Y-%m-%d')
            days_since_last_episode = (datetime.now() - last_date).days
        except:
            pass

    # Get US content rating
    us_rating = None
    for rating in data.get('content_ratings', {}).get('results', []):
        if rating.get('iso_3166_1') == 'US':
            us_rating = rating.get('rating')
            break

    # Get IMDB ID
    imdb_id = data.get('external_ids', {}).get('imdb_id')

    # Get creator names
    creators = ', '.join([c['name'] for c in data.get('created_by', [])])

    return {
        'status': data.get('status'),
        'in_production': data.get('in_production'),
        'num_seasons': data.get('number_of_seasons'),
        'num_episodes': data.get('number_of_episodes'),
        'genres': genres,
        'type': data.get('type'),
        'original_language': data.get('original_language'),
        'origin_country': ', '.join(data.get('origin_country', [])),
        'avg_episode_runtime': avg_runtime,
        'show_age_days': show_age_days,
        'days_since_last_episode': days_since_last_episode,
        'keywords': keywords,
        'last_air_date': last_air,
        'us_content_rating': us_rating,
        'imdb_id': imdb_id,
        'created_by': creators,
        'homepage': data.get('homepage'),
    }


# Main execution
if __name__ == "__main__":
    print("=" * 80)
    print("NETFLIX SHOW CANCELLATION ANALYSIS - DATA COLLECTION")
    print("=" * 80)

    # Step 1: Get basic show list
    print("\n[STEP 1/3] Fetching Netflix show IDs...")
    df_shows = get_netflix_shows(num_pages=25)  # ~500 shows
    print(f"✅ Found {len(df_shows)} shows")

    # Step 2: Get detailed info for each
    print("\n[STEP 2/3] Fetching detailed information...")
    print("This will take ~5 minutes with rate limiting...")

    details = []
    failed = 0

    for idx, show_id in enumerate(df_shows['id']):
        detail = get_detailed_show_info(show_id)

        if detail:
            details.append(detail)
        else:
            failed += 1

        time.sleep(0.25)  # Rate limiting (4 requests/second max)

        # Progress indicator every 50 shows
        if (idx + 1) % 50 == 0:
            print(f"  Progress: {idx + 1}/{len(df_shows)} shows processed...")

    print(f"✅ Collected details for {len(details)} shows ({failed} failed)")

    # Step 3: Combine and save
    print("\n[STEP 3/3] Combining and saving data...")
    df_details = pd.DataFrame(details)
    df_final = pd.concat([df_shows.reset_index(drop=True), df_details], axis=1)

    # Save to CSV
    filename = 'data/netflix_shows_complete.csv'
    df_final.to_csv(filename, index=False)

    print(f"✅ Data saved to '{filename}'")

    # Summary statistics
    print("\n" + "=" * 80)
    print("📊 DATASET SUMMARY")
    print("=" * 80)
    print(f"\nTotal shows collected: {len(df_final)}")
    print(f"\nStatus breakdown:")
    print(df_final['status'].value_counts())

    print(f"\n📈 Rating statistics:")
    print(f"  Average rating: {df_final['vote_average'].mean():.2f}")
    print(f"  Median rating: {df_final['vote_average'].median():.2f}")

    print(f"\n📺 Season statistics:")
    print(f"  Average seasons: {df_final['num_seasons'].mean():.2f}")
    print(f"  Max seasons: {df_final['num_seasons'].max()}")

    print(f"\n🎭 Genre breakdown (top 5):")
    all_genres = []
    for genres in df_final['genres'].dropna():
        all_genres.extend([g.strip() for g in genres.split(',')])
    genre_counts = pd.Series(all_genres).value_counts().head(5)
    for genre, count in genre_counts.items():
        print(f"  {genre}: {count}")

    # Show sample
    print(f"\n📋 Sample of collected data:")
    print(df_final[['name', 'status', 'vote_average', 'num_seasons', 'genres']].head(10))

    print("\n" + "=" * 80)
    print("✅ DATA COLLECTION COMPLETE!")
    print("=" * 80)