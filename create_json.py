import os
import json

def create_json_files(root_dir):
    # カテゴリを取得
    categories = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]

    # categories.json を作成
    with open('data/categories.json', 'w') as f:
        json.dump(categories, f)

    # 各カテゴリのJSONファイルを作成
    for category in categories:
        category_path = os.path.join(root_dir, category)
        papers = [d for d in os.listdir(category_path) if os.path.isdir(os.path.join(category_path, d))]
        
        paper_data = [{"title": paper} for paper in papers]
        
        with open(f'data/{category}.json', 'w') as f:
            json.dump(paper_data, f, indent=2)

    print("JSON files have been created successfully.")

# スクリプトを実行
if __name__ == "__main__":
    root_directory = "Research_papers"  # このパスは実際のディレクトリ構造に合わせて調整してください
    
    # data ディレクトリが存在しない場合は作成
    if not os.path.exists('data'):
        os.makedirs('data')
    
    create_json_files(root_directory)
