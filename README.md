# 起動手順

依存関係の解決（python が使用できる環境であること）

```shell
python -m venv .venv #仮想環境の作成
pip install --upgrade pip && pip install -r requirements.txt #ライブラリのインストール
```

起動

```shell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
