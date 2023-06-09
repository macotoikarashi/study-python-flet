import asyncio,random

async def returnDialogue(keywords="Ghost,High school"):
    await asyncio.sleep(10)
    return """
    {
  "dialogue": [
    {
      "speaker": "Emily",
      "content": [
        "I can't believe it's been five years since high school.",
        "Do you remember that haunted house on Oak Street?"
      ]
    },
    {
      "speaker": "Ben",
      "content": [
        "Of course I do. The one they said was haunted by a ghost.",
        "But come on, it was just an urban legend, right?"
      ]
    },
    {
      "speaker": "Emily",
      "content": [
        "I'm not so sure anymore. I went back there last night.",
        "I saw something... someone."
      ]
    },
    {
      "speaker": "Ben",
      "content": [
        "Wait, are you serious? What did you see?",
        "Tell me everything."
      ]
    },
    {
      "speaker": "Emily",
      "content": [
        "It was a ghost, Ben. I know it sounds crazy,",
        "but I saw a transparent figure walking through the walls."
      ]
    },
    {
      "speaker": "Ben",
      "content": [
        "This is insane. We have to investigate this together.",
        "If there's really a ghost, we need to find out who it is."
      ]
    }
  ],
  "status": {
    "situation": "Emily and Ben, former high school friends, reunite after five years.",
    "characters": [
      {
        "name": "Emily",
        "description": "A curious and adventurous young woman who believes in the supernatural."
      },
      {
        "name": "Ben",
        "description": "A skeptical and logical guy who relies on facts and evidence."
      }
    ]
  }
}
    """

async def returnJapanese(jsontext="..."):
    await asyncio.sleep(5)
    return """
    {
"dialogue": [
{
"speaker": "Emily",
"content": [
"高校から5年経つなんて信じられないわ。",
"オークストリートにあったあのお化け屋敷覚えてる？"
]
},
{
"speaker": "Ben",
"content": [
"もちろん覚えてるよ。幽霊が出るって言われてたあの場所だろ？",
"でもさ、それって都市伝説だろ？"
]
},
{
"speaker": "Emily",
"content": [
"もうよくわからないわ。昨晩、そこに戻ってきたの。",
"何かを見たの…誰かを。"
]
},
{
"speaker": "Ben",
"content": [
"待って、マジで？何を見たの？",
"全部教えてよ。"
]
},
{
"speaker": "Emily",
"content": [
"幽霊だったわ、Ben。信じられないかもしれないけど、",
"壁を通り抜けて歩いている透明な姿を見たの。"
]
},
{
"speaker": "Ben",
"content": [
"これは狂気だ。一緒に調査しなければならない。",
"もし本当に幽霊がいるなら、その正体を突き止めないといけない。"
]
}
]
}
    """

async def returnEvaluation(situation="..",question="...", correctEx="....", answer="....."):
    await asyncio.sleep(8)
    return """
{
  "isgood": true,
  "evaluate": "あなたの翻訳は正しいです。この文脈では、「Do you remember the haunted house that used to be at Oak Street?」という表現が適切です。EmilyとBenは高校の友人であり、5年ぶりに再会した状況です。そのため、相手がオークストリートにあったお化け屋敷を覚えているかどうかを尋ねるのが適切です。あなたの翻訳と正解例との違いは微妙ですが、ニュアンス的にはほとんど変わりません。素晴らしい翻訳ですね!"
}
    """

