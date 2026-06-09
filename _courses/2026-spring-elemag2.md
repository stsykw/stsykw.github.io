---
title: "電磁気学詳論II"
collection: courses
type: "全学共通教育科目"
permalink: /courses/2026-spring-elemag2
venue: "大阪大学, 全学共通教育機構"
date: 2026-04-01
location: "Osaka, Japan"
---

専門基礎教育科目(基礎工学部(システム、情報)、理学部(数学))、火曜日1限、共A302  
[CLE授業支援システム](https://www.cle.osaka-u.ac.jp/ultra/courses/_242203_1/outline)

[このページ](https://stsykw.github.io/courses/2026-spring-elemag2)


スケジュール
----------
**4月14日**  
電磁気学詳論Iの復習  
真空中の電磁波: 波動方程式の導出とその解  

**4月21日**  
真空中の電磁波: 電磁波としての性質、エネルギーと運動量  

**4月28日**  
真空中の電磁波: 偏光  
電気伝導と導体の性質: 導体、電荷の保存則、電気伝導  

**5月12日**  
誘電体: 分極、電束密度、誘電率、境界条件  

**5月19日**  
誘電体: エネルギー、具体例  

**5月26日**  
磁性体: 磁化、磁化電流、透磁率  

**6月2日**  
磁性体: 境界条件、エネルギー、具体例  

**6月9日**  
磁性体: 具体例、強磁性体の例  
超伝導体と磁場: 超伝導  

**6月16日**  
物質中の電磁波: 物質中のマクスウェル方程式、屈折率  

Quiz
----

解答はCLE経由で提出すること。手書き文書のスキャン、Word文書、Tex文書など形式は問わないが、最終的に提出時には一つのpdfファイルにまとめて提出すること。
基本的に提出締め切りは、出題日の一週間後の正午とします。

**Quiz 1(4月14日出題)**  
ベクトル微分演算子\\( \nabla \\)およびベクトル値関数\\( \boldsymbol{A} \\)に対し
\\[
  \nabla \times ( \nabla \times \boldsymbol{A}) = \nabla (\nabla \cdot \boldsymbol{A} ) - \nabla^2 \boldsymbol{A}
\\]
となること、および
\\[
   (\nabla \times  \nabla )\times \boldsymbol{A} =0
\\]
であることを示せ。

**Quiz 2(4月21日出題)**  
真空中の電磁場のエネルギー密度
\\[
  u = \dfrac{\epsilon_0}{2} \left\lvert \boldsymbol{E}\right\rvert^2
  +\dfrac{1}{2\mu_0} \left\lvert \boldsymbol{B}\right\rvert^2
\\]
および、Poyntingベクトル
\\[
  \boldsymbol{S} = \dfrac{1}{\mu_0} \boldsymbol{E}\times \boldsymbol{B}
\\]
が、エネルギー保存の式
\\[
  \dfrac{\partial u}{\partial t} + \nabla \cdot \boldsymbol{S}=0
\\]
を満たすことを、電荷密度、電流密度が存在しない場合の真空中のMaxwell方程式をつかって
示せ。

**Quiz 3(5月19日出題)**  
誘電率\\( \epsilon \\)をもつ誘電体の領域が3次元空間中の\\( z \ge 0 \\)の領域に広がっているとする。\\(z < 0 \\)は真空であるとする。真空中から\\(z \\)軸に平行に\\( \boldsymbol{E_0 } =  E_0 \boldsymbol{e}\_{z} \\)という電場を誘電体に加えた。また誘電体中には実電荷は存在していないとする。
* 誘電体内部の電場\\( \boldsymbol{E}\\)および電気分極\\( \boldsymbol{P}\\)を\\( \boldsymbol{E_0} \\)をつかって表せ。
* 誘電体の\\(z = 0\\)の表面に誘導される分極電荷密度の大きさを求めよ。


**Quiz 4(5月26日出題)**  
原点にある磁気双極子モーメント\\( \boldsymbol{m} \\)が点\\( \boldsymbol{r} \\)につくるベクトルポテンシャルは
\\[
  \boldsymbol{A}(\boldsymbol{r}) = \dfrac{\mu_0}{4\pi} \dfrac{ \boldsymbol{m} \times \boldsymbol{r}}{\lvert \boldsymbol{r} \rvert^3}
\\]
である。このベクトルポテンシャルが表す磁束密度\\( \boldsymbol{B} \\)を計算し、結果が磁気双極子モーメントが\\( \boldsymbol{r} \ne 0\\)に作る磁束密度
\\[
  \boldsymbol{B} = \dfrac{\mu_0}{4\pi} 
  \left\[3 \dfrac{(\boldsymbol{m}\cdot \boldsymbol{r} ) \boldsymbol{r} }{r^{5}} - \dfrac{\boldsymbol{m}}{r^{3}}\right\]
\\]
と同じことを確認せよ。

**Quiz 5(6月2日出題)**  
単位長さあたり\\( n \\)巻きの十分長いソレノイドに電流\\( I \\)が流れているとする。
ソレノイドの内部には透磁率\\( \mu \\)の常磁性体で満たされているとする。
このとき磁場、磁束密度はソレノイドの軸方向(\\(z\\)軸方向)に、内部に一様に存在し、外部には存在しないとする。
* 物質中のAmpereの法則を使って、磁場および磁束密度を求めよ。
* 磁化を求めよ。
* 磁化電流について、どのような密度でどこに存在するか考察せよ。


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
