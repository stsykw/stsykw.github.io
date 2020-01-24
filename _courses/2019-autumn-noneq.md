---
title: "非平衡現象論"
collection: courses
type: "理学研究科宇宙地球科学専攻大学院科目"
permalink: /courses/2019-autumn-noneq
venue: "大阪大学, 理学部"
date: 2019-09-10
location: "Osaka, Japan"
---

大学院科目、金曜日2限、理F202教室



スケジュール
-----
**10月4日**  
非平衡現象とは。平衡近傍でのゆらぎ、Boltzmann-Einsteinの原理。最小仕事による表現

**10月11日**  
ゆらぎの動力学、Onsagerの相反定理

**10月18日**  
最小散逸の原理、Onsager係数の決定

**10月25日**  
Onsager-Machlup過程、例:ブラウン運動

**11月8日**  
ポテンシャルのある系のブラウン運動
線形応答: 古典系の静的な場合

**11月15日**  
線形応答: 量子系の静的な場合
線形応答: 動的な場合に向けて。Liouville動力学

**11月22日**  
線形応答: 摂動展開、静的な場合再び

**11月29日**  
線形応答: 複素アドミッタンスとエネルギー散逸、Kramers-Kronig関係、揺動散逸定理  

**12月6日**  
出張により休講の予定

**12月13日**  
ゆらぎの定理: 散逸ダイナミクス

**12月20日**  
ゆらぎの定理: ゆらぎの定理、Jarzynski等式

**1月10日**  
沙川さんの集中講義のため休講の予定

**1月24日**  
**1月31日**  
**2月7日**  


Quiz
----
**Quiz 1(10月4日出題)**  
マクロ量 \\( \\{ a_i \\} \\)の分布はエントロピーで支配される。
\\[
P(\\{ a_i \\} ) = \dfrac{1}{\mathcal{N}} \exp \left( \dfrac{1}{k_\mathrm{B}}  S(\\{a_i\\})\right)
\\]
このとき、指数関数の肩を平衡状態のマクロ量\\( \\{ \overline{a_i} \\} \\)からのずれで展開して、
\\[
P(\\{a_i\\}) = (2\pi)^{-n/2} \left[ \det \left(
-\dfrac{1}{k_\mathrm{B}} \dfrac{\partial^2 S}{\partial a_i \partial a_j }
 \right)
 \right]^{1/2}
\exp \left(
\dfrac{1}{2 k_\mathrm{B}}
\sum_{ij} \dfrac{\partial^2 S}{\partial a_i \partial a_j} (a_i - \overline{a_i}) (a_j - \overline{a_j})
\right)
\\]
とかけることを示せ。

**Quiz 2(10月11日出題)**  
マクロ量 \\( \\{ a_i \\} \\)の分布
\\[
P(\\{a_i\\}) \propto
\exp \left(
-\dfrac{1}{2 }
\sum_{ij} A_{ij} a_i a_j
\right)
\\]
に対し、期待値 \\( \left\langle a_i a_j \right\rangle = A_{ij}^{-1}\\)となることを示せ。

**Quiz 3(10月18日出題)**  
Hall効果をDrudeモデルにより考察する。
電荷\\(q\\)をもつ質量\\(m\\)の荷電粒子が運動方程式
  \\[
  m \dfrac{d\mathbf{v}}{dt} = q \mathbf{E} + q \mathbf{v} \times
  \mathbf{B}- \gamma \mathbf{v}
  \\]
  に従うとする。ここで\\(\mathbf{E}, \mathbf{B}\\)はそれぞれ電場、
  磁場、\\(\gamma\\)は散逸を表す。
  電場、磁場が\\(\mathbf{E} = (E_x, E_y, 0) , \mathbf{B} = (0,0,B)\\)のとき、
  定常速度\\( (v_x, v_y) \\)を求め、電気伝導率テンソル\\( \sigma_{xx}, \sigma_{xy},\sigma_{yx},\sigma_{yy} \\)を
  \\begin{align}
v_x & = \sigma_{xx} E_x + \sigma_{xy} E_y \\\
v_y & = \sigma_{yx} E_x + \sigma_{yy} E_y
  \\end{align}
  で定義したとき、電気伝導率テンソル\\( \sigma_{xy} , \sigma_{yx} \\)に関してOnsagerの相反定理が成立していることを確認せよ。

