# データ前処理する前に

データ前処理をしたあとで機械学習を使って何かを予測した意思決定をする際、たとえば以下のようなサイトを定期的に確認して、正しく運用できているかどうかを常にチェックする必要があります（と、私は考えています）。

- [1] [人工知能学会倫理委員会 機械学習と公平性に関する声明](http://ai-elsi.org/archives/888)
- [2] [機械学習と公平性に関する声明とシンポジウム](http://ai-elsi.org/archives/898)
- [3] [私のブックマーク「機械学習のプライバシーとセキュリティ（Privacy and security issues in machine learning）」](https://www.ai-gakkai.or.jp/resource/my-bookmark/my-bookmark_vol32-no5/)
- [4] [ＡＩと著作権　学習用データセットの生成](http://www.uit-patent.or.jp/%EF%BD%81%EF%BD%89%E3%81%A8%E8%91%97%E4%BD%9C%E6%A8%A9-2/%EF%BD%81%EF%BD%89%E3%81%A8%E8%91%97%E4%BD%9C%E6%A8%A9/)
- [5] [EU 一般データ保護規則（GDPR）の概要（前編）](https://www.intellilink.co.jp/article/column/security-gdpr01.html)
- [6] [著作権 | 文化庁](https://www.bunka.go.jp/seisaku/chosakuken/)
- [7] [GDPR（General Data Protection Regulation：一般データ保護規則）](https://www.ppc.go.jp/enforcement/infoprovision/laws/GDPR/)

また、扱うデータが『_識別された又は識別され得る自然人（以下「データ主体」という。）に関するあらゆる情報を意味する。識別され得る自然人は、特に、氏名、識別番号、位置データ、オンライン識別子のような識別子、または当該自然人に関する物理的、生理的、遺伝子的、精神的、経済的、文化的もしくは社会的アイデンティティに特有な一つ、もしくは複数の要素を参照することによって、直接的にまたは間接的に、識別され得る（GDPR 第 4 条）_（[5]より引用）』かどうかを必ずチェックする必要があります。

そして、データそのもののバイアスや標本の選択の仕方によるバイアス、帰納バイアス ("_機械学習手法が汎化のために採用している仮定が，実世界の状況とはずれている場合_([引用元](http://ai-elsi.org/wp-content/uploads/2020/01/20200109-fairness_sympo.pdf))"によって機械学習の結果が変化することを把握する必要があります。
つまり、**データ前処理をする際には必ずそれが後続の処理**（前処理・機械学習モデル・後処理・意思決定）**にどのような影響を与えるかを確認する必要があります**。
