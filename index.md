<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>論文一覧</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to right, #ece9e6, #ffffff);
            color: #333;
            padding: 20px;
        }
        h1 {
            text-align: center;
            margin-bottom: 40px;
            color: #2c3e50;
        }
        .container {
            max-width: 800px;
            margin: auto;
        }
        select, ul {
            width: 100%;
            padding: 10px;
            margin: 20px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
            padding: 10px;
            background: #3498db;
            color: #fff;
            border-radius: 5px;
        }
        a {
            color: #fff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>論文一覧</h1>
    <div class="container">
        <select id="categorySelect">
            <option value="">カテゴリを選択してください</option>
        </select>
        <ul id="paperList"></ul>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const categories = {
                'Agent': ['Paper1', 'Paper2'],  // ここにフォルダ構造から取得したデータを追加
                'Innovation': ['Paper1', 'Paper2']  // 同上
            };

            const categorySelect = document.getElementById('categorySelect');
            const paperList = document.getElementById('paperList');

            for (const category in categories) {
                const option = document.createElement('option');
                option.value = category;
                option.textContent = category;
                categorySelect.appendChild(option);
            }

            categorySelect.addEventListener('change', function() {
                const selectedCategory = this.value;
                paperList.innerHTML = '';

                if (selectedCategory && categories[selectedCategory]) {
                    categories[selectedCategory].forEach(paper => {
                        const li = document.createElement('li');
                        const a = document.createElement('a');
                        a.href = `Research_papers/${selectedCategory}/${paper}/${paper}.md`;
                        a.textContent = paper;
                        li.appendChild(a);
                        paperList.appendChild(li);
                    });
                }
            });
        });
    </script>
</body>
</html>