def randomKeywords(n):
    kws = ['Impala', '天井', 'Yodel', 'カーペット', '鳥籠', 'ラップトップ', 'Grapes', '雨具', 'イチゴ', '紅茶', 'Jungle', 'バスタオル', 'Sloth', '虹', 'コーヒー', '鉄', 'Panda', 'Kilogram', 'Maracas', 'バラ', '扉', 'ココア', 'Yucca', '日差し', 'Asteroid', '電話', 'ノート', '火花', '森林', 'Zinnia', 'Walrus', 'スプーン', 'アイスクリーム', '花火', 'キャンプ', 'レモン', 'Waffle', '春', '飛行船', 'ファイル', 'Ultraviolet', 'Orchid', 'Weasel', 'シューズ', 'クレヨン', '時間', '天使', 'Zodiac', 'Molecule', 'Eggplant', 'Kettle', '足跡', '海岸線', 'Watermelon', 'Coconut', 'Unicorn', 'Juggler', '本棚', 'Pineapple', 'Butterfly', 'Raspberry', 'リース', 'Quilt', 'Galaxy', 'サラダ', '椅子', 'ネックレス', 'ハンガー', 'バスケット', 'Otter', '霧', '水滴', 'ナッツ', 'Lion', 'Ninja', '冷蔵庫', '壷', '塔', '朝日', 'エコー', 'ブランコ', 'メモ', 'Elephant', 'Kiwi', 'Goose', 'パンダ', '鳥', 'Volcano', 'ヘリコプター', 'フォーク', 'イルカ', 'スプレー', 'アンテナ', 'Ostrich', 'Beetle', 'Leopard', 'Kettlebell', 'ベッド', 'Tambourine', '台所', 'リボン', 'Kangaroo', 'Ocelot', 'ポット', '皿', 'Hawk', 'Mitten', '貝殻', 'Jumper', 'Tuna', 'Gecko', 'ベーグル', '砂糖', 'バレンタイン', 'メロディ', 'Jacket', 'Iguana', 'テーブル', 'Lemon', 'Yew', 'Yo-yo', '塀', 'コミック', 'Uranus', 'Balloon', 'Lighthouse', 'ハイビスカス', 'ピザ', 'ソファ', 'Yacht', 'Koala', 'スパゲティ', 'トレッドミル', '錠前', 'Zeppelin', 'Lynx', 'Urchin', 'シャンプー', 'Rainbow', '夏', 'Cherry', 'Pomegranate', 'スパイス', 'ユニコーン', 'Iceberg', 'シロップ', 'ワイン', '飛行機', 'デッキ', 'Shark', '家族', '風見鶏', '雲', 'Zephyr', '新聞', '鉛筆', '栗', '石像', '雪', 'Lamp', '遊園地', 'Banjo', 'Hedgehog', '森', 'ライオン', 'Vulture', 'Donkey', 'イヤリング', 'Goldfish', 'クリスマス', 'Rooster', '燭台', '蝶', 'Robot', '網戸', '海', 'Zucchini', 'Lychee', 'Velociraptor', 'Zoo', 'ハンバーガー', 'Island', 'Apple', 'ビスケット', 'Hummingbird', '妖精', 'Raven', '風', 'Yam', 'Squirrel', 'Rose', '雪だるま', 'Orange', 'ベンチ', 'Carrot', 'Ice', 'エレベーター', 'Jasmine', 'Parrot', 'パスポート', 'Toucan', 'Violin', '水晶球', 'Lark', 'Cello', '花', 'ブロッコリー', 'ハイキング', 'Raccoon', 'Icicle', 'オリーブオイル', '昼寝', 'トランペット', '靴下', 'Turtle', 'Guava', 'Antelope', 'ドアノブ', '指', '雪景色', '絨毯', 'ドレッシング', 'Jalapeno', 'Dolphin', 'テーブルクロス', '塩', 'Racoon', 'Spaceship', 'サングラス', '蛍', '桟橋', 'おもちゃ', 'Bison', 'アワビ', 'Quasar', 'ボート', 'Satellite', 'クッキー', 'Blueberry', 'ピクニック', 'ピアノ', '八角', 'レンガ', '蝋燭', 'ハンモック', '蛍光灯', 'ウェーブ', 'Olive', '日傘', 'Lemur', 'Heron', '砂漠', 'Rabbit', 'Xylophone', '部屋', '犬', 'Nun', 'Lizard', 'Jazz', 'ボールペン', 'ガーデン', 'Lemonade', '野球', 'Rocket', 'Orangutan', 'Noodle', 'リモコン', '寝具', '火山', '梨', 'Tangerine', 'Kumquat', 'Lilac', 'Cactus', 'ヨーグルト', 'キノコ', '遊び場', 'Yak', '絆創膏', 'Mango', 'ひまわり', 'ガラス', 'Licorice', '月面', 'Strawberry', 'Ox', 'ゴミ箱', 'Tulip', 'Tricycle', '音符', 'ビーチボール', '茶碗', '花瓶', 'Ukulele', 'ピラミッド', 'バレーボール', 'Octopus', '冬', '火', 'Mandolin', 'パンプキン', 'ハロウィン', 'プラスチック', 'ペンダント', 'ソーダ', 'Tiger', '窓', 'Walnut', 'バタフライノット', '川', 'Lantern', 'Hyena', '猫', 'Telescope', 'Lute', '雪原', 'トンネル', '廊下', '風船', '蛸', 'スクリュー', 'Moth', 'Ladder', '天窓', '水玉', 'Pillow', '音楽', 'Giraffe', 'タクシー', 'Nectarine', 'ビーチ', 'Flamingo', 'アクアリウム', '星座', 'Zebra', 'Penguin', 'ボール', 'Hippopotamus', 'Circus', 'Gorilla', 'シャワー', 'Gazelle', '夕焼け', 'レコード', 'インク', 'スケートボード', 'Yoga', 'Harmonica', '冬眠', 'ベル', '赤ちゃん', '電球', '鏡', '泥棒', 'ペン', 'Oyster', '紙飛行機', 'リンゴ', '魚', 'Nebula', 'Ogre', 'Jigsaw', 'Nimbus', 'マグネット', '雲海', 'Lobster', 'Banana', '魔法使い', 'Vase', 'Venus', '紙', 'Vanilla', 'カップ', 'Rattlesnake', 'Kitten', 'Hippo', 'Viking', '石鹸', '扇風機', '歯ブラシ', 'Wolf', 'シャベル', 'Topaz', 'ハチ', 'ブラシ', '宝石', 'Binoculars', 'Eagle', 'ビーズ', 'Accordion', 'Dinosaur', 'フェンス', 'キツネ', 'パン', 'ティーポット', 'ドラム', 'サンドイッチ', 'ギター', 'Umbrella', 'トースト', 'ピアス', 'コート', 'Yeti', 'コイン', 'ダンボール', 'Iris', 'チーズ', 'Jellyfish', 'Grapefruit', 'Saxophone', '鍵', '帽子', 'Peach', 'Jade', 'Vampire', '雨', 'Osprey', '帯', 'Narwhal', 'Guitar', 'エプロン', '煙突', 'ハンドル', '葉', '蝶々', 'Yardstick', '星', 'タオル', 'Navigator', '木', 'Rhinoceros']
    rndkws = random.sample(kws,n)
    return rndkws



if __name__=="__main__":
    print(returnDialogue())
    print(returnJapanese())
    print(returnEvaluation())