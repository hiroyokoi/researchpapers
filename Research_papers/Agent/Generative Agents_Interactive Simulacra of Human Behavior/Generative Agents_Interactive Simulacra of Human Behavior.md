# Title
Generative Agents: Interactive Simulacra of Human Behavior

# Authors
Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein

# Publication Year
April 2023

# Journal
ACM Symposium on User… 7 April 2023

# Citation
1,275

# 背景及び先行研究との違い
人間の行動を模したSimsをエージェントを作ることで、短期的なインタラクションと長期的なコミュニケーションによるエージェントの進化を実装したもの

# 研究内容

# 1. GENERATIVE AGENT BEHAVIOR AND INTERACTION
## 1-1. Agent Avatar and Communication
Smallvilleに居住する25のエージェントのコミュニティを生成する。エージェントの生成は1パラの自然言語により生成され、職業、他のエージェントの関係性を含める。例えば、John Linは以下のように表現される。

```
John Lin is a pharmacy shopkeeper at the Willow Market and Pharmacy who loves to help people. He is always looking for ways to make the process of getting medication easier for his customers; John Lin is living with his wife, Mei Lin, who is a college professor, and son, Eddy Lin, who is a student studying music theory; John Lin loves his family very much; John Lin has known the old couple next-door, Sam Moore and Jennifer Moore, for a few years; John Lin thinks Sam Moore is a kind and nice man; John Lin knows his neighbor, Yuriko Yamamoto, well; John Lin knows of his neighbors, Tamara Taylor and Carmen Ortiz, but has not met them before; John Lin and Tom Moreno are colleagues at The Willows Market and Pharmacy; John Lin and Tom Moreno are friends and like to discuss local politics together; John Lin knows the Moreno family somewhat well — the husband Tom Moreno and the wife Jane Moreno.
```

### 1-1-1 Inter-Agent Communication
エージェントは、サンドボックス内で、“Isabella Rodriguez is writing in her journal”, “Isabella Rodriguez is checking her emails”, “Isabella Rodriguez is talking with her family on the phone”, or “Isabella Rodriguez is getting ready for bed.”といった自然言語で現在のアクションを説明する。このアクションは、サンドボックスのUI上にabstractな表現を示すため、絵文字に変換されスピーチバブル上に説明される。例えば、🗒️✏️であれば、“Isabella Rodriguez is writing in her journal” であるし、💻✉️であれば、“Isabella Rodriguez is checking her emails”となる。

エージェントは、お互いのローカルエリアの情報を理解している。例えば、以下のような会話がなされる。

```
Isabella: I’m still weighing my options, but I’ve been discussing the election with Sam Moore. What are your thoughts on him?

Tom: To be honest, I don’t like Sam Moore. I think he’s out of touch with the community and doesn’t have our best interests at heart
```
### 1-1-2 User Controls
ユーザーコミュニケーションは、ペルソナをspecifyすることで、コミュニケーションを行う。例えば、ユーザーがニュースレポーターとペルソナ定義し、直近の選挙について、"Who is running for office?"と質問すると、Johnエージェントは以下のように応える。

```
John: My friends Yuriko, Tom and I have been talking about the upcoming election and discussing the candidate Sam Moore. We have all agreed to vote for him because we like his platform
```

## 1-2 Envornmental Interaction
Smallvilleは、小さな村にあるものを再現したものであり、カフェ、バー、公園、学校、寮、家、お店がある。また、サブエリアとして、家の中のキッチンや、キッチンの中のストーブというような構造も含まれる。エージェントのprimary livingクォーターは、ベッド、デスク、クローゼット、棚、風呂、キッチンである。

![alt text](image.png)

Figure 2: The Smallville sandbox world, with areas labeled. The root node describes the entire world, children describe areas (e.g., houses, cafe, stores), and leaf nodes describe objects (e.g., table, bookshelf). Agents remember a subgraph that reflects the parts of the world they have seen, maintaining the state of those parts as they observed them.

エージェントは、smallvilleの中を動き回る。エージェントの動きは、generative agentのアーキテクチャとサンドボックス内のゲームエンジンにdirectされる。例えば、エージェントがどこかに移動するときに、裏側ではsmallville内の環境において目的地までのwalking pathが計算され、そのうえで、エージェントは動き出す。

　　
##


# 2. GENERATIVE AGENT ARCHITECTURE


# 結果

# 考察
