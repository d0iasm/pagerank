# Pagerank
Page rank with random surfer model.

## Usage
```
$ git clone https://github.com/d0iasm/pagerank.git
$ cd pagerank
$ python pagerank.py
```
If you input pagerank score, pages with a higher score is displayed.

Try changing ``self.limit = 10000``  
The more times, the more reliable it is. However, it takes time to execute...

[caution]  
python >= 3.0

## What Page Score?
``pagescore = (visited times) / (limit count) * 100 (%)``
- visited times: Number of times the surfer visited.
- limit count: Maximum number of times the surfer moves.

### When limit = 1000 (=1000 times surfing the net)
#### 0.3% or more (highest pagescore group)
950898	神奈川県

#### 0.2% or more
7	パリ  
75	医学  
940	ラオス  
1242	歴史  
1307	俳優  
5851	カリフォルニア州  
7277	国立国会図書館  
9256	プラットホーム  
14694	ゴム  
17426	マルクス主義  
17604	テレビドラマ  
22320	病理学  
25872	Portable_Document_Format  
26314	重要文化財  
35228	哲学者  
44729	日高市  
90429	ハゼ  
376340	フォルセティ  
432011	IS-4  
851107	イギリス  
927119	日本  
950898	神奈川県  
964312	ルンピ  
1065960	ヴィルパント  

### When limit = 10000 (=10000 times surfing the net)
#### 0.1% or more (highest pagescore group)
2245	英語  
851077	アメリカ合衆国  
851096	ドイツ  
927119	日本  

#### 0.05% or more
178	沖縄県  
184	滋賀県  
1313	キリスト教  
1652	歌手  
2018	メートル  
2156	業種  
2244	イタリア  
2245	英語  
2405	漫画家一覧  
2781	ISBN  
3385	ウィクショナリー  
3634	人口  
4875	朝鮮語  
4915	国家  
5506	江戸幕府  
10790	アルバム  
151501	福岡県  
158620	中国  
215164	インターネット・ムービー・データベース  
353562	MBSテレビ  
409713	東京都  
680677	セーフティフレーズ  
851073	カナダ  
851077	アメリカ合衆国  
851093	フランス  
851096	ドイツ  
851107	イギリス  
927119	日本  
950898	神奈川県  
1038457	地理座標系  


