from __future__ import unicode_literals

STOP_WORDS = set("""
adiakopa ai akoma akomi akrivos akrivws alla alles alli allh allin allhn allhna
allis allhs allo alloi allos allote allou
allios alliws alloios alloiws
alliotika alliwtika alloiotika alloiwtika
allous allon allwn ama amesa amesos an ana anamesa anametaxy anametaxi anef anti antipera antis
ano anw ap apenanti apo apopse ara arage arketa arketes
arxika as avrio afta aftes afti aftin aftis afto aftoi afton aftos aftou aftous
afton afotou afou
bebaia bebaiotata
vevaia vevaiotata
gi gia giati grigora gyro guro
de den dexia dithen di8en diladi dhladh dia diarkos diarkws dika diko dikoi dikos dikou
dikous diolou dipla dixos
ean eauto eauton eautou eautous egkaira egkairos ego egw edo edw eimai
eimaste einai eis eisai eisaste eiste eite eixa eixame eixan eixate eixe eixes
ekei ekeina ekeines ekeini ekestop_words = STOP_WORDSinin ekeinis ekeino ekeinoi ekeinon ekeinos ekeinou
ekeinous ekeinon ektos emas emeis emena empros en ena enan enas enos entelos entelws entos
""".split())

# enantion  exis  exaitias  epipleon epomeni entometaxy eno ex exafna exis exisou exo epano epanw
# epeidi epeita epi episis epomenos esas eseis esena esto esy etera eterai eteras eteres 
# eteri eteris etero eteroi eteron eteros eterou eterous eteron etouta etoutes etouti etoutin 
# etoutis etouto etoutoi etouton etoutos etoutou etoutous etouton etsi evge efthys eftychos efexis 
# echei echeis echete echome echoume echoun echtes echo eos eginan  egine  ekane  exi  echontas
# i idi imastan imaste imoun isastan isaste isoun itan itane itoi itton
# tha
# i idia idia idian idias idies idio idioi idion idios idios idiou idious idion idios ii iii
# isame isia isos
# kathe kathemia kathemias kathena kathenas kathenos katheti katholou kathos kai kaka kakos kala
# kalos kamia kamian kamias kamposa kamposes kamposi kamposin kamposis kamposo kamposoi
# kamposon kamposos kamposou kamposous kamposon kaneis kanen kanena kanenan kanenas
# kanenos kapoia kapoian kapoias kapoies kapoio kapoioi kapoion kapoios kapoiou kapoious
# kapoion kapote kapou kapos kat kata kati katiti katopin kato kiolas klp konta ktl kyrios
# ligaki ligo ligotero logo loipa loipon
# ma mazi makari makrya malista mallon mas me methavrio meion melei melletai memias men
# merika merikes merikoi merikous merikon mesa met meta metaxy mechri mi mide min mipos
# mite mia mian mias molis molonoti monacha mones moni monin monis mono monoi monomias
# monos monou monous monon mou borei boroun bros meso  mia  meso
# na nai noris
# 3ana ksana 3afnika ksafnika
# o oi ola oles oli olin olis olo ologyra oloi olon olonen olos olotela olou olous olon
# olos olosdiolou omos opoia opoiadipote opoian opoiandipote opoias opoios opoiasdipote opoidipote
# opoies opoiesdipote opoio opoiodiipote opoioi opoion opoiondipote opoios opoiosdipote
# opoiou opoioudipote opoious opoiousdipote opoion opoiondipote opote opotedipote opou
# opoudipote opos orismena orismenes orismenon orismenos osa osadipote oses osesdipote
# osi osidipote osin osindipote osis osisdipote oso osodipote osoi osoidipote oson osondipote
# osos ososdipote osou osoudipote osous osousdipote oson osondipote otan oti otidipote
# otou ou oude oute ochi opoia  opoies  opoio  opoioi  opote  os
# pano  para  peri  polla  polles  polloi  pollous  pou  prota  protes  proti  proto  protos  pos
# pali panta pantote pantou pantos para pera peri peripou perissotero persi perysi pia pithanon
# pio piso plai pleon plin poia poian poias poies poio poioi poion poios poiou poious
# poion poly poses posi posin posis posoi posos posous pote pote pou pouthe pouthena prepei
# prin pro prokeimenou prokeitai propersi pros protou prochthes prochtes protytera pos
# san sas se seis sou sta sti stin stis stis sto ston stou stous ston sygchronos
# syn synama synepos sychnas sychnes sychni sychnin sychnis sychno sychnoi sychnon
# syxnos syxnws sychnou sychnous sychnon sychnos schedon
# ta tade tafta taftes tafti taftin taftis taftotafton taftos taftou tafton tacha tachate
# teleftaia  teleftaio  teleftaios  tou  tria  triti  treis telika telikos tes tetoia tetoian 
# tetoias tetoies tetoio tetoioi tetoion tetoios tetoiou
# tetoious tetoion ti tin tis ti tipota tipote tis to toi ton tos tosa toses tosi tosin
# tosis toso tosoi toson tosos tosou tosous toson tote tou toulachisto toulachiston tous tous touta
# toutes touti toutin toutis touto toutoi toutois touton toutos toutou toutous touton tychon
# ton tora
# yp yper ypo ypopsi ypopsin ystera
# xoris xorista
# xwris xwrista
# choris chorista
# o os osan osotou ospou oste ostoso och
