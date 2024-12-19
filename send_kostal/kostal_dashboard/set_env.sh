## Usage: source set_env.sh

if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi