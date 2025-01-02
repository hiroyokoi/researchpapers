# Title
A Survey on Large Language Model based Autonomous Agents

# Authors
LeiWang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhi-Yuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, ZheweiWei, Ji-RongWen

# Publication Year
August 2023

# Journal
Frontiers Comput. Sci. 22 August 2023

# Citation
754 (accessed on Dec 27, 2024)

# 背景及び先行研究との違い
Autonomous Agentsに関するレビューアーティクル

# 研究内容
LLMベースのautonomous agentsを規定するフレーム枠として以下を提示。
![alt text](image.png)

## Profiling Module
プロファイルとして、コーディング、先生、ドメイン専門家などのロールを担う。エージェントプロファイルとして、年齢・性別・キャリア・物理的情報を含み、エージェントのパーソナリティ・ソーシャルデータ・エージェント間のインタラクションをリフレクションする。特に、人間の認知プロセスを学習させる場合は、心理的な情報が不可欠となる。
プロファイルが決まった後は、特定のプロファイルを示すエージェントの作り方であり、以下の3つの方法に分かれる。

- **Handcrafting Method**：マニュアルでエージェントのプロファイルを規定する方法であり、”You are an outgoing person”や"You are an introvered person"として規定する
    >Zhang H, Du W, Shan J, Zhou Q, Du Y, Tenenbaum J B, Shu T, Gan C. Building cooperative embodied agents modularly with large language models. arXiv preprint arXiv:2307.02485, 2023

    >Hong S, Zheng X, Chen J, Cheng Y, Wang J, Zhang C, Wang Z, Yau S K S, Lin Z, Zhou L, others . Metagpt: Meta programming for multi-agent collaborative framework. arXiv preprint arXiv:2308.00352, 2023

    >Qian C, Cong X, Yang C, Chen W, Su Y, Xu J, Liu Z, Sun M. Communicative agents for software development. arXiv preprint arXiv:2307.07924, 2023

- **LLM-generation Method**：LLMにより自動的にプロファイルを生成するもの。まずプロファイル生成ルールを定め、エージェントのプロファイルの構成と属性を定める。そのうえで、オプション的に複数シードとfew-shotによりエージェントを生成する。例えば、RecAgent論文では、年齢、性別、特徴、映画の嗜好性などの属性について、数人分のエージェントのプロファイルを作成し、その後ChatGPTで、シード情報を変えることにより、より多くのエージェントの生成を行っている。
    >Wang L, Zhang J, Chen X, Lin Y, Song R, Zhao W X, Wen J R. Recagent: A novel simulation paradigm for recommender systems. arXiv preprint arXiv:2306.02552, 2023

- **Dataset Alignment Method**：リアルワールドデータを用いて、エージェントをあらインさせる方法。例えば、American National Election Studiesを用いて、参加者の人種・宗教、性別、年齢、居住地のデモグラを用いてGPT3にロールを与えるもの。
    > Argyle L P, Busby E C, Fulda N, Gubler J R, Rytting C, Wingate D. Out of one, many: Using language models to simulate human samples. Political Analysis, 2023, 31(3): 337–351

