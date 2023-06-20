---
title: "電磁気学詳論II"
collection: courses
type: "全学共通教育科目"
permalink: /courses/2023-spring-elemag2
venue: "大阪大学, 全学共通教育機構"
date: 2023-03-29
location: "Osaka, Japan"
---

専門基礎教育科目(基礎工学部(システム、情報)、理学部(数学))、火曜日1限、共A302
[CLE授業支援システム](https://www.cle.osaka-u.ac.jp/ultra/courses/_174604_1/cl/outline)

[このページ](https://stsykw.github.io/courses/2022-spring-elemag2)


スケジュール
----------
**4月11日**  
電磁気学詳論Iの復習  
真空中の電磁波: 波動方程式の導出とその解  

**4月18日**  
真空中の電磁波: 電磁波としての性質、エネルギーと運動量  

**4月25日**  
真空中の電磁波: 偏光  
電気伝導と導体の性質: 導体、電荷の保存則、電気伝導  

**5月2日**  
(銀杏祭で休講)

**5月9日**  
電気伝導と導体の性質: ジュール熱、ホール効果  
誘電体: 分極、電束密度、誘電率  

**5月16日**  
誘電体: 境界条件、エネルギー、具体例  

**5月23日**  
磁性体: 磁化、磁化電流、透磁率、境界条件  

**5月30日**  
磁性体: エネルギー、具体例  

**6月6日**  
磁性体: 強磁性体  

**6月13日**  
超伝導体と磁場: 完全反磁性、ロンドン方程式  
物質中の電磁波: 物質中のマクスウェル方程式、屈折率  

**6月20日**  
物質中の電磁波: 物質中のマクスウェル方程式、屈折率、反射、屈折  

**6月27日**  
物質中の電磁波: 反射、屈折、内部全反射、エバネッセント光、反射波の位相、導体と電磁波  

Quiz
----

解答はCLE経由で提出すること。手書き文書のスキャン、Word文書、Tex文書など形式は問わないが、最終的に提出時には一つのpdfファイルにまとめて提出すること。
基本的に提出締め切りは、出題日の一週間後の正午とします。

**Quiz 1(4月11日出題)**  
ベクトル微分演算子\\( \nabla \\)およびベクトル値関数\\( \boldsymbol{A} \\)に対し
\\[
  \nabla \times ( \nabla \times \boldsymbol{A}) = \nabla (\nabla \cdot \boldsymbol{A} ) - \nabla^2 \boldsymbol{A}
\\]
となることを示せ。

**Quiz 2(4月18日出題)**  
磁束密度も波動方程式を満たす。\\(  \boldsymbol{e_{z}} \\)ベクトルの向きに進行する進行波解を
\\[
  \boldsymbol{B} =  
     \boldsymbol{e_{x}} f_{x}( z - ct ) 
    +\boldsymbol{e_{y}} f_{y}( z - ct ) 
    +\boldsymbol{e_{z}} f_{z}( z - ct ) 
\\]
と仮定して、Maxwell方程式をもちい磁束密度が横波として伝わることを示せ。またこの磁束密度に対応する電場\\( \boldsymbol{E} \\)を求めよ。

**Quiz 3(4月25日出題)**  
Drudeモデルで電気伝導率\\( \sigma \\)は
\\[
  \sigma = \dfrac{ne^2\tau}{m}
\\]
と計算された。銅の場合に値を計算してみよ。ただし銅の自由電子密度を\\( n=8.5\times 10^{28} \mathrm{m}^{-3} \\)、
緩和時間\\( \tau \\)は、平均自由行程\\( \ell = 4.0\times 10^{-8} \mathrm{m}\\)を電子の特徴的な速度\\( v=1.6\times 10^6 \mathrm{ms^{-1}}\\)で割ったものとして求めよ。
その他の数値は理科年表などで調べよ。

**Quiz 4(5月9日出題)**  
Drudeモデルに磁場を加えたものを二次元で考察する。
粒子は\\( xy \\)平面内を運動し、\\( z \\)軸正の向きに磁場\\( \boldsymbol{B} \\)がかけられているとする。
電荷\\( q (> 0) \\)、質量\\( m \\)をもつ荷電粒子の速度\\( \boldsymbol{v} \\)
は、定常状態で
\\[
  q \boldsymbol{E} - \dfrac{m}{\tau} \boldsymbol{v} + q \boldsymbol{v} \times \boldsymbol{B} = 0
\\]
を満たす。
電流密度\\( \boldsymbol{i} = \rho \boldsymbol{v} = n q \boldsymbol{v} \\)は\\( x\\)軸正の向きを向いていると仮定して、
Hall電場(電流と直交する方向の電場成分)の大きさを求めよ。

**Quiz 5(5月16日出題)**  
無限に広い誘電率\\( \epsilon \\)をもつ厚さ\\( d\\)の誘電体の板に、面に直交するように外部から電場\\( \boldsymbol{E_0 }\\)を加えた。
* 誘電体内部の電場\\( \boldsymbol{E}\\)および電気分極\\( \boldsymbol{P}\\)を\\( \boldsymbol{E_0} \\)をつかって表せ。
* 誘電体の板の表面に誘導される誘導電荷密度の大きさを求めよ。

**Quiz 6(5月23日出題)**  
原点にある磁気双極子モーメント\\( \boldsymbol{m} \\)が点\\( \boldsymbol{r} \\)につくるベクトルポテンシャルは
\\[
  \boldsymbol{A}(\boldsymbol{r}) = \dfrac{\mu_0}{4\pi} \dfrac{ \boldsymbol{m} \times \boldsymbol{r}}{\lvert \boldsymbol{r} \rvert^3}
\\]
である。このベクトルポテンシャルが表す磁束密度\\( \boldsymbol{B} \\)を計算し、結果が磁気双極子モーメントが作る磁束密度と同じことを確認せよ。

**Quiz 7(5月30日出題)**  
講義で、半径\\( a\\)の無限に長い円柱型常磁性体(透磁率\\( \mu \\))に一様に電流 \\( I \\)が流れているときの、磁場\\( \boldsymbol{H} \\)と磁束密度\\( \boldsymbol{B} \\)を取り扱った。復習も兼ねて以下の問いに解答せよ。
* 磁場を、半径が\\( r >a \\)と\\( r < a \\)の場合に分けて導出せよ。
* 同様に磁束密度を求めよ。
* 同様に磁化を求めよ。
* 得られた磁化がどのような磁化電流で説明できるか述べよ。

**Quiz 8(6月6日出題)**  
原点を中心とする半径\\( a \\)の球面上の積分\\( I\\)
\\[
  I = \int_{\lvert \boldsymbol{r'} \rvert=a } dS' \dfrac{\boldsymbol{r'}\cdot \boldsymbol{r}}{\lvert\boldsymbol{r}-\boldsymbol{r'} \rvert}
\\]
を計算せよ。上で\\( \boldsymbol{r'} \\)は球面上の位置ベクトルで、\\( \boldsymbol{r} \\)は\\( z \\) 軸上のある点の位置ベクトルであるとする。

**Quiz 9(6月13日出題)**  
渦度\\( \boldsymbol{\omega} \\)を
\\[
  \boldsymbol{\omega} = \nabla \times \boldsymbol{v} + \dfrac{q}{m} \boldsymbol{B}
\\]
と定義する。
速度場の時間発展が
\\[
  \dfrac{\partial \boldsymbol{v}}{\partial t} + (\boldsymbol{v}\cdot \nabla ) \boldsymbol{v} = 
  \dfrac{q}{m} ( \boldsymbol{E} + \boldsymbol{v}\times \boldsymbol{B})
\\]
を満たすとき、
渦度の時間発展が
\\[
  \dfrac{\partial \boldsymbol{\omega}}{\partial t} = \nabla \times (\boldsymbol{v} \times \boldsymbol{\omega})
\\]
となることを示せ。
(ヒント: (8)式から出発する。まず両辺の回転を取る。\\( \nabla \times \boldsymbol{E} = - \dfrac{\partial \boldsymbol{B}}{\partial t} \\) をつかって、電場の回転を磁場の時間変化に置き換える。時間微分に関する項をすべて左辺に集める。\\( (\boldsymbol{v}\cdot \nabla) \boldsymbol{v}  \\)を\\( \boldsymbol{v} \times (\nabla \times \boldsymbol{v}) \\)をつかって置き換える。)

**Quiz 10(6月20日出題)**  
実電荷も実電流も存在しない物質を考える。物質は線形の常誘電体でかつ常磁性体であるとする。
\\[
\boldsymbol{D} = \epsilon \boldsymbol{E}, \quad   \boldsymbol{H} = \dfrac{\boldsymbol{B}}{\mu}
\\]
この物質中のMaxwell方程式
$$
  \begin{align}
\nabla \cdot  \boldsymbol{D}  & = 0  \\
\nabla \times \boldsymbol{E} & = - \dfrac{\partial \boldsymbol{B}}{\partial t} \\
\nabla \cdot \boldsymbol{B} & = 0 \\
\nabla \times  \boldsymbol{H} & =  \dfrac{\partial \boldsymbol{D}}{\partial t} 
\end{align}
$$
より、電場\\( \boldsymbol{E} \\)が満たす波動方程式を導出せよ。

評価
-----
期末試験(60%)、及びQuiz等(平常点 40%)で判断する。シラバスに従う。


文献
-----
電磁気学詳論Iでつかった教科書や資料は参考になります。
それ以外の参考書、演習書などをあげおきます。
参考書は、詳しい内容や教科書以外の記述を見たくなった場合に利用してください。
すべて大学図書館にあると思います。
* 参考書: 前野昌弘「よくわかる電磁気学」東京図書
* 参考書: 太田浩一「電磁気学の基礎I」東京大学出版会
* 参考書: 太田浩一「電磁気学の基礎II」東京大学出版会
* 参考書: J. D. ジャクソン(著)、西田稔(訳)「電磁気学(上)」吉岡書店
* 演習書: 後藤憲一、山崎修一郎(編)「詳解電磁気学演習」共立出版
