from bible_parser import BibleParser, LineType

lines = [
    'MATE',
    '1',
    'Jesu Chrih Ei Sawnlam',
    '1Abraham ei capa, David tei capa, Jesu Chrih ei sawnlam kha cawla krakue. 2Abraham kha Isaac kei pai, Isaac kha Jacob pei pai, Jacob kha Judah awn a nautuei pai. 3Judah kha Perez awn Zerah ei pai, an nawi Tamar, Perez kha Hezron ei pai, Hezron kha Ram ei pai. 4Ram kha Amminadab pei pai, Amminadab kha Nahshon ei pai, Nahshon kha Salmon ei pai. 5Salmon kha Boaz ei pai, Rahab awn an ca, Boaz kha Obed tei pai, Ruth awn an ca, Obed kha Jesse ei pai la krakue.',
    '6Jesse kha Hrangpuei David tei pai la krakue. David kha Solomon ei pai, Uriah ei chru Bathsheba awn an ca la krakue. 7Solomon kha Rehoboam ei pai, Rehoboam kha Abijah ei pai, Abijah kha Asa ei pai. 8Asa kha Jehoshaphat tei pai la krakue. Jehoshaphat kha Joram ei pai, Joram kha Uzziah ei pai. 9Uzziah kha Jotham ei pai, Jotham kha Ahaz ei pai, Ahaz kha Hezekiah ei pai. 10Hezekiah kha Mannasseh ei pai, Manasseh kha Amawn ei pai, Amawn kha Josiah ei pai. 11Josiah kha Jeconiah awna nautuei pai, akhapoetta Babylon la tut hei u kue. 12Babylon la am tuh hei kawnna: Jeconiah kha Shealtial ei pai la tang ein Shealtial kha Zerubbabel nei pai. 13Zerubbable kha Abihud ei pai, Abihud kha Eliakim ei pai, Eliakim kha Azor ei pai, 14Azor kha Zadok ei pai, Zadok kha Achim ei pai, Achim kha Eliuk ei pai. 15Eliuk kha Eleazar ei pai, Eleazar kha Matthan ei pai, Matthan kha Jacob pei pai. 16Jacob kha Mary ei vaa Joseph pei pai, Ani ein Messiah la am sui Jesu cana kue. 17Abraham ei David hrila sawn hleili, David tei Babylon la tutoemnak hrila sawn hleili, tutoemnak Babylon ei Messiah hrila sawn hleili lawh kue.',
    'Jesu Chrih Ei Hminak',
    '18Jesu Chrih kha cawmueihla hmikue: Anawi Mary kha Joseph pei chru la, am beek poetta, atoengla oeh an awmpha ah Hmueichra Ciim awn pooi kue. 19Avaa Joseph kha chrang dueng la, akranak awn Mary ei thangthed tei oeh yahlue ein a rawk duem eila, ngaihtueh kue. 20Khanaphi khacawh a ngaihtueh poetta, Bawipa ei fanchrang ani ei mangah danglaw ein, David tei capa Joseph, Mary na chrunak eila oeh lue, hatulatiah Hmueichra Ciim awn ani ein amaw pooina kue a ti. 21Ani tongpa la cakom; a ming Jesu la na suiyei, hatulatiah ani ein a chrangtu khuui yei. 22Bawipa ein Sanghma awn a toektu avan tuboeih kuem kue. 23Boen u, nuta ciim pooikom, tongpa la ca ei, Ani Imanuel la, a ming sui u ei, khacawh ei asuilam kha Fanpuhri nim eppa awmkue tinak ni. 24Ippueng Joseph a letlawah, Bawipa ei Fanchrang ein a toek mueihla, Mary chruna kue. 25Khanaphi tongpa la oeh a capha ei chrueih, nuta ciim la ngoengsou kue.',
    '2',
    'Hmuhmat Tuei Beeknak',
    '1Judah ram Bethlehem khawah, Herod Hrangpuei la, akrapoetta Jesu hmi khoenkue. Hnilaw vang ei hmuhmattu Jerusalem la sutlaw u kue. 2Judahtuei Hrangpuei hawanum a hmi? Hatulatiah hnilaw vangah a aiisi kam hmuh ein ani beekei la kam law kue am ti. 3Herod Hrangpuei ein khacawh a yaak ah, Jerusalem khawchrang avan awn luehmaih u kue. 4Tairuetungtu avan awn chrang hmuei thukhoen tikkhit puengtu kruum hei ein ahawla Messiah hmi ei tila doed hei kue. 5Judah ram Bethlehem khawah hmi ei am ti, hatulatiah Sanghma ein cawmueih la ru kue: 6Judah ram Bethlehem khaw nangkha Judah kruem pueng toengpangtu khuiah, ayawi soeih la oeh na kra ei; hatulatiah nang ei khuiah Judah kruem pueng awm lawei, ani ein ka chrang Israeltu coei hei yei. 7Khanei Herod kha hmuhmattu khueu hei duem ein amni eila, ahawtipoetta adanglaw doed hei tueptuep kue. 8Khanei, "Bethlehem khawla ceit u na, amaw thana u na yap u, nam hmuhah, nih thenlaw bai u, keihaw ka ceitkom ani ka be ei," tiein tuei hei kue. 9Fanpuhri ei thu am ngaih kawnna ceit u ein hnilaw lamei am hmuh aiisi am hmaiah ceit ein amaw ei awmnak hmun am pha ah aiisi duei kue. 10Khacawh ei aiisi am hmuh baiah anuila yeikraihe u kue. 11Im khuila am luh ah, a nawi mary awn amaw hmuh u ein koop u ein ani beh u kue. Khanei am khawhtu hmong u ein hrui, frankincense, myrrh, peekduentu am peek. 12Herod teila oeh am latbai yeila Fanpuhri ein mangah mana hei ein afei lam awn am khaw la lat u kue.',
    'Egypt La Dawngnak',
    '13Am ceh konna, Fanpuhri ei fanchrang Joseph pei mangah danglaw ein a toek, boen, thouna amaw awn a nawi la na, Egypt la dawng, oeh kan then ei chrueih akhala awm u; hatulatiah Herod tein a ngon eila, amaw yap law ei tikue.',
    '14Khatiein Joseph thou ein amaw awn anawi la ein than khuiah Egypt la dawng u kue. 15Herod a sih hrila, akhala awm u kue. Cawhkha Egypt khaw lamei ka ca, ka khue bai tila, Bawipa ein Sanghma awn a toek kuempueng la krakue.',
    'Herod Tei Amaw Ngonnak',
    '16Khanei hmuhmattu ein am theinak, Herod tein hmat ein akawthehe kue, hmuhmat tuei la niin hmat ein Jerusalem awn ayungkeu tveei kumhnih awn akai yei amaw tongpa avan ngon eila chrang tuei kue. 17Sanghma Jeremiah awn a toek kuem kue. 18Ramah khawah anui la oe hngoek nak awn kiunak awi nim yak, a catuei hmokla Rachel kiu ein a lungsin oeh dip hlot kue, hatulatiah a catu oeh awm u kue.',
    'Nazareth Khawla Latnak',
    '19Khanaphi Herod a sih ah, Egypt ram ah awmpueng Joseph pei mangah Bawipa ei fanchrang hmuh ein. 20Thouna, amaw awn anawi lana Israel ram la ceit; hatulatiah amaw ei hringnak yappueng sikhoen kue a ti. 21Khatiein Joseph thou ein amaw awn anawi la ein Israel ramla ceit kue. 22Khanaphi Archelaus kha, a pai yei hungah Judah ram kruemkue ti a yakah, akhala a ceh eila krih ein a mangah Fanpuhri ein taih ein Kalile ram la ceit kue. 23Nazareth la am sui yei khaw la ceit ein awm kue, Nazareth chrangla sui u ei tila Sanghma awn toek ei thu kuem kue.',
    'Mark',
    '1',
    'Johan Ei Thuthang Toeknak',
    '1Fanpuhri ei ca Jesu Chrih ei thuthang atuennak la kra kue. 2Cawhkha Sanghma Isaiah ei rukla kra kue: Boen noe, na hmailah ka thoei ka tueikue, hauein namlam prangtham mei. 3Prong khuilamei vikoikha, bawipa ei lam soemphran u, a lamtu duengsak u a ti mueihla; 4Prong khuila baptisma Johan danglawein, Katnak ngaihsim mei hmokla, yutnak baptisma ei mawng toek kue. 5Jerusalem chrangtu avan awn Judah rammei chrangavan, aniei la ceit u kue; Am kattu yut u ein, Jordan tuinu khuiah, ani ein baptisma pehei kue. 6Johan kha kalauk muei awn tah suisa ein, a cawiah mehvuen thomrui awn pin ein khangkhip awn khoilutui singkha a buh la kra kue. 7Atoektah lawkha, ka hnulah law pueng kha keilah khuetngai kue, aniei khawdawk rui kawppah phrannei hawla oeh ka hawi kue. 8Tui awn baptisma kan pe u ei; ani ein Hmueichra Ciim awn baptisma nipe u ei.',
    'Jesu Baptisma Hmuhnak',
    '9Akhapoetta Jordan tuinuah Johan nein baptisma a pek keila, Kalile ram Nazareth khawei ka Jesu lawh kue. 10Tui khuiyei ka lawhrit ein, fankhaw ahmongkru hmuh ein muem awn toeng pueng Hmueichra aniei fannah culawkue. 11Nangkha ka yawngnak capala nakra ein, kan yeinaklah na kra kue tila fan la mei oilaw kue. 12Hmueichra Ciim mein khawprong khuila cehpuei hrit kue. 13Khawram mein khawprong khuila hnueplikip ah sueksaw kue.',
    'Kalile Ah Jesu Thutoek',
    '14Thongkhuila Jesu a sutkonnah, kalile khawla Jesu lawein Fanpuhri ei thuthang toek kue.  15Nin kuem khoen kue, Fanpuhri ei ram etkhoen kue; yutuna thuthang yum u a ti. 16Kalile tuilikengah a ceh hnuiah, tuiliah vai an voih Saimon koeinau, Saimon awn Andrew hmuh rawi kue, anni kha ngayap chranglah kra nih kue. 17Jesu ein, nigui nih, chrangpanglah kan krasak nih ei. 18An vaitu rawk nih ein hruigit nih kue. 19Asoeng ceit u ein, zebede ei a ca James awn a nau Johan kongkhuiah vaitu am prangah hmuh heikue. 20Khue rawi hrit ein Kong fannah om u pueg, an pai zebede awn am vah saitu cehta nih ein, a hnuhrui hrit nih kue.',
    'Jesu Ein Khawram Atuh',
    '21Kapernaum khawla ceit u ein, chring hnuep baiah Sinakok khuiah Jesu ein theihei hrit kue.   22A thei hei ah coei u kue, hatulatiah anikha thukhoen tikkhik pueng mueihla oehkra ein huham tapueng mueihla thei hei kue. 23Am sinakok ah raithe ei omnak chrangapum omlaw palai ein; vik kue. 24Nazareth khawchrang Jesu kei mih hatu nanti na u eilanum? nalaw? nan di u eila ne? a ti. Fanpuhri ei chrang cim! la nakra kam hmatkue a ti. 25Jesu ein duemlaom, aniei khuiyei lutlaw tiein a tam. 26Raithe ein ani tuengtangsak ein vikowow ein aniei khuiyei ka lutlaw kue. 27Avan coeiboeih u ein, huham awn athaila theithang kha, hatunum? Raithe haw ein a toek ngai kue, tilah am mah cengcawek u kue. 28Ani ei mawng thuthang kha, kalile ram yung keu hmunpoeng avannah pueipawng kue.',
    'Chrangtu Acangsak',
    '29Sinakok khuiyei am lawkonnah, Saimon awn Andrew miei imlah Jame awn Johan awn ceithrit u kue. 30Saimon nei a koi hnatein yoenkue; ani ei mawng Jesu am thengit. 31Ani lawein nuta ei kut a yoek ei, nuta hnattein chrah ein, yinlei na kue. 32Khawmue lawein, khawkrak konnah, ani eila hnat pueng avan awn khawram mei a omnaktu lawpuei u kue. 33Khawchrang avan kawttah bum u kue. 34Neh ahaha awn hnat u pueng avan cangsak ein. Raitu tut hei kue; ani am hmatnak awn, khawramtu oeh thusak hei kue.',
    'Asiunak Ah Jesu Tairuenak',
    '35Khawathan hnui, khowngoisik ah, Jesu thouein, immei chrahkru kue, asiunak hmunla ceitein, akhala tairue kue. 36Saimon awn a pueitu ein ani yap u kue. 37Am hmuhah, avan nein niyap u kue amti. 38Khaw awn a et nak ahawla aw nim ceitte, khanavah thu katoek hlottei, khacawh ei hmokla ka law pueng a tinak hei. 39Kalile ram ayung ngei am Sinakok khuiah, thei hei ein, raithe tu tut hei kue.',
    'Phaineh Acimsak',
    '40Jesu eilah phai neh pueng lawein, a hmaiah khudong ein a panak, na yakhlue ei sueah, nan cimsak hning kue a ti. 41Rennak lungsin awn, Jesu ein a kutsoeng ein a sun, cimmoe, ka yahlue kue a ti. 42Ahritla phai yein chrah ein, ani cimkue. 43Ahlangla na ngaihnak kei tina ein afeila a tueih. 44Boennoe, hauphih oeh na thennei, a tinak; khanaphi ceitna, tairue eila vaw hmuhkru, moses ei toek mueihla, na ciim am hmattei la peta. 45Khanaphi ceitein a toeknak awn yungkeu ah thang ein pueikue, khatiein khaw khui ah Jesu adangla oeh ceitcawn baikue, pungim mah omein hmunpoeng ngei chrangtu ani ei la lawh u kue.',
    '2 TIMOTHY',
    '1',
    '1Jesu Chrih ah awm pueng thukam awn hring ngeila, Fanpuhri ei yakhlue awn Jesu Chrih ei thoeila kra pueng kei Pawluh ein. 2Nim Bawipa Jesu Chrih awn pai Fanpuhri ei lamei, dimdeihnak, rennak, boekhoeknak tu: ka yongnak capa Timothy ah awm  seh.',
    'Betak Keilah Thapeknak',
    '3Ka pupaituei am bi mueihla, lungsin ciim awn a bi ka bipeek Fanpuhri ka boena doei kue, hnuep awn than ka taiirueah nangmih kan thuemloet u kue. 4Na mikphritui ka thuembaiah, yeinak awn ka biei hmokla, na muei kan hmuhlue ein kan omdamna kue. 5Na pei lois awn na nawi Eunice ah omma pueng, yumnak a tang nangah a awm ka thuem ein, khacawh nangah awmkue tila ka hmatkhai kue. 6Khatiein cawhei mawngah na fanna kut ka taihnak awn Fanpuhri ei pekduen ahuentat baiyeilah ngaihna oe. 7Hatulatiah Fanpuhri ein krihnak Hmueichra oeh nipe u ein, huham awn yongnak awn ningcang tu ni an peek u.',
    'Thuthang Hmok Oeh Kri',
    '8Khatiein Aniei hamla thong ka krum awn nim Bawipa ei thuthang hmatsak nak ah oeh yak u, Fanpuhri ei huham awn thuthangni hamla khuikha nak ni hmuh puei u. 9Ni khui u ein, aciimla hringom meila an khue uh kha, nim bilawh la oeh kra ein, aruempueiah a mah ei ngaihtueh ein a boenak awn Jesu Chrih ah an peek uh ni. 10Khacawh ei boenak kha ni khui u pueng Jesu Chrih adanglaw nak awn tuboeih ah poeulaw kue. Ani ein sihnak phreh ein thuthangni awn hringnak awn aloet vang nak khuila ni cehpuei u kue. 11Khacawh ei hmokla kei, tikkhik peung awn thoei awn thutoek puenglah ni som  kue. 12Khacawh ei hmokla khaw vuuk khuikha ka hmuh, khanaphi oeh ka yak ein; hatulatiah hau ka yum ka hmat ein, khacawh ei hnuep hrila, a ni ka ap, ngoeng hning ngeila ka uepna ein, ani ka hmat ein ka yum kue.',
    'Yumnak Ah Betaknak',
    '13Jesu Chrih ah awm pueng yumnak awn yongnak awn kei ah nam yak thutangtu nuetnak lah nam taak toeih ei. 14Nangah kan appei khawh, nim khuiah awm pueng Hmueichra Ciim awn, ngoengsou voe. 15A kratang na hmat mueihla Asia rammei a van nein ni cehta u ein, am ni khuiah Phygelus awn Hermogenes thumnih kue. 16Bawipa ein Onesiphorus imkhuiah rennak pese, hatulatiah a ni ein ni thoeuyau sak ciein, sirui awn an khih uh lah oeh yak kue. 17Rom khawah a ompoetta thanna ein ni yap ein ni hmulaw kue. 18Khacawh ei hnueppa Bawipa ei lamei rennak a hmuh eila Bawipa ein ani pese! Efisa khawah hatukruk la kei an bom a vehla nam hmat kue.',
]