## Memory Module
メモリーとは、エージェントが外界から得られる情報や将来のアクションを促すための記録されたメモリの活用をするために使われるものである。メモリは、経験・self-evolve・アクションを、一貫性があり、リーズナブルで、効果的な形でガイドするものとなる。
- **Memory Structures**：人間の認知科学に照らしたもの。人間の記憶は、一時的な情報を維持するための短期記憶と、長期間にわたって統合される長期記憶に分類される。エージェントの世界では、二つの方法により短期・長期記憶のメモリ活用がなされる。
  1. **Unified Memory**：短期記憶のみ捉えるもの。メモリ情報はプロンプトに直接書き込まれる
  2. **Hybrid Memory**：短期記憶と長期記憶を捉える。短期記憶は、エージェントの現在のシチュエーションに関するコンテキスト情報をメモリ化する。Generative Agentでは、長期記憶は、現在のイベントからretrieveされるエージェントの過去の行動と思考となる。AgentSimsでも、短期・長期記憶が扱われており、短期記憶はプロンプトで提供される。一方、長期記憶は、エージェントの短期記憶がエンベディングされ、ベクターデータベースに保存される。エージェントが過去の記憶を呼び起こすときに、ベクターデータベースから、エンベディングの類似度を用いて、retrieveするものである。GITMでは、短期記憶は現在のtrajectoryを保存し、長期記憶は成功した過去のtrajectoriesからサマリされたreference plansを保存する。Reflexionでは、短期的なsliding windowにより直近のフィードバックを捉え、persistentな長期記憶をcondensed insightsとして統合する。この短期・長期記憶の組み合わせが、直近の経験をハイレベルの抽象化に使うことができる。
      >Park J S, O’Brien J, Cai C J, Morris M R, Liang P, Bernstein M S. Generative agents: Interactive simulacra of human behavior. In: Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology. 2023, 1–22
      
      > <font color = 'lightblue'>Lin J, Zhao H, Zhang A, Wu Y, Ping H, Chen Q. Agentsims: An open-source sandbox for large language model evaluation. arXiv preprint arXiv:2308.04026, 2023</font>

      > Zhu X, Chen Y, Tian H, Tao C, Su W, Yang C, Huang G, Li B, Lu L, Wang X, others . Ghost in the minecraft: Generally capable agents for open-world enviroments via large language models with text-based knowledge and memory. arXiv preprint arXiv:2305.17144, 2023

      > <font color = 'lightblue'>Shinn N, Cassano F, Gopinath A, Narasimhan K, Yao S. Reflexion: Language agents with verbal reinforcement learning. Advances in Neural Information Processing Systems, 2024, 36</font>

- **Memory Formats**: 上記で述べたMemory Structureだけではなく、メモリのフォーマットも論点に上がる。フォーマットとしては、自然言語メモリ、エンベディングメモリがある。
  1. **Natural Language**: エージェントの行動や観察を自然言語のフォーマットとするもの。Reflexionでは、経験的なフィードバックを自然言語のsliding windowで保存している。Voyagerでは、Minecraftゲームにおけるスキルを自然言語で保存している。
      > Shinn N, Cassano F, Gopinath A, Narasimhan K, Yao S. Reflexion: Language agents with verbal reinforcement learning. Advances in Neural Information Processing Systems, 2024, 36 

      > Wang G, Xie Y, Jiang Y, Mandlekar A, Xiao C, Zhu Y, Fan L, Anandkumar A. Voyager: An open-ended embodied agent with large language models. arXiv preprint arXiv:2305.16291, 2023

  2. **Embeddings**：メモリインフォメーションはエンベディングベクターで保存される。
      > Zhong W, Guo L, Gao Q, Wang Y. Memorybank: Enhancing large language models with long-term memory. arXiv preprint arXiv:2305.10250, 2023


  3. **Databases**: メモリ情報がデータベースに保管され、エージェントが効率的にメモリを取得する
      > Hu C, Fu J, Du C, Luo S, Zhao J, Zhao H. Chatdb: Augmenting llms with databases as their symbolic memory. arXiv preprint arXiv:2306.03901, 2023

  4. **Structured Lists**：リスト形式でメモリ情報が保管される。GITMでは、サブゴールのアクションリストを階層化ツリー構造で保管している。Ret-LLMでは、自然言語をトリプレットに変換し、メモリとして保存している。
      > Zhu X, Chen Y, Tian H, Tao C, Su W, Yang C, Huang G, Li B, Lu L, Wang X, others . Ghost in the minecraft: Generally capable agents for open-world enviroments via large language models with text-based knowledge and memory. arXiv preprint arXiv:2305.17144, 2023

      > <font color = 'lightblue'>Modarressi A, Imani A, Fayyaz M, Schütze H. Retllm: Towards a general read-write memory for large language models. arXiv preprint arXiv:2305.14322, 2023</font>

