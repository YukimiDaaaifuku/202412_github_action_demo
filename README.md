# dockerコマンドメモ
カレントディレクトリ：202412_github_action_demoで実行前提

$ docker compose -f ./batch/docker/test_docker-compose.yml build
$ docker compose -f ./batch/docker/test_docker-compose.yml up -d
$ docker ps -a
$ docker exec -it python_batch_a /bin/bash
:/batch# python -m pytest

$ docker compose -f ./batch/docker/test_docker-compose.yml down
$ docker rmi $(docker images -q)


# ローカルテスト時との差分
### なし ###
batch/docker/test_docker-compose.yml
    build/volumes:　をコメントアウト #　マウントしないため

batch/docker/test_batch_Dockerfile
COPY ./test_batch_requirements.txt /batch/docker
 ↓
COPY ../../batch /batch




docker exec -it python_batch_a /bin/bash -c "python -m pytest"
docker-compose exec -T python_batch_a /bin/bash -c "python -m pytest"


