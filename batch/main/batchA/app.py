import os
import psycopg2
from psycopg2 import extras
from main.common import message

def main():
    # 更新用データ取得
    data = get_data()

    # データベース更新
    update_sampledb(data)


def get_data():
    data = [
        (11, 'ムラ', 'サキ'),
        (12, 'メレ', 'ブ')
    ]
    return data


def update_sampledb(data):
    # 接続情報を設定
    """
    host = "test_db_cntr"         # データベースのホスト名
    port = "5432"              # データベースのポート（デフォルト: 5432）
    database = "sample_db" # データベース名
    user = "postgres"         # データベースユーザー名
    password = "postgres" # データベースユーザーパスワード
    """
    # 環境変数から接続情報を取得
    host = os.getenv("DB_HOST", "localhost")         # デフォルト値を "localhost" に設定
    port = os.getenv("DB_PORT", "1234")             # デフォルト値を "5432" に設定
    database = os.getenv("DB_NAME", "your_database") # デフォルト値を "your_database" に設定
    user = os.getenv("DB_USER", "your_user")         # デフォルト値を "your_user" に設定
    password = os.getenv("DB_PASSWORD", "your_password") # デフォルト値を "your_password" に設定


    # PostgreSQLに接続してデータを取得
    try:
        # データベース接続
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        print(message.MSG003)

        # カーソル作成
        cursor = connection.cursor()

        # 削除SQLクエリを実行
        delete_query = 'DELETE FROM sample;'
        cursor.execute(delete_query)

        # インサートSQLクエリを実行
        insert_query = "INSERT INTO sample (id, first_name, last_name) VALUES %s"
        extras.execute_values(cursor,insert_query , data)

        # 全件表示
        query = "SELECT * FROM sample;"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        # コミット
        connection.commit()
        
    except Exception as e:
        print(message.MSG005, e)

    finally:
        # リソースをクローズ
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print(message.MSG004)