- **Memory Operations**: Memory Operationsとは、エージェントが外的環境とインタラクトするにあたって、重要な知識を獲得し、蓄積し、利用するのに必要な不可欠な要素。そのためには3つのクリティカルなメモリオペレーションがあり、Memory Reading, Memory Writing, Memory Reflectionである。

    - 1. **Memory Reading**: Memory Readingとは、エージェントのアクションを高めるために、メモリーから重要な情報を抜き出すことである。記憶の抜出には、3つのクライテリアがあり、recency, relevance, importanceである。
    $$ m=arg min_{m∈M}{\alpha}s^{rec}(q,m)+{\beta}s^{rel}(q,m)+{\gamma}s^{imp}(m)$$
    where,  
            q=query  
            M=set of memories  
            $s^{rec}$, $s^{rel}$, $s^{imp}$ = scoring fuctions for measuring the recency, relevance, and importance of the memory $m$  
    $s^{rec}$, $s^{rel}$, $s^{imp}$は、様々な手法で実行され、LSH, ANNOY, HNSW, FAISSがある。なお、式にあるとおり、重要度は、メモリーの特徴を反映するものであり、queryには依存しない。$\alpha$, $\Beta$, $\gamma$はバランシングパラメータである。  
    多くのスタディでは、${\alpha}={\gamma}=0$とし、relevance scoreである$s^{rel}$のみをメモリーリーディングとして考慮している（下記、1, 2, 3, 4論文）。$\alpha=\beta=\gamma=1.0$とすると、均等ウェイトとなる（下記、5論文）
    >1. Zhu X, Chen Y, Tian H, Tao C, Su W, Yang C, Huang  G, Li B, Lu L, Wang X, others . Ghost in the minecraft:  Generally capable agents for open-world enviroments  via large language models with text-based knowledge  and memory. arXiv preprint arXiv:2305.17144, 2023

    >2. Fischer K A. Reflective linguistic programming (rlp):  A stepping stone in socially-aware agi (socialagi).  arXiv preprint arXiv:2305.12647, 2023

    >3. Wang G, Xie Y, Jiang Y, Mandlekar A, Xiao C, Zhu  Y, Fan L, Anandkumar A. Voyager: An open-ended  embodied agent with large language models. arXiv  preprint arXiv:2305.16291, 2023

    >4. Modarressi A, Imani A, Fayyaz M, Schütze H. Retllm:  Towards a general read-write memory for large  language models. arXiv preprint arXiv:2305.14322,
    2023

    >5. Park J S, O’Brien J, Cai C J, Morris M R, Liang P,  Bernstein M S. Generative agents: Interactive simulacra  of human behavior. In: Proceedings of the 36th  Annual ACM Symposium on User Interface Software  and Technology. 2023, 1–22
    
    - 2. **Memory Writing**: Memory Writingは、外的環境においてメモリに情報を書き出す行為である。Writingの課題は二つあり、①どのように過去の類似した記憶を保存するか（i.e., Memory Duplicated）と②ストレージリミットに達したときにどのように情報を削除するか（i.e., Memory Overflow）である。
      1. **Memory Duplicated**: 類似情報を統合するもの。同じサブゴールに対して成功した一連のアクションをリスト化し、リストのサイズがN(=5)を超えた場合、LLMを用いてa unified plan solutionとして統合される。元々の一連のアクションは、新しく生成されたものに置き換えられる（下記論文1）。Augmented LLMでは、重複した情報をcount accumulationを通じて集約し、redundutなストレージを避ける(下記論文2)
      2. **Memory Overflow**: メモリがフルになったときに、過去のメモリを削除するもの。例えば、ChatDBでは、ユーザーコマンドにより削除し（下記論文3）、RET-LLMでは、メモリ用に固定サイズのバッファーを使い、First-in-First_outの考えで、古い情報を上書きしていく（下記論文4）。
   
        >1. Zhu X, Chen Y, Tian H, Tao C, Su W, Yang C, Huang  G, Li B, Lu L, Wang X, others . Ghost in the minecraft:  Generally capable agents for open-world enviroments  via large language models with text-based knowledge and memory. arXiv preprint arXiv:2305.17144, 2023

        >2. Schuurmans D. Memory augmented large language  models are computationally universal. arXiv preprint  arXiv:2301.04589, 2023
        
        >3. Hu C, Fu J, Du C, Luo S, Zhao J, Zhao H. Chatdb: Augmenting  llms with databases as their symbolic memory.  arXiv preprint arXiv:2306.03901, 2023
        
        >4. Modarressi A, Imani A, Fayyaz M, Schütze H. Retllm:  Towards a general read-write memory for large  language models. arXiv preprint arXiv:2305.14322,  2023