**Quiz 4(10月25日出題)**  
ブラウン運動のLangevin表現、
\\[
  \dfrac{dp_i}{dt} = - \dfrac{f}{T_R M} p_i + \xi_i(t)
\\]
ただし\\(  \langle \xi_i(t) \rangle_{eq} = 0 \enspace , \quad \langle \xi_i(t) \xi_j (t') \rangle_{eq} = 2 k_\mathrm{B} f \delta_{ij} \delta (t-t') \\)に対して、
\\[
\langle p_i (t+\tau) p_j (t) \rangle_{p_i(0)=p_i^0, p_j(0)=p_j^0}
\\]
を計算せよ。また、初期値 \\( p_i^0, p_j^0 \\)を熱平衡にとり十分に時間が経った後の、
\\[
\langle p_i (t+\tau) p_j (t) \rangle_{eq} - \langle p_i (t+\tau) \rangle_{eq} \langle p_j (t) \rangle_{eq}
\\]
を計算せよ。

**Quiz 5(11月8日出題)**  
\\(L \times L \times L \\)の立方体中に\\( N \\)個の古典的な自由粒子が逆温度\\( \beta \\)の熱平衡状態として存在している。
この自由粒子の重心位置\\( \dfrac{1}{N} \langle \sum_i q_i^z \rangle \\)の重力に対する応答を
線形応答の範囲で調べよ。また、重力は立方体のある辺と平行なz軸負の向きにかかるとする。
この系では厳密な重心位置も評価できるので、線形応答の結果と比較せよ。

**Quiz 6(11月22日出題)**  
Quiz 4の相関関数を、Fokker-Plack方程式
\\[
 \dfrac{\partial P}{\partial t}
 = k_\mathrm{B} f \sum_i \dfrac{\partial^2 }{\partial p_i^2} P + \dfrac{f}{T_RM}\sum_i \dfrac{\partial }{\partial p_i} (p_i P)
\\]
を使って計算せよ。

**Quiz 7(11月22日出題)**  
ハミルトニアン\\(H\\)とのPoisson括弧で定義される\\( \mathcal{L}(\cdot) =\\{ \cdot, H\\}\\)
という線形微分演算子に対して、
平衡分布\\( f_{eq}\propto \exp -\beta H \\)が
\\[
\mathcal{L} f_{eq} = 0
\\]
となることを示せ。

