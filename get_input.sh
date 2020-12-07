
# based on redit thread https://www.reddit.com/r/adventofcode/comments/a2vonl/how_to_download_inputs_with_a_script/

echo 'Fetching data inout for' $1 'and' $2

curl 'https://adventofcode.com/'$1'/day/'$2'/input' --cookie "session=53616c7465645f5f93613545e6da701e406606d7114a3fab67d00b64eca7434666114ecaaee991f30f0b1c96b8111019"