def get_parsed():
    bp = BibleParser('lang')
    for line in lines:
        bp.process(line)
    return bp


def test_create_bible():
    language = 'Kaang Chin'
    bp = BibleParser(language)
    assert bp.bible.language == language
    assert bp.last_line == None
    assert bp.last_line_type == None
    assert bp.current_book = None


def test_line_classification():
    test_cases = {
        '3': LineType.number,
        'Jesu Ei Nethe Ciimsak': LineType.text,
        '2THESALONI': LineType.text,
        '2 TIMOTHY': LineType.text,
        "15Tovuen buengkom nang eila law pueng sanghma loitu ngaihna u, khanaphi akhuila thekha pueng hetu la kra kue. 16Am theihtu awn nam hmat hei yei. Hlingbum ah pucueng theih bit khoi u aw?, Hlingsingah theitheih bitkhoi u aw? 17Khatiein singveh poeng aveh la thei kue, khanaphi singthe poeng athela thei kue. 18Singveh athe la oeh thei hning ei, singthe aveh la oeh thei hning ei. 19Singpoeng aveh la oeh thei pueng tukpitta mei khuila fih ei. 20Khatiein am theih tu awn nam hmat hei yei.": LineType.numbered_text
    }

    for line_text, line_type in test_cases.items():
        bp = BibleParser('language')
        assert bp.classify(line_text) == line_type


def test_parsing_books():

    bp = get_parsed()

    bible = bp.build()

    assert len(bp.bible.chapters) == 3
    assert bp.bible.chapter[0].name == 'MATE'
    assert len(bp.bible.chapter[0].chapters) == 2
    assert bp.bible.chapter[1].name == 'Mark'
    assert len(bp.bible.chapter[1].chapters) == 1
    assert bp.bible.chapter[2].name == '2 TIMOTHY'
    assert len(bp.bible.chapter[2].chapters) == 1
