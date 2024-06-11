from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from command import command_line


def main():
    print("ポケモン暗号化プログラム")
    # text = input("暗号化したい文字列をひらがなで入力してください: ")
    text = "おためし"

    print(text)

    command_line(text)

    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="https://beta.pokeapi.co/graphql/v1beta")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query = gql(
        """
        query samplePokeAPIquery {
            pokemon_v2_pokemonspeciesflavortext(
                where: {language_id: {_eq: 1}, pokemon_v2_version: {name: {_eq: "x"}}, flavor_text: {_like: "%あい%"}}
            ) {
                flavor_text
                pokemon_species_id
                pokemon_v2_version {
                    name
                }
            }
        }
        """
    )

    result = client.execute(query)
    print(result)


main()
