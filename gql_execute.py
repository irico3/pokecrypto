from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


def gql_execute(search_str: str):
    transport = AIOHTTPTransport(url="https://beta.pokeapi.co/graphql/v1beta")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query = gql(
        f"""
        query samplePokeAPIquery {{
            pokemon_v2_pokemonspeciesflavortext(
                where: {{language_id: {{_eq: 1}}, pokemon_v2_version: {{name: {{_eq: "x"}}}}, flavor_text: {{_like: "%{search_str}%"}}}}
            ) {{
                flavor_text
                pokemon_species_id
                pokemon_v2_version {{
                    name
                }}
            }}
        }}
        """
    )
    result = client.execute(query)
    return result["pokemon_v2_pokemonspeciesflavortext"]
