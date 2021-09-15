# -*- coding: utf-8 -*-
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/randomquote/")
def quote():
    quotes = [

{
       "quote":"おれは人間をやめるぞ！ジョジョ―――ッ！！","author":"ディオ・ブランドー"},
{
       "quote":"我がナチスの科学力はァァァァァァァアアア世界一ィィィイイイイ","author":"シュトロハイム"},
{
       "quote":"だが断る","author":"岸辺露伴"},
{
       "quote":"てめーの敗因は…たったひとつだぜ…DIO…たったひとつの単純な答えだ…『てめーは俺を怒らせた』","author":"空条承太郎"},
{
       "quote":"やったッ！！さすがディオ！おれたちにできない事を平然とやってのけるッ！そこにシビれる！あこがれるゥ！","author":"ディオの取り巻きの小僧"},
{
       "quote":"オラオラオラオラオラオラオラオラオラオラオラオラ","author":"空条承太郎"},
{
       "quote":"無駄無駄無駄無駄無駄無駄無駄無駄無駄無駄無駄無駄ァーーーッ","author":"DIO"},
{
       "quote":"ディオォォオオーーーーッ君がッ 泣くまで 殴るのをやめないッ！","author":"ジョナサン・ジョースター"},
{
       "quote":"貧弱！貧弱ゥ！","author":"ディオ・ブランドー"},
{
       "quote":"パパウパウパウ波紋カッタ―――ッ！！フヒィーン","author":"ジャイロ・Ａ・ツェペリ"},
{
       "quote":"「世界（ザ・ワールド）」ッ！時よ止まれ！","author":"DIO"},
{
       "quote":"落ちつくんだ『素数』を数えて落ちつくんだ…『素数』は１と自分の数でしか割ることのできない孤独な数字…わたしに勇気を与えてくれる","author":"エンリコ・プッチ"},
{
       "quote":"逃げるんだよォ！","author":"ジョセフ・ジョースター"},
{
       "quote":"ハッピーうれピーよろピくねーーー","author":"ジョセフ・ジョースター"},
{
       "quote":"やれやれだぜ","author":"空条承太郎"},
{
       "quote":"レロレロレロレロ","author":"花京院典明"},
{
       "quote":"『銃は剣よりも強し』ンッン～ 名言だな これは","author":"ホル・ホース"},
{
       "quote":"『正義（ジャスティス）』は勝つ！","author":"エンヤ婆"},
{
       "quote":"Hail 2 U!","author":"ジャッジメント"},
{
       "quote":"YES I AM!","author":"アヴドゥル"},
{
       "quote":"アリーヴェデルチ","author":"ブチャラティ"},
{
       "quote":"ディ・モールト","author":"メローネ"},
{
       "quote":"To Be Continued…","author":"（演出）"},
{
       "quote":"僕は本当の［紳士］をめざしているからだ！","author":"ジョナサン"},
{
       "quote":"人間讃歌は「勇気の讃歌」ッ!!人間のすばらしさは勇気のすばらしさ!!","author":"ツェペリ"},
{
       "quote":"おまえは今まで食ったパンの枚数をおぼえているのか？","author":"ディオ"},
{
       "quote":"ウィンウィンウィンウィン","author":"カーズ"},
{
       "quote":"ジョセフ・ジョースター！きさま！見ているなッ！","author":"DIO"},
{
       "quote":"忘れっぽいんでな、メモってたんだ…！","author":"空条承太郎"},
{
       "quote":"ロードローラーだッ！","author":"DIO"},
{
       "quote":"無敵の『スタープラチナ』でなんとかしてくださいよォーーー！","author":"東方仗助"},
{
       "quote":"これで今夜も………くつろいで熟睡できるな","author":"吉良吉影"},
{
       "quote":"このジョルノ・ジョバァーナには正しいと信じる夢がある","author":"ジョルノ・ジョバァーナ"},
{
       "quote":"この味は！………ウソをついてる『味』だぜ……","author":"ブチャラティ"},
{
       "quote":"あなた…『覚悟して来てる人』……ですよね。人を「始末」しようとするって事は、逆に「始末」されるかもしれないという危険を、常に『覚悟して来ている人』ってわけですよね…","author":"ジョルノ・ジョバァーナ"},
{
       "quote":"ジョルノ君だっけ？立ってるのも何だからここ座んなよ、お茶でも飲んで…話でもしようや………","author":"アバッキオ"},
{
       "quote":"良ぉお～～～～しよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしよしたいしたやつだ、セッコおまえは","author":"チョコラータ"},
{
       "quote":"オレのそばに近寄るなああーーーーッ","author":"ディアボロ"},
{
       "quote":"初めての相手はジョジョではないッ！このディオだッ！―――――ッ","author":"ディオ"},
{
       "quote":"ふるえるぞハート！燃えつきるほどヒート！！","author":"ジョナサン"},
{
       "quote":"これが運命なら、あるがまま受け入れよう","author":"ツェペリさん"},
{
       "quote":"猿が人間に追いつけるかーッ！お前はこのディオにとってのモンキーなんだよジョジョォォォーーーッ！！","author":"ディオ"},
{
       "quote":"あたしはテキーラ酒をもってまいりましたの～～ 通ってもよろしいかしら～～","author":"ジョセフ"},
{
       "quote":"マヌケッ！一目でわかるわーっ気持ち悪いーっお前みたいにでかくて筋肉質の女がいるかスカタン！客観的に自分を見れねーのかバーカ","author":"ナチス兵"},
{
       "quote":"JOJO、そのチェリー食べないのか？ ガッつくようだが、ぼくの好物なんだ.........くれないか？","author":"花京院典明"},
{
       "quote":"やかましいッ！うっおとしいぜッ！！おまえらッ！","author":"空条承太郎"},
{
       "quote":"最高に「ハイ！」ってやつだアアアアアアハハハハハハハハハハーッ","author":"DIO"},
{
       "quote":"スゲーッ爽やかな気分だぜ！新しいパンツをはいたばかりの正月元旦の朝のよーによォ～ッ","author":"東方仗助"},
{
       "quote":"『運命』に勝った！","author":"川尻早人"},
{
       "quote":"「ブッ殺す」と心の中で思ったならッ！その時スデに行動は終わっているんだッ！","author":"プロシュート兄貴"},
{
       "quote":"『任務は遂行する』『部下も守る』両方やらなくっちゃあならないってのが「幹部」のつらいところだな","author":"ブチャラティ"},
{
       "quote":"ミスタ…あなたの「覚悟」は…この登りゆく朝日よりも明るい輝きで『道』を照らしている。そして我々がこれから『向かうべき…正しい道』をもッ！","author":"ジョルノ"},
{
       "quote":"誰だろうと、わたしの永遠の絶頂をおびやかす者は許さない。決して。確実に消え去ってもらう","author":"ディアボロ"},
{
       "quote":"そうだな…　わたしは「結果」だけを求めてはいない。「結果」だけを求めていると、人は近道をしたがるものだ……近道をした時、真実を見失うかもしれない。やる気もしだいに失せていく。","author":"アバッキオの同僚警官"},
{
       "quote":"『帝王』はこのディアボロだッ！依然変わりなくッ！","author":"ディアボロ"},
{
       "quote":"終わりがないのが『終わり』それが『ゴールド・E（エクスペリエンス）・レクイエム』","author":"ジョルノ"},
{
       "quote":"去ってしまった者たちから受け継いだものは、さらに『先』に進めなくてはならない！！","author":"ジョルノ"},
{
       "quote":"おれは人間を超越するッ！ ジョジョ、おまえの血でだァ──ッ！","author":"ディオ"},
{
       "quote":"もしかしてオラオラですかーッ！？","author":"テレンス・T・ダービー"},
{
       "quote":"質問を質問で返すなあーっ！！疑問文には疑問文で答えろと学校で教えているのか？","author":"吉良吉影"},
{
       "quote":"てめー今確かに「吉良吉影」っつったよなぁー！！","author":"東方仗助"},
{
       "quote":"激しい「喜び」はいらない…そのかわり深い「絶望」もない……「植物の心」のような人生を…そんな「平穏な生活」こそ私の目標だったのに………","author":"吉良吉影"},
{
       "quote":"オレは『正しい』と思ったからやったんだ。後悔はない…こんな世界とはいえ、オレは自分の『信じられる道』を歩いていたい！」","author":"ブチャラティ"},
{
       "quote":"アバッキオ、おまえはりっぱにやったのだ。そしておまえの真実に「向かおうとする意志」は、あとの者たちが感じ取ってくれているさ","author":"アバッキオの同僚警官"},
{
       "quote":"さびしいよォォォォ…………ボス。いつものように、電話ください………… 待ってます…… 電　話","author":"ドッピオ"},
{
       "quote":"おれが最期にみせるのは、代々受け継いだ未来にたくす「ツェペリ魂」だ！「人間の魂」だ！","author":"シーザー"},
{
       "quote":"自動車か…　なかなかのパワーとスピードだ。このDIOが生まれた時代には、馬車しか走っていなかった…","author":"DIO"},
{
       "quote":"歩道が広いではないか…行け","author":"DIO"},
{
       "quote":"さ…………最後の……エメラルド・スプラッシュ…メ…ッセージ…で…す…これが…せい…いっぱい…ですジョースター…さん　受け取って…ください…伝わって………ください……","author":"花京院典明"},
{
       "quote":"なんていうか…その…下品なんですが…フフ…boki…しちゃいましてね…","author":"吉良吉影"}
]
    colors = [
  "#16a085",
  "#27ae60",
  "#2c3e50",
  "#f39c12",
  "#e74c3c",
  "#9b59b6",
  "#FB6964",
  "#342224",
  "#472E32",
  "#BDBB99",
  "#77B1A9",
  "#73A857"
]
    randomNumber1 = randint(0,len(quotes)-1)
    randomNumber2 = randint(0,len(colors)-1)
    quote = quotes[randomNumber1]["quote"]
    author = quotes[randomNumber1]["author"]
    color = colors[randomNumber2]
    return render_template('layout.html', **locals())

if __name__ == "__main__":
    app.run()
