
echo "Generating docker image"
docker build -t game .
docker tag gatekeeper therealflash/snake_game
echo "Uploading docker image"
docker push therealflash/snake_game
echo "Docker task completed successfully!"