<br>
    - 3. **Memory Reflection**: Memory Reflectionは、自身の認知的、感情的、行動的プロセスを認識し、評価することができ能力を示すものである。目的は、エージェントが独立的に各種情報をサマリし、推測することができ能力を持つことである。Generative Agents（下記論文1）では、エージェントが過去の経験をメモリから抽象的なインサイトを導出し過去の経験をサマライズしている。具体的には、エージェントは、直近の記憶について3つのキークエスチョンを生成す。次に、それらのクエスチョンは、関連する情報を得るのに使われ、エージェントは5つのインサイトを引き出し、それらはハイレベルなアイデアを反映することとなる。例えば、以下の3つの文章は、
        >>“Klaus Mueller is writing a research paper”  
        >>“Klaus Mueller is engaging with a librarian to further his research”  
        >>“Klaus Mueller is conversing with Ayesha Khan about his research”  

            、以下のハイレベル抽象化を行う  
        >>“Klaus Mueller is dedicated to his research”.

            また、抽象化は、階層的に発生し、既存のインサイトを用いてインサイトが階層的に生成される。
            
            GITM（下記論文2）ではサブゴールの成功を達成したアクションがリストにストアされる。リストが5つの要素を超える場合、エージェントは共通し抽象化したパターンをサマライズし、それら要素をリプレースする。

            ExpeL（下記論文3）では、reflectionのため、2つのアプローチが提案されている。第一に、エージェントは同一のタスクにおける一連の成功・失敗のを比較し、次に、一連の成功したアクションコレクションから経験値を引き出すことをしている。

        > 1. Park J S, O’Brien J, Cai C J, Morris M R, Liang P, Bernstein M S. Generative agents: Interactive simulacra of human behavior. In: Proceedings of the 36th Annual ACM Symposium on User Interface Software
        and Technology. 2023, 1–22

        > 2. Zhu X, Chen Y, Tian H, Tao C, Su W, Yang C, Huang  G, Li B, Lu L, Wang X, others . Ghost in the minecraft:  Generally capable agents for open-world enviroments  via large language models with text-based knowledge  and memory. arXiv preprint arXiv:2305.17144, 2023

        >3. Zhao A, Huang D, Xu Q, Lin M, Liu Y J, Huang G.  Expel: Llm agents are experiential learners. arXiv  preprint arXiv:2308.10144, 2023

## Planning Module
Planning ModuleはPlannning without FeedbackとPlanning with Feedbackに別れる
![alt text](image-1.png)