**Quiz 8(12月13日出題)**  
能勢-Hoover動力学において、分布関数\\( f\\)の全微分が以下のようになることを示せ。
\\begin{align}
  \dfrac{d f{dt} & =
  \dfrac{\partial f}{\partial t}
  + \dot{p}_i \dfrac{\partial f}{\partial p_i}
  + \dot{q}_i \dfrac{\partial f}{\partial q_i}
  + \zeta \dfrac{\partial f{\partial \zeta}
  \\
  & = dN\zeta f_{NH}
\\end{align}
      
**Quiz 9(12月13日出題)**  
位相空間中のある領域\\( \mathcal{D}(t) \\)の体積のLagrange的な時間変化が、
    \\[
    \dfrac{dV(\Gamma(t))}{dt} =
    \int_{\mathcal{D}(t)} d\Gamma(t) \Lambda (\Gamma(t))
    \\]
    となることを示せ。ただし \\( \Lambda (\Gamma(t))
    = \sum_i \left(\dfrac{\partial \dot{q}_i }{\partial q_i }
    + \dfrac{\partial \dot{p}_i} {\partial p_i} \right) \\) である。

**Quiz 10(12月20日出題)**  
\\( f(x) \\) を下に凸な関数とする。\\(x\\)を確率変数として、Jensen不等式
\\[
 \langle f(x) \rangle \ge f(\langle x \rangle)
\\]
を示せ。


評価
---
期末レポート、およびQuizの解答状況(数問選んで、最後に提出)をみて総合的に判断する。


参考書、参考文献
-------------
一般的なこと
* S. R. de Groot and P. Mazur "Non-equilibrium Thermodynamics", Dover Publications
* 一柳正和「不可逆過程の物理」日本評論社
* 川崎恭治「非平衡と相転移-メソスケールの統計力学-」朝倉書店
* 早川尚男「非平衡統計力学」サイエンス社
* 北原和夫「非平衡系の統計力学」岩波書店
* 鈴木増雄「統計力学、岩波講座現代の物理学」岩波書店
* 戸田盛和、久保亮五、斎藤信彦、橋爪夏樹「統計物理学、現代物理学の基礎第二版」岩波書店

Einsteinのゆらぎの理論
* L. Landau, E. Lifshitz 「統計物理学 (下)」岩波書店, L. Landau, E. Lifshitz, "Statistical Physics (course of theoretical physics volume 5) Butterworth-Heinemann"
* A. Einstein, "Theorie der Opaleszenz von homogenen Flüssigkeiten und Flüssigkeitsgemischen in der Nähe des Kritischen Zustandes", Ann. der Phys. **33** (1910), pp. 1275-1298. 邦訳 アインシュタイン選集1、監修 湯川秀樹 翻訳 井上健、谷川安孝、中村誠太郎 共立出版(1971)

大偏差性
* 大野克嗣、["Large Deviation and Statistical Physics", Prog. Theor. Phys. Suppl. **99** (1989) 165.](https://doi.org/10.1143/PTPS.99.165)
* 大野克嗣、["Onsager's Principle from Large Deviation Point of View", Prog. Theor. Phys. **89** (1993) 973.](https://doi.org/10.1143/PTP.89.973)
* H. Touchette, ["The large deviation approach to statistical mechancis", arXiv:0804.0327](http://arxiv.org/abs/0804.0327)

Onsagerの相反定理、Onsager-Machlup過程
* L. Onsager, ["Reciprocal Relations in Irreversible Processes I", Phys. Rev. **37** (1931) 405.](http://prola.aps.org/abstract/PR/v37/i4/p405_1)
* L. Onsager, ["Reciprocal Relations in Irreversible Processes II", Phys. Rev. **38** (1931) 2265.](http://prola.aps.org/abstract/PR/v38/i12/p2265_1)
* 橋爪夏樹、["A Statistical Theory of Linear Dissipative Systems", Prog. Theor. Phys. **8** (1952) 461.](https://doi.org/10.1143/PTP/8.4.461)N. Hashitsume
* L. Onsager and S. Machlup, ["Fluctuations and Irreversible Processes", Phys. Rev. **91**, 1505, (1953).](http://prola.aps.org/abstract/PR/v91/i6/p1505_1)
* M. Ichiyanagi ["Variational principles of irreversible processes", Phys. Rep. **243**, 125,(1994)](http://www.sciencedirect.com/science/article/pii/0370157394900523)


ゆらぎの定理、Jarzynski等式
* D. J. Evans and  D. J. Searles, ["The Fluctuation Theorem"</a>, Adv. Phys. **51** (2002) 1529.](http://taylorandfrancis.metapress.com/index/GY5R6P9XX8RYVXGR.pdf)
* G. E. Crooks, ["Entropy production fluctuation theorem and
    the non equilibrium work relation for free energy
  differences", Phys. Rev. E **60**, 2721, (1999).]()
* C. Jarzynski, ["Nonequilibrium Equality for Free Energy
  Differences", Phys. Rev. Lett. **78**, 2690 (1997).]()
*  C. Jarzynski, ["Nonequilibrium  work theorem for a system strongly coupled to a thermal environment", J. Stat. Mech.: Theor. Exp. **P09005**, (2004).]()

未整理
* A. Einstein "Investigations on the theory of the Brownian movement", Dover
* M. Ichiyanagi, ["Conceptual developments of non-equilibrium statistical mechanics in the early days of Japan", Phys. Rep. **262** (1995) 227.](http://www.sciencedirect.com/science?_ob=MImg&_imagekey=B6TVP-3YF4GW9-6-2&_cdi=5540&_user=5735665&_orig=browse&_coverDate=11%2F30%2F1995&_sk=997379994&view=c&wchp=dGLzVlz-zSkWA&md5=eb16ad3f3147413c76cc65ec10af35e6&ie=/sdarticle.pdf)
* R. Kubo, M. Toda, and N. Hashitsume, "Statistical Physics II, Nonequilibirum Statistical Mechanics" Spinter-Verlag
* J. A. McLennan, "Introduction to Non-equilibrium Statistical Mechanics" Prentice-Hall
* 佐々真一「非平衡現象論」講義ノート
* 関本謙「ゆらぎのエネルギー論」岩波書店
* N. G. van Kampen, "Stochastic Processes in Physics and Chemistry", Elsevier
* D. N. Zubarev, "Nonequilibrium Statistical Thermodynamics", Consultants Bureau
* R. Zwanzig, "Nonequilibirum Statistical Mechanics", Oxford
