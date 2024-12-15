# dockerコマンドメモ
カレントディレクトリ：202412_github_action_demoで実行前提

$ docker compose -f ./batch/docker/test_docker-compose.yml build
$ docker compose -f ./batch/docker/test_docker-compose.yml up -d
$ docker ps -a
$ docker exec -it python_batch_a /bin/bash
:/batch# python -m pytest

$ docker compose -f ./batch/docker/test_docker-compose.yml down
$ docker rmi $(docker images -q)


