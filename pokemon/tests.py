from django.test import TestCase, Client
from django.urls import reverse
import requests
from unittest.mock import patch, Mock

# Create your tests here.

class PokemonViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_pokemon_list_view(self):
        """Test that pokemon list view loads correctly"""
        response = self.client.get(reverse('pokemon:pokemon_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pokemon/pokemon_list.html')
        
    def test_pokemon_detail_view_with_valid_id(self):
        """Test pokemon detail view with valid ID"""
        # Mock the PokeAPI response
        mock_response = Mock()
        mock_response.json.return_value = {
            'id': 25,
            'name': 'pikachu',
            'sprites': {'front_default': 'https://example.com/pikachu.png'},
            'height': 4,
            'weight': 60,
            'types': [{'type': {'name': 'electric'}}],
            'abilities': [{'ability': {'name': 'static'}}],
            'stats': [{'stat': {'name': 'hp'}, 'base_stat': 35}]
        }
        mock_response.raise_for_status.return_value = None
        
        with patch('requests.get', return_value=mock_response):
            response = self.client.get(reverse('pokemon:pokemon_detail', args=['25']))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'pokemon/pokemon_detail.html')
            
    def test_pokemon_detail_view_with_invalid_id(self):
        """Test pokemon detail view with invalid ID"""
        # Mock the PokeAPI response to raise an exception
        with patch('requests.get', side_effect=requests.exceptions.RequestException):
            response = self.client.get(reverse('pokemon:pokemon_detail', args=['99999']))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'pokemon/pokemon_detail.html')
            self.assertIn('error_message', response.context)
            
    def test_pokemon_detail_view_with_name(self):
        """Test pokemon detail view with name instead of ID"""
        mock_response = Mock()
        mock_response.json.return_value = {
            'id': 25,
            'name': 'pikachu',
            'sprites': {'front_default': 'https://example.com/pikachu.png'},
            'height': 4,
            'weight': 60,
            'types': [{'type': {'name': 'electric'}}],
            'abilities': [{'ability': {'name': 'static'}}],
            'stats': [{'stat': {'name': 'hp'}, 'base_stat': 35}]
        }
        mock_response.raise_for_status.return_value = None
        
        with patch('requests.get', return_value=mock_response):
            response = self.client.get(reverse('pokemon:pokemon_detail', args=['pikachu']))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'pokemon/pokemon_detail.html')
