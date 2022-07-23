import requests

from pytest_bdd import scenarios, given, then, parsers

# Shared Variables
DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

# Scenarios
scenarios('../features/service.feature')

# Steps
@given(parsers.parse('the DuckDuckGo API is queries with {phrase}'), target_fixture='query_phrase')
def query_phrase(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response

@then(parsers.parse('the response status code is "{status_code}"'), converters={"status_code": int})
def query_reponse_status(query_phrase, status_code):
    assert query_phrase.status_code == status_code

@then(parsers.parse('the response contains results for {phrase}'))
def query_response_content(query_phrase, phrase):
    assert phrase.lower() == query_phrase.json()['Heading'].lower()
