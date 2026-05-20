import requests
import random


class CountriesError(Exception):
    """Base exception for the countries module."""


def get_random_countries(n: int = 10) -> list[str]:
    """Fetch n unique random country names from the REST Countries API."""
    try:
        response = requests.get('https://restcountries.com/v3.1/all', params={'fields': 'name'})
        response.raise_for_status()
    except requests.RequestException as error:
        raise CountriesError(f"API request failed: {error}")

    try:
        data = response.json()
    except requests.JSONDecodeError as error:
        raise CountriesError(f"Failed to parse API response as JSON: {error}")

    try:
        names = [c['name']['common'] for c in data]
    except KeyError as error:
        raise CountriesError(f"Unexpected API response structure, missing key: {error}")

    return random.sample(names, n)
