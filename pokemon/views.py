# pokemon/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

def fetch_pokemon_data(pokemon_id_or_name):
    """Fetches data for a single Pokémon from PokeAPI."""
    url = f"{POKEAPI_BASE_URL}pokemon/{pokemon_id_or_name}/"
    print(f"Making request to: {url}")
    try:
        response = requests.get(url, timeout=10)  # Add timeout
        print(f"Response status: {response.status_code}")
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        print(f"Successfully fetched data for {pokemon_id_or_name}")
        return data
    except requests.exceptions.Timeout:
        print(f"Timeout fetching data for {pokemon_id_or_name}")
        return None
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Pokémon '{pokemon_id_or_name}' not found")
        else:
            print(f"HTTP error fetching data for {pokemon_id_or_name}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {pokemon_id_or_name}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error fetching data for {pokemon_id_or_name}: {e}")
        return None

def pokemon_list(request):
    """Displays a list of Pokémon."""
    all_pokemon_data = []
    limit = 151
    offset = 0
    list_url = f"{POKEAPI_BASE_URL}pokemon/?limit={limit}&offset={offset}"

    try:
        response = requests.get(list_url)
        response.raise_for_status()
        data = response.json()
        results = data.get('results', [])

        for p in results:
            # Fetch full details for each Pokémon for image/other data
            detail_data = fetch_pokemon_data(p['name'])
            if detail_data:
                all_pokemon_data.append({
                    'name': detail_data['name'].capitalize(),
                    'id': detail_data['id'],
                    'image_url': detail_data['sprites']['front_default']
                })
        all_pokemon_data.sort(key=lambda x: x['id']) # Sort by ID

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Pokémon list: {e}")
        all_pokemon_data = [] # Ensure it's an empty list on error

    context = {
        'pokemons': all_pokemon_data,
        'title': 'PokéDex List'
    }
    return render(request, 'pokemon/pokemon_list.html', context)


def pokemon_detail(request, pokemon_name_or_id):
    """Displays details for a single Pokémon."""
    print(f"Attempting to fetch data for: {pokemon_name_or_id}")
    pokemon_data = fetch_pokemon_data(pokemon_name_or_id.lower())

    if pokemon_data:
        try:
            print(f"Processing data for {pokemon_name_or_id}")
            print(f"Pokemon data keys: {list(pokemon_data.keys())}")
            
            # Check if required fields exist
            if 'sprites' not in pokemon_data:
                print("Missing sprites in pokemon data")
                raise KeyError("sprites")
            
            if 'front_default' not in pokemon_data['sprites']:
                print("Missing front_default in sprites")
                raise KeyError("front_default")
            
            # Convert height from decimeters to centimeters
            height_cm = pokemon_data['height'] * 10
            # Convert weight from hectograms to kilograms
            weight_kg = pokemon_data['weight'] / 10
            
            context = {
                'pokemon': {
                    'id': pokemon_data['id'],
                    'name': pokemon_data['name'].capitalize(),
                    'image_url': pokemon_data['sprites']['front_default'],
                    'height': height_cm,
                    'weight': weight_kg,
                    'types': [t['type']['name'].capitalize() for t in pokemon_data['types']],
                    'abilities': [a['ability']['name'].capitalize() for a in pokemon_data['abilities']],
                    'stats': [{'name': s['stat']['name'].replace('-', ' ').capitalize(), 'value': s['base_stat']} for s in pokemon_data['stats']],
                },
                'title': pokemon_data['name'].capitalize()
            }
            print("Context created successfully")
            return render(request, 'pokemon/pokemon_detail.html', context)
        except KeyError as e:
            print(f"KeyError in pokemon data: {e}")
            return render(request, 'pokemon/pokemon_detail.html', {
                'error_message': f"Error processing Pokémon data for '{pokemon_name_or_id}': {e}",
                'title': 'Error'
            })
        except Exception as e:
            print(f"Unexpected error processing pokemon data: {e}")
            import traceback
            traceback.print_exc()
            return render(request, 'pokemon/pokemon_detail.html', {
                'error_message': f"Unexpected error processing Pokémon data for '{pokemon_name_or_id}': {e}",
                'title': 'Error'
            })
    else:
        return render(request, 'pokemon/pokemon_detail.html', {
            'error_message': f"Pokémon '{pokemon_name_or_id}' not found or could not be fetched.",
            'title': 'Pokémon Not Found'
        })