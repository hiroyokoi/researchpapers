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

![alt text](image-1.png)
Figure 3: A morning in the life of a generative agent, John Lin. John wakes up around 6 am and completes his morning routine, which includes brushing his teeth, taking a shower, and eating breakfast. He briefly catches up with his wife, Mei, and son, Eddy, before heading out to begin his workday.

![alt text](image-2.png)
Figure 4: At the beginning of the simulation, one agent is initialized with an intent to organize a Valentine’s Day party. Despite many possible points of failure in the ensuing chain of events—agents might not act on that intent, might forget to tell others, might not remember to show up—the Valentine’s Day party does, in fact, occur, with a number of agents gathering and interacting.

## 1-3. Emergent Social Behaviors
- Information Diffusion
- Relationship Memory
- Coordination

# 2. GENERATIVE AGENT ARCHITECTURE
Generative Agentsのコアのアーキテクチャは、Memory Streamであり、レコードがエージェントの経験として蓄積されていき、エージェントの特定のアクションを計画するのにrelevantなものがretrieveされ、レコードとなる。このレコードが継続的により高次元のリフレクションとしてシンセサイズされ、自然言語してreasoningされる。

![alt text](image-4.png)
Figure 5: Our generative agent architecture. Agents perceive their environment, and all perceptions are saved in a comprehensive record of the agent’s experiences called the memory stream. Based on their perceptions, the architecture retrieves relevant memories and uses those retrieved actions to determine an action. These retrieved memories are also used to form longer-term plans and create higher-level reflections, both of which are entered into the memory stream for future use.

## 2-1. Memory and Retrieval
Memory Streamは、メモリオブジェクトのリストであり、オブジェクトは自然言語の説明、タイムスタンプの生成、最も直近アクセスしたタイムスタンプ、を意味する。最もベーシックなmemory streamの要素は*observation*である。よくあるobservationsは、エージェント自身による行動、もしくは他のエージェントが実行ししたものを当該エージェントが認識する（perceive）行動である。例えば、Isabella Rodriguezは、コーヒーショップで働いており、以下のようなobservationを行う。
```
(1) Isabella Rodriguez is setting out the pastries
(2) Maria Lopez is studying for a Chemistry test while drinking coffee
(3) Isabella Rodriguez and Maria Lopez are conversing about planning a Valentine’s day party at Hobbs Cafe
(4) The refrigerator is empty
```

Retrieval functionとして、エージェントの現在の状況をインプットに、一式のメモリーストリームをリターンする。Retrievalを適切に行うため、以下の方法により実行された。
- *Recency*: 最近アクセスされたメモリーオブジェクトに高いスコアが付与される。実装では、サンドボックスでのゲーム時間に応じてexponential decay functionを適用し、decay factorは0.995に設定した。
- *Importance*: コアメモリのありふれたメモリから、エージェントが重要だと思うメモリーオブジェクトを識別するためのもの。朝食を食べるなどの取るに足らないイベントは低いimportanceスコアが与えれば、そうではない場合は高いスコアとなる。実装では、LLMに以下のとおりプロンプトを与えてスコアをintegerで算出した。Importanceスコアは、メモリオブジェクトが作られるときに算出した。
    ```
    >On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory. Memory: buying groceries at The Willows Market and Pharmacy

    >Rating: <fill in>
    ```
- *Relevance*:現在のシチュエーションに関連するメモリーオブジェクトが高いスコアが与えられる。関連するという点については、queryと各メモリ内のembedding vectorのcosine similarityにより算出した。
- *final retrieval score*: 0~1の範囲で、3つの指標をminmax scalingし算出した。各要素にウェイトをかける形都市、以下のように算出された。実装では、$\alpha$はすべて1に設定した。
  
  $retrievalscore = \alpha_{recency} \cdot recency + \alpha_{importance} \cdot importance + \alpha_{relevance} \cdot relevance$

![alt text](image-3.png)
Figure 6: The memory stream comprises a large number of observations that are relevant and irrelevant to the agent’s current situation. Retrieval identifies a subset of these observations that should be passed to the language model to condition its response to the situation.

## 2-2. Reflection
Reflectionを適切に行うため、もう一つのメモリである**reflection**を使う。Reflectionは、エージェントが生成するハイレベルでアブストラクトな思考である。これはメモリの一つであるため、Retrievalが発生する際に他のobservationsと一緒に引っ張ってくることができる。Reflectionsは定期的に行うものであり、実装では、直近のイベントのimportance scoreの合計が閾値（実装では150回）を超えた時にreflectionsを実行した。実態として、エージェントは1日に2-3回リフレクションを実行した。

Reflectionの第1ステップは、何をreflectionするかであり、これはエージェントの直近の経験から、想定される質問をidentifyすることである。

本実装では、まずエージェントのmemory streamのもっとも直近の100レコードに対してlarge language modelにqueryを行う。memory streamの例は以下のとおり。

```
“Klaus Mueller is reading a book on gentrification”

“Klaus Mueller is conversing with a librarian about his research project” 

“desk at the library is currently unoccupied”
```

次に、language modelでプロンプトを出す。
```
“Given only the information above, what are 3 most salient highlevel questions we can answer about the subjects in the statements?
```

その結果、モデルは以下のような質問候補を生成する。

```
What topic is Klaus Mueller passionate about?

What is the relationship between Klaus Mueller and Maria Lopez? 
```

これらの質問をRetrieval用のクエリとして用い、各質問に対してrelevantなメモリを収集する。

次に、LLMを用いて、インサイトを抽出し、インサイトの基となる特定のレコードも引用する。プロンプトは以下のとおり。

```
Statements about Klaus Mueller
1. Klaus Mueller is writing a research paper
2. Klaus Mueller enjoys reading a book on gentrification
3. Klaus Mueller is conversing with Ayesha Khan about exercising [...]

What 5 high-level insights can you infer from the above statements? (example format: insight (because of 1, 5, 3))

```

これにより、以下のようなレスポンスが返ってくる。
```
Klaus Mueller is dedicated to his research on gentrification (because of 1, 2, 8, 15). 
```

このstatementsをメモリストリーム内のreflectionとして保存する。なお、引用されたメモリーオブジェクトも含めて保存する。

Reflectionsは、自分自身のobservationsだけではなく、他のエージェントのreflectionsも反映させられる。Klaus Muellerの上記のreflectionは彼自身のものではなく、他のenvironmentのものである。その結果、エージェントはtrees of reflectionsを作成することができ、リーフノードがbase observationsを示し、non-leaf nodesがより抽象化され、ハイレベルなreflectionsとなる。

![alt text](image-5.png)
Figure 7: A reflection tree for Klaus Mueller. The agent’s observations of the world, represented in the leaf nodes, are recursively synthesized to derive Klaus’s self-notion that he is highly dedicated to his research

## 2-3. Planning and Reacting



# 結果

# 考察
