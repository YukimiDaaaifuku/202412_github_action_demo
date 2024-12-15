-- DB作成
CREATE DATABASE sample_db;

-- 作成したDBに接続
\c sample_db;

-- テーブル作成
DROP TABLE IF EXISTS sample;
CREATE TABLE sample (
	id integer NOT NULL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);

-- サンブルデータの登録
INSERT INTO sample (id, first_name, last_name) VALUES 
    (01, '田中', '太郎'),
    (02, '鈴木', '次郎'),
    (03, 'ジョン', 'マイケル');