### Planning without Feedback
フィードバックは得ずに、アクションの結果が将来のアクションに影響を及ぼすもの。
1. Single-path Reasoning：最終的なタスクが複数の中間ステップに分解され、LLMはそれに従う。Chain of Thought, Zero-shot-CoT, Reprompting（プランを作る前に各ステップが必要な前提条件をクリアしているかチェックするもの）、ReWOO（エージェントが最初にプランを立て、外的環境からは独立して観察を行い、最終的に最終結果を得るのにそれらを組み合わせるもの）などがある
2. Multi-path Reasoning：Reasoningステップがツリー系の構造にオーガナイズされ最終計画を立案するもの。各中間ステップは、複数の関連するステップから構成される。Self-consistent CoTでは、最終回答を得るには複数の思考のパスがあると仮定し、まずCoTにより複数のReasoning Pathsを生成し、関連する回答を生成し、そのうえで、高頻度の回答が最終アウトプットとして選ばれる（論文1）。Tree of Thoughts (ToT)では、ツリーのノードが”thought”を表し、すなわち中間のreasoning stepとなる。最終ブランは、Breadth-first searchかdepth-first searchにより生成される（論文2）。AoTは、アルゴリズミックな例をプロンプトに使っており、LLMのクエリを1回か数回のみでよくなる。これは、Zero-shotを活用し、各プランニングステップにおいて、まず複数の考えうる次のステップを生成し、次に、許容されるアクションへの距離を基に最終的なプランが決定される（論文3）。
    >1. Wang X, Wei J, Schuurmans D, Le Q, Chi E, Narang  S, Chowdhery A, Zhou D. Self-consistency improves  chain of thought reasoning in language models. arXiv  preprint arXiv:2203.11171, 2022
    >2. Yao S, Yu D, Zhao J, Shafran I, Griffiths T, Cao Y,  Narasimhan K. Tree of thoughts: Deliberate problem  solving with large language models. Advances in Neural  Information Processing Systems, 2024, 36
    >3. Sel B, Al-Tawaha A, Khattar V, Wang L, Jia R, Jin  M. Algorithm of thoughts: Enhancing exploration  of ideas in large language models. arXiv preprint  arXiv:2308.10379, 2023
3. External Planner：LLM+Pでは、まずPlanning Domain Definition Languages(PDDL)によりタスクを分解し、external plannerがPDDLを扱う、そして、LLM により自然言語で最終リザルトを出すものである（論文1）。LLM-DPでは、LLMを活用し、観察、現在のworld state、目的をPDDLに転換し、external plannerに共有され、最終アクションに変換される（論文2）。
    >1. Liu B, Jiang Y, Zhang X, Liu Q, Zhang S, Biswas J,  Stone P. LLM+P: Empowering large language models  with optimal planning proficiency. arXiv preprint  arXiv:2304.11477, 2023
    >2. Dagan G, Keller F, Lascarides A. Dynamic planning with a llm. arXiv preprint arXiv:2308.06391, 2023

### Planning with Feedback
1. Environmental Feedback：外的環境からフィードバックを得るもの。ReAct、Voyager(プランを3種類の環境フィードバックにする)、Ghostなど。
2. Human Feedback：直接人間からフィードバックを得るもの。Monologueでは、シーン判定において人間から積極的にFBをもらい、エージェントは、人間からのフィードバックをプロンプトに変え、プランニングとリーズニングに反映させる（論文1）。
    >1. Huang W, Xia F, Xiao T, Chan H, Liang J, Florence P, Zeng A, Tompson J, Mordatch I, Chebotar  Y, others . Inner monologue: Embodied reasoning  through planning with language models. arXiv preprint  arXiv:2207.05608, 2022
3. Model Feedback：エージェント自身のフィードバックを用いる。Self-Refineメカニズム（論文1）では、output-feedback-refinementプロセスからなる。まず、エージェントはアウトプットを生成し、そのあと、LLMを用いて、アウトプットに対するFBとリファインのガイドをもらう。そのうえで、アウトプットするかFBをもらい、アウトプットが更新される。SelfCheckでは、エージェントが各ステージでリーズニングステップを評価し、アウトカムを比較した場合のエラーを修正する（論文2）。そのほか、ChatCoTやReflexionがある。
    >1. Madaan A, Tandon N, Gupta P, Hallinan S, Gao L,  Wiegreffe S, Alon U, Dziri N, Prabhumoye S, Yang  Y, others . Self-refine: Iterative refinement with selffeedback.  Advances in Neural Information Processing  Systems, 2024, 36
    >2. Miao N, Teh Y W, Rainforth T. Selfcheck: Using llms  to zero-shot check their own step-by-step reasoning.  In: The Twelfth International Conference on Learning  Representations. 2023

## Action Module


# 結果

# 考察
