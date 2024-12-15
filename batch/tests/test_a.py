import sys
import os
import pytest
from unittest.mock import MagicMock

import psycopg2

# monkeypatchの後にインポートが必要
# from main.batchA.app import main

##### 前処理 #####

@pytest.fixture
def mock_db_env():
    reset_db()
    yield


##### テストケース #####
def test_dbpudate_1(monkeypatch):
    # 期待結果
    expected = [
        (11, 'ムラ', 'サキ'),
        (12, 'メレ', 'ブ')
    ]
    
    # テスト
    # 同一関数の中で、この順番でないと上書きできない。。
    monkeypatch.setenv("DB_HOST", "test_db_cntr")
    monkeypatch.setenv("DB_PORT", "5432")
    monkeypatch.setenv("DB_NAME", "sample_db")
    monkeypatch.setenv("DB_USER", "postgres")
    monkeypatch.setenv("DB_PASSWORD", "postgres")
    from main.batchA.app import main
    main()
    result = select_db()
    assert result == expected

def test_dbpudate_2(monkeypatch):
    # 期待結果
    expected = [
        (22, 'のび', 'のび太'),
        (23, 'すね', '男')
    ]
    
    # テスト
    # 同一関数の中で、この順番でないと上書きできない。。
    monkeypatch.setenv("DB_HOST", "test_db_cntr")
    monkeypatch.setenv("DB_PORT", "5432")
    monkeypatch.setenv("DB_NAME", "sample_db")
    monkeypatch.setenv("DB_USER", "postgres")
    monkeypatch.setenv("DB_PASSWORD", "postgres")
    from main.batchA import app

    replase_data = [
        (22, 'のび', 'のび太'),
        (23, 'すね', '男')
    ]
    monkeypatch.setattr(app, 'get_data', MagicMock(return_value=replase_data))
    app.main()
    result = select_db()
    assert result == expected



##### 共通関数 ######
def select_db():
    # 環境変数から接続情報を取得
    host = "test_db_cntr"         # データベースのホスト名
    port = "5432"              # データベースのポート（デフォルト: 5432）
    database = "sample_db" # データベース名
    user = "postgres"         # データベースユーザー名
    password = "postgres" # データベースユーザーパスワード

    # PostgreSQLに接続してデータを取得
    data = []
    try:
        # データベース接続
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        # カーソル作成
        cursor = connection.cursor()
        # 全件表示
        query = "SELECT * FROM sample;"
        cursor.execute(query)
        data = cursor.fetchall()
        # コミット
        connection.commit()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return data
    
def reset_db():
    # 環境変数から接続情報を取得
    host = "test_db_cntr"         # データベースのホスト名
    port = "5432"              # データベースのポート（デフォルト: 5432）
    database = "sample_db" # データベース名
    user = "postgres"         # データベースユーザー名
    password = "postgres" # データベースユーザーパスワード

    # PostgreSQLに接続してデータを取得
    data = []
    try:
        # データベース接続
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        # カーソル作成
        cursor = connection.cursor()

        # データクリア
        query_delete = 'DELETE FROM sample;'
        cursor.execute(query_delete)

        # 初期データインサート
        query_insert = '''INSERT INTO sample (id, first_name, last_name) VALUES 
        (1, '初期', '太郎'),
        (2, '初期', '次郎'),
        (3, '初期', 'マイケル');
        '''
        cursor.execute(query_insert)

         # 全件表示
        query = "SELECT * FROM sample;"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        # コミット
        connection.commit()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

