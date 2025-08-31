# pokemon/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

def fetch_pokemon_data(pokemon_id_or_name):
    """Fetches data for a single Pokémon from PokeAPI."""
    url = f"{POKEAPI_BASE_URL}pokemon/{pokemon_id_or_name}/"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {pokemon_id_or_name}: {e}")
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
    pokemon_data = fetch_pokemon_data(pokemon_name_or_id.lower())

    if pokemon_data:
        context = {
            'pokemon': {
                'id': pokemon_data['id'],
                'name': pokemon_data['name'].capitalize(),
                'image_url': pokemon_data['sprites']['front_default'],
                'height': pokemon_data['height'],
                'weight': pokemon_data['weight'],
                'types': [t['type']['name'].capitalize() for t in pokemon_data['types']],
                'abilities': [a['ability']['name'].capitalize() for a in pokemon_data['abilities']],
                'stats': [{'name': s['stat']['name'].replace('-', ' ').capitalize(), 'value': s['base_stat']} for s in pokemon_data['stats']],
            },
            'title': pokemon_data['name'].capitalize()
        }
        return render(request, 'pokemon/pokemon_detail.html', context)
    else:
        return render(request, 'pokemon/pokemon_detail.html', {
            'error_message': f"Pokémon '{pokemon_name_or_id}' not found or could not be fetched.",
            'title': 'Pokémon Not Found'
        })