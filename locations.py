#!/usr/bin/python3
loc_dict = {
  "\"#vothL336\"": "\"Algiers\"",
  "\"#vothL517\"": "\"Ghardaïa\"",
  "\"#vothL319\"": "\"Buenos Aires\"",
  "\"#vothL1\"": "\"Wien\"",
  "\"#vothL2\"": "\"Mistelbach\"",
  "\"#vothL3\"": "\"Trofaiach\"",
  "\"#vothL4\"": "\"Judenburg\"",
  "\"#vothL5\"": "\"Linz\"",
  "\"#vothL9\"": "\"Gabersdorf\"",
  "\"#vothL171\"": "\"Mauthausen\"",
  "\"#vothL355\"": "\"Herzogenburg\"",
  "\"#vothL419\"": "\"Bludenz\"",
  "\"#vothL426\"": "\"Salzburg\"",
  "\"#vothL427\"": "\"Innsbruck\"",
  "\"#vothL430\"": "\"Bregenz\"",
  "\"#vothL455\"": "\"Enns\"",
  "\"#vothL479\"": "\"Deutschkreuz\"",
  "\"#vothL482\"": "\"Braunau am Inn\"",
  "\"#vothL585\"": "\"Glasenbach\"",
  "\"#vothL592\"": "\"Villach\"",
  "\"#vothL614\"": "\"Feldkirch\"",
  "\"#vothL390\"": "\"Baku\"",
  "\"#vothL6\"": "\"Pinsk\"",
  "\"#vothL7\"": "\"Slonim\"",
  "\"#vothL398\"": "\"Baranovichi\"",
  "\"#vothL433\"": "\"Minsk\"",
  "\"#vothL434\"": "\"Chervyen’ \"",
  "\"#vothL471\"": "\"Lyntupy\"",
  "\"#vothL472\"": "\"Shudovtsy\"",
  "\"#vothL478\"": "\"Zharki\"",
  "\"#vothL508\"": "\"Brest\"",
  "\"#vothL528\"": "\"Vawkavysk\"",
  "\"#vothL146\"": "\"Antwerp\"",
  "\"#vothL264\"": "\"Namur\"",
  "\"#vothL266\"": "\"Philippeville\"",
  "\"#vothL327\"": "\"Brussels\"",
  "\"#vothL414\"": "\"Rio de Janeiro\"",
  "\"#vothL8\"": "\"Santiago\"",
  "\"#vothL384\"": "\"Temuco\"",
  "\"#vothL546\"": "\"Osorno\"",
  "\"#vothL386\"": "\"Shanghai\"",
  "\"#vothL418\"": "\"Doubrava\"",
  "\"#vothL421\"": "\"Mariánské Lázně\"",
  "\"#vothL473\"": "\"Karviná\"",
  "\"#vothL10\"": "\"Chynadiyovo\"",
  "\"#vothL50\"": "\"Terezín\"",
  "\"#vothL71\"": "\"Mukacheve\"",
  "\"#vothL157\"": "\"Niznii Verezky\"",
  "\"#vothL161\"": "\"Solotvyno\"",
  "\"#vothL227\"": "\"Vyhne\"",
  "\"#vothL228\"": "\"Sudeten\"",
  "\"#vothL230\"": "\"Carpathian Mountains Region\"",
  "\"#vothL298\"": "\"Praha\"",
  "\"#vothL352\"": "\"Neuschonstau\"",
  "\"#vothL400\"": "\"Vyškov\"",
  "\"#vothL435\"": "\"Ústí nad Labem\"",
  "\"#vothL436\"": "\"Litomyšl\"",
  "\"#vothL439\"": "\"Ostrava\"",
  "\"#vothL501\"": "\"Nováky\"",
  "\"#vothL502\"": "\"Zvolen\"",
  "\"#vothL503\"": "\"Prešov\"",
  "\"#vothL504\"": "\"Brezno\"",
  "\"#vothL561\"": "\"Litoměřice\"",
  "\"#vothL556\"": "\"Cairo\"",
  "\"#vothL11\"": "\"Tartu\"",
  "\"#vothL128\"": "\"Narva\"",
  "\"#vothL148\"": "\"Tallinn\"",
  "\"#vothL259\"": "\"Toila\"",
  "\"#vothL597\"": "\"Pärnu\"",
  "\"#vothL13\"": "\"Paris\"",
  "\"#vothL18\"": "\"Hénouville\"",
  "\"#vothL19\"": "\"Hénonville\"",
  "\"#vothL20\"": "\"Périgueux\"",
  "\"#vothL21\"": "\"Limoges\"",
  "\"#vothL22\"": "\"Compiègne\"",
  "\"#vothL23\"": "\"Drancy\"",
  "\"#vothL24\"": "\"Pithiviers\"",
  "\"#vothL25\"": "\"Colmar\"",
  "\"#vothL26\"": "\"Nice\"",
  "\"#vothL27\"": "\"Cannes\"",
  "\"#vothL141\"": "\"Le Brugeron\"",
  "\"#vothL152\"": "\"Corbie\"",
  "\"#vothL159\"": "\"Cantal department\"",
  "\"#vothL166\"": "\"Lorraine region\"",
  "\"#vothL185\"": "\"Rivesaltes\"",
  "\"#vothL190\"": "\"Gurs\"",
  "\"#vothL201\"": "\"Les Milles\"",
  "\"#vothL203\"": "\"Le Vernet\"",
  "\"#vothL209\"": "\"Noé\"",
  "\"#vothL236\"": "\"Marseille\"",
  "\"#vothL242\"": "\"Natzwiller\"",
  "\"#vothL261\"": "\"Toulouse\"",
  "\"#vothL262\"": "\"Versailles\"",
  "\"#vothL265\"": "\"Orléans\"",
  "\"#vothL267\"": "\"Lyon\"",
  "\"#vothL268\"": "\"Vichy\"",
  "\"#vothL272\"": "\"Bordeaux\"",
  "\"#vothL276\"": "\"La Rochelle\"",
  "\"#vothL299\"": "\"Barbizon\"",
  "\"#vothL300\"": "\"Courbevoie\"",
  "\"#vothL320\"": "\"Annecy\"",
  "\"#vothL321\"": "\"Chambéry\"",
  "\"#vothL323\"": "\"Dunkerque\"",
  "\"#vothL324\"": "\"Cravant\"",
  "\"#vothL325\"": "\"Olliergues\"",
  "\"#vothL326\"": "\"Clermont-Ferrand\"",
  "\"#vothL328\"": "\"Albi\"",
  "\"#vothL329\"": "\"Brens\"",
  "\"#vothL331\"": "\"Saint-Julien-en-Genevois\"",
  "\"#vothL333\"": "\"Nimes\"",
  "\"#vothL334\"": "\"Perpignan\"",
  "\"#vothL335\"": "\"Osseja\"",
  "\"#vothL339\"": "\"Grenoble\"",
  "\"#vothL341\"": "\"Pyrenees\"",
  "\"#vothL374\"": "\"Nièvre department\"",
  "\"#vothL375\"": "\"Strasbourg\"",
  "\"#vothL376\"": "\"Besançon\"",
  "\"#vothL413\"": "\"Le Creusot\"",
  "\"#vothL416\"": "\"Vendôme district\"",
  "\"#vothL424\"": "\"Amiens\"",
  "\"#vothL456\"": "\"Moulins\"",
  "\"#vothL457\"": "\"Brive-la-Gaillarde\"",
  "\"#vothL458\"": "\"Voiron\"",
  "\"#vothL495\"": "\"Ecouis\"",
  "\"#vothL500\"": "\"Romainville\"",
  "\"#vothL514\"": "\"Thiers\"",
  "\"#vothL516\"": "\"Sedan\"",
  "\"#vothL518\"": "\"Aix-en-Provence\"",
  "\"#vothL520\"": "\"Elne\"",
  "\"#vothL521\"": "\"Septfonds\"",
  "\"#vothL522\"": "\"Lorient\"",
  "\"#vothL523\"": "\"Metz\"",
  "\"#vothL524\"": "\"Saint-Étienne\"",
  "\"#vothL550\"": "\"Bart\"",
  "\"#vothL563\"": "\"Pantin\"",
  "\"#vothL566\"": "\"Rouen\"",
  "\"#vothL567\"": "\"Maintenon\"",
  "\"#vothL571\"": "\"Cagny\"",
  "\"#vothL572\"": "\"Péronne\"",
  "\"#vothL573\"": "\"Bougainville\"",
  "\"#vothL574\"": "\"Pellevoisin\"",
  "\"#vothL575\"": "\"Quintal\"",
  "\"#vothL583\"": "\"Gaillac\"",
  "\"#vothL588\"": "\"Chelles\"",
  "\"#vothL594\"": "\"Saint-Cyprien\"",
  "\"#vothL601\"": "\"Annemasse\"",
  "\"#vothL149\"": "\"Kutaisi\"",
  "\"#vothL554\"": "\"Tbilisi\"",
  "\"#vothL29\"": "\"München\"",
  "\"#vothL33\"": "\"Bernkastel-Kues\"",
  "\"#vothL34\"": "\"Nürnberg\"",
  "\"#vothL35\"": "\"Wiesbaden\"",
  "\"#vothL36\"": "\"Dresden\"",
  "\"#vothL38\"": "\"Dachau\"",
  "\"#vothL39\"": "\"Mühldorf am Inn\"",
  "\"#vothL40\"": "\"Bergen\"",
  "\"#vothL41\"": "\"Burgau\"",
  "\"#vothL42\"": "\"Weimar\"",
  "\"#vothL43\"": "\"Fürstenberg\"",
  "\"#vothL44\"": "\"Meissen\"",
  "\"#vothL45\"": "\"Taucha\"",
  "\"#vothL46\"": "\"Oschatz\"",
  "\"#vothL47\"": "\"Flossenbürg\"",
  "\"#vothL48\"": "\"Aschersleben\"",
  "\"#vothL49\"": "\"Oranienburg\"",
  "\"#vothL51\"": "\"Crawinkel\"",
  "\"#vothL54\"": "\"Braunschweig\"",
  "\"#vothL55\"": "\"Ludwigslust\"",
  "\"#vothL56\"": "\"Neustadt-Glewe\"",
  "\"#vothL57\"": "\"Görlitz\"",
  "\"#vothL58\"": "\"Fürth\"",
  "\"#vothL59\"": "\"Nordhausen\"",
  "\"#vothL60\"": "\"Kamenz\"",
  "\"#vothL61\"": "\"Magdeburg\"",
  "\"#vothL62\"": "\"Ellrich\"",
  "\"#vothL63\"": "\"Augsburg\"",
  "\"#vothL64\"": "\"Ravensbrück\"",
  "\"#vothL65\"": "\"Stuttgart\"",
  "\"#vothL66\"": "\"Hillersleben\"",
  "\"#vothL67\"": "\"Verl\"",
  "\"#vothL130\"": "\"Hamburg\"",
  "\"#vothL131\"": "\"Heilenbach\"",
  "\"#vothL134\"": "\"Berlin\"",
  "\"#vothL140\"": "\"Mannheim\"",
  "\"#vothL142\"": "\"Kaunitz\"",
  "\"#vothL143\"": "\"Brunnau\"",
  "\"#vothL150\"": "\"Falkenberg\"",
  "\"#vothL160\"": "\"Offenburg\"",
  "\"#vothL164\"": "\"Schwabhausen Bei Landsberg\"",
  "\"#vothL168\"": "\"Lippstadt\"",
  "\"#vothL169\"": "\"Barth\"",
  "\"#vothL170\"": "\"Malchow\"",
  "\"#vothL173\"": "\"Mecklenburg region\"",
  "\"#vothL175\"": "\"Bremen\"",
  "\"#vothL176\"": "\"Auerbach\"",
  "\"#vothL179\"": "\"Börgermoor\"",
  "\"#vothL182\"": "\"Chemnitz\"",
  "\"#vothL188\"": "\"Gersdorf\"",
  "\"#vothL199\"": "\"Leipzig\"",
  "\"#vothL207\"": "\"Weidenberg\"",
  "\"#vothL208\"": "\"Wilhelmshaven\"",
  "\"#vothL212\"": "\"Papenburg\"",
  "\"#vothL214\"": "\"Freistaat Sachsen\"",
  "\"#vothL215\"": "\"Goldberg\"",
  "\"#vothL216\"": "\"Tutzing\"",
  "\"#vothL218\"": "\"Erfurt\"",
  "\"#vothL220\"": "\"Retzow\"",
  "\"#vothL221\"": "\"Türkheim\"",
  "\"#vothL224\"": "\"Freising\"",
  "\"#vothL237\"": "\"Karlsruhe\"",
  "\"#vothL238\"": "\"Oberlungwitz\"",
  "\"#vothL243\"": "\"Landsberg am Lech\"",
  "\"#vothL263\"": "\"Saarland region\"",
  "\"#vothL270\"": "\"Grimma\"",
  "\"#vothL273\"": "\"Trier\"",
  "\"#vothL274\"": "\"Schrobenhausen\"",
  "\"#vothL275\"": "\"Mainz\"",
  "\"#vothL281\"": "\"Frankfurt am Main\"",
  "\"#vothL284\"": "\"Bochum\"",
  "\"#vothL285\"": "\"Essen\"",
  "\"#vothL286\"": "\"Hannover\"",
  "\"#vothL287\"": "\"Celle\"",
  "\"#vothL288\"": "\"Weil am Rhein\"",
  "\"#vothL302\"": "\"Geislingen an der Steige\"",
  "\"#vothL304\"": "\"Heidelberg\"",
  "\"#vothL342\"": "\"Moers\"",
  "\"#vothL343\"": "\"Geldern\"",
  "\"#vothL356\"": "\"Prienbach-am-Inn\"",
  "\"#vothL357\"": "\"Stephanskirchen\"",
  "\"#vothL358\"": "\"Iffeldorf\"",
  "\"#vothL373\"": "\"Aschaffenburg\"",
  "\"#vothL380\"": "\"Oberlangen\"",
  "\"#vothL381\"": "\"Kempten\"",
  "\"#vothL382\"": "\"Farsleben\"",
  "\"#vothL383\"": "\"Wurzen\"",
  "\"#vothL387\"": "\"Regensburg\"",
  "\"#vothL394\"": "\"Luxembourg\"",
  "\"#vothL396\"": "\"Schimberg\"",
  "\"#vothL401\"": "\"Eisenhüttenstadt\"",
  "\"#vothL402\"": "\"Frankfurt an der Oder\"",
  "\"#vothL404\"": "\"Wismar\"",
  "\"#vothL405\"": "\"Bad Schwartau\"",
  "\"#vothL410\"": "\"Kevelaer\"",
  "\"#vothL432\"": "\"Kassel\"",
  "\"#vothL442\"": "\"Bayreuth\"",
  "\"#vothL444\"": "\"Nancy\"",
  "\"#vothL449\"": "\"Eisenberg\"",
  "\"#vothL450\"": "\"Schwandorf in Bayern\"",
  "\"#vothL451\"": "\"Deggendorf\"",
  "\"#vothL452\"": "\"Paderborn\"",
  "\"#vothL460\"": "\"Wanne\"",
  "\"#vothL461\"": "\"Köln\"",
  "\"#vothL462\"": "\"Coburg\"",
  "\"#vothL463\"": "\"Gotha\"",
  "\"#vothL464\"": "\"Eisenach\"",
  "\"#vothL468\"": "\"Rosenheim\"",
  "\"#vothL481\"": "\"Passau\"",
  "\"#vothL483\"": "\"Simbach am Inn\"",
  "\"#vothL488\"": "\"Wetzlar\"",
  "\"#vothL489\"": "\"Marburg\"",
  "\"#vothL532\"": "\"Lichterfelde\"",
  "\"#vothL535\"": "\"Ampfing\"",
  "\"#vothL540\"": "\"Pfalzheim\"",
  "\"#vothL543\"": "\"Schwerin\"",
  "\"#vothL545\"": "\"Immendingen\"",
  "\"#vothL552\"": "\"Rosenberg\"",
  "\"#vothL560\"": "\"Halle\"",
  "\"#vothL582\"": "\"Aachen\"",
  "\"#vothL68\"": "\"Thessaloníki\"",
  "\"#vothL126\"": "\"Athens\"",
  "\"#vothL244\"": "\"Komotiní\"",
  "\"#vothL245\"": "\"Xánthi\"",
  "\"#vothL246\"": "\"Kavála\"",
  "\"#vothL247\"": "\"Dráma\"",
  "\"#vothL248\"": "\"Véroia\"",
  "\"#vothL249\"": "\"Kastoría\"",
  "\"#vothL250\"": "\"Didymoteicho\"",
  "\"#vothL251\"": "\"Orestiada\"",
  "\"#vothL252\"": "\"Alexandroupoli\"",
  "\"#vothL253\"": "\"Flórina\"",
  "\"#vothL254\"": "\"Thessalía\"",
  "\"#vothL283\"": "\"Piraeus\"",
  "\"#vothL69\"": "\"Szombathely\"",
  "\"#vothL70\"": "\"Kisvárda\"",
  "\"#vothL72\"": "\"Székesfehérvár\"",
  "\"#vothL132\"": "\"Budapest\"",
  "\"#vothL301\"": "\"Mátészalka\"",
  "\"#vothL525\"": "\"Hatvan\"",
  "\"#vothL526\"": "\"Jászberény\"",
  "\"#vothL527\"": "\"Novi Sad\"",
  "\"#vothL344\"": "\"Miskolc\"",
  "\"#vothL73\"": "\"Tradate\"",
  "\"#vothL291\"": "\"Como\"",
  "\"#vothL292\"": "\"Milano\"",
  "\"#vothL322\"": "\"Turin\"",
  "\"#vothL348\"": "\"Merano\"",
  "\"#vothL349\"": "\"Rome\"",
  "\"#vothL350\"": "\"Bari\"",
  "\"#vothL415\"": "\"Cremona\"",
  "\"#vothL425\"": "\"Venice\"",
  "\"#vothL559\"": "\"Almaty\"",
  "\"#vothL129\"": "\"Rīga\"",
  "\"#vothL144\"": "\"Rūjiena\"",
  "\"#vothL406\"": "\"Jelgava\"",
  "\"#vothL596\"": "\"Liepāja\"",
  "\"#vothL74\"": "\"Vilnius\"",
  "\"#vothL75\"": "\"Labūnava\"",
  "\"#vothL76\"": "\"Kaunas\"",
  "\"#vothL153\"": "\"Vilkaviškis\"",
  "\"#vothL154\"": "\"Zemaičių Kalvarija\"",
  "\"#vothL163\"": "\"Sakiai\"",
  "\"#vothL165\"": "\"Telšiai\"",
  "\"#vothL181\"": "\"Pravieniškės\"",
  "\"#vothL353\"": "\"Šiauliai\"",
  "\"#vothL362\"": "\"Kretinga\"",
  "\"#vothL363\"": "\"Klaipėda\"",
  "\"#vothL440\"": "\"Kelm\"",
  "\"#vothL474\"": "\"Švenčionys\"",
  "\"#vothL476\"": "\"Pabradė\"",
  "\"#vothL505\"": "\"Ukmergė\"",
  "\"#vothL557\"": "\"Kybartai\"",
  "\"#vothL578\"": "\"Rainiai\"",
  "\"#vothL534\"": "\"Mexico City\"",
  "\"#vothL271\"": "\"Casablanca\"",
  "\"#vothL139\"": "\"Yerushalayim\"",
  "\"#vothL260\"": "\"Hadera\"",
  "\"#vothL280\"": "\"Tel Aviv\"",
  "\"#vothL52\"": "\"Kędzierzyn-Koźle\"",
  "\"#vothL53\"": "\"Brzeszcze\"",
  "\"#vothL77\"": "\"Staszów\"",
  "\"#vothL78\"": "\"Starachowice\"",
  "\"#vothL79\"": "\"Warsaw\"",
  "\"#vothL80\"": "\"Augustów\"",
  "\"#vothL81\"": "\"Katowice\"",
  "\"#vothL82\"": "\"Lódź\"",
  "\"#vothL83\"": "\"Dąbrowa Górnicza\"",
  "\"#vothL84\"": "\"Kielce\"",
  "\"#vothL85\"": "\"Wieliczka\"",
  "\"#vothL86\"": "\"Wadowice\"",
  "\"#vothL87\"": "\"Olkusz\"",
  "\"#vothL89\"": "\"Kalisz\"",
  "\"#vothL90\"": "\"Oświęcim\"",
  "\"#vothL91\"": "\"Częstochowa\"",
  "\"#vothL92\"": "\"Lublin\"",
  "\"#vothL93\"": "\"Plaszow\"",
  "\"#vothL94\"": "\"Międzyrzec Podlaski\"",
  "\"#vothL95\"": "\"Rogoźnica\"",
  "\"#vothL96\"": "\"Libiaż\"",
  "\"#vothL97\"": "\"Skarżysko-Kamienna\"",
  "\"#vothL98\"": "\"Sosnowiec\"",
  "\"#vothL99\"": "\"Jelcz-Laskowice\"",
  "\"#vothL100\"": "\"Rzeszów\"",
  "\"#vothL101\"": "\"Będzin\"",
  "\"#vothL102\"": "\"Roznów\"",
  "\"#vothL103\"": "\"Wejherowo\"",
  "\"#vothL105\"": "\"Gliwice\"",
  "\"#vothL106\"": "\"Strzegom\"",
  "\"#vothL107\"": "\"Sztutowo\"",
  "\"#vothL108\"": "\"Giebułtów\"",
  "\"#vothL109\"": "\"Mielec\"",
  "\"#vothL135\"": "\"Kraków\"",
  "\"#vothL138\"": "\"Przemyśl\"",
  "\"#vothL151\"": "\"Janów Lubelski\"",
  "\"#vothL155\"": "\"Zakopane\"",
  "\"#vothL158\"": "\"Wasów\"",
  "\"#vothL162\"": "\"Andrychów\"",
  "\"#vothL172\"": "\"Bełżec\"",
  "\"#vothL178\"": "\"Poznań\"",
  "\"#vothL180\"": "\"Buczacz\"",
  "\"#vothL183\"": "\"Pustkow\"",
  "\"#vothL186\"": "\"Gdańsk\"",
  "\"#vothL187\"": "\"Wesoła\"",
  "\"#vothL189\"": "\"Hrodna\"",
  "\"#vothL192\"": "\"Jelenia Góra\"",
  "\"#vothL196\"": "\"Kutno\"",
  "\"#vothL198\"": "\"Sobibór\"",
  "\"#vothL202\"": "\"Szebnie\"",
  "\"#vothL204\"": "\"Trawniki\"",
  "\"#vothL205\"": "\"Treblinka\"",
  "\"#vothL206\"": "\"Warta\"",
  "\"#vothL210\"": "\"Prokocim\"",
  "\"#vothL211\"": "\"Jawiszowice\"",
  "\"#vothL217\"": "\"Tomaszów Mazowiecki\"",
  "\"#vothL231\"": "\"Miłoszyce\"",
  "\"#vothL239\"": "\"Gogolin\"",
  "\"#vothL241\"": "\"Bolków\"",
  "\"#vothL258\"": "\"Gdynia\"",
  "\"#vothL296\"": "\"Radzyń Podlaski\"",
  "\"#vothL297\"": "\"Nowy Targ\"",
  "\"#vothL303\"": "\"Szczecin\"",
  "\"#vothL308\"": "\"Chorzów\"",
  "\"#vothL309\"": "\"Debica\"",
  "\"#vothL313\"": "\"Wrocław\"",
  "\"#vothL337\"": "\"Bełżyce\"",
  "\"#vothL347\"": "\"Tarnow\"",
  "\"#vothL351\"": "\"Prabuty\"",
  "\"#vothL354\"": "\"Dębice\"",
  "\"#vothL359\"": "\"Radom\"",
  "\"#vothL360\"": "\"Kraśnik\"",
  "\"#vothL366\"": "\"Czechowice\"",
  "\"#vothL372\"": "\"Bytom\"",
  "\"#vothL379\"": "\"Hutysche\"",
  "\"#vothL385\"": "\"Łowicz\"",
  "\"#vothL391\"": "\"Walim\"",
  "\"#vothL393\"": "\"Gmina Wolin\"",
  "\"#vothL395\"": "\"Głuszyca\"",
  "\"#vothL397\"": "\"Sandomierz\"",
  "\"#vothL403\"": "\"Bielsko-Biała\"",
  "\"#vothL417\"": "\"Radomyśl Wielki\"",
  "\"#vothL437\"": "\"Turnow\"",
  "\"#vothL438\"": "\"Cieszyn\"",
  "\"#vothL443\"": "\"Wodzisław\"",
  "\"#vothL445\"": "\"Radomsko\"",
  "\"#vothL447\"": "\"Skierniewice\"",
  "\"#vothL459\"": "\"Zba̜szyń\"",
  "\"#vothL467\"": "\"Siedlce\"",
  "\"#vothL475\"": "\"Klecin\"",
  "\"#vothL477\"": "\"Kamienna Góra\"",
  "\"#vothL480\"": "\"Świdnica\"",
  "\"#vothL484\"": "\"Podde̜bice\"",
  "\"#vothL485\"": "\"Aleksandrów Łódzki\"",
  "\"#vothL486\"": "\"Białystok\"",
  "\"#vothL487\"": "\"Radoszyce\"",
  "\"#vothL494\"": "\"Rajsko\"",
  "\"#vothL496\"": "\"Lukow\"",
  "\"#vothL497\"": "\"Chelm\"",
  "\"#vothL498\"": "\"Jasło\"",
  "\"#vothL499\"": "\"Bochnia\"",
  "\"#vothL509\"": "\"Poniatowa\"",
  "\"#vothL510\"": "\"Brzeziny\"",
  "\"#vothL511\"": "\"Ternopol\"",
  "\"#vothL512\"": "\"Zolotyy Potik\"",
  "\"#vothL513\"": "\"Wolin\"",
  "\"#vothL515\"": "\"Czortków\"",
  "\"#vothL519\"": "\"Gorodenka\"",
  "\"#vothL530\"": "\"Krosno\"",
  "\"#vothL531\"": "\"Zabrze\"",
  "\"#vothL536\"": "\"Nowy Sa̜cz\"",
  "\"#vothL538\"": "\"Pszczyna\"",
  "\"#vothL539\"": "\"Podgórze\"",
  "\"#vothL541\"": "\"Brzezinka\"",
  "\"#vothL542\"": "\"Stargard Szczeciński\"",
  "\"#vothL544\"": "\"Bydgoszcz\"",
  "\"#vothL549\"": "\"Zakrzów\"",
  "\"#vothL553\"": "\"Maślice Wielkie\"",
  "\"#vothL564\"": "\"Radomyśl nad Sanem\"",
  "\"#vothL576\"": "\"Mysłowice\"",
  "\"#vothL577\"": "\"Myszków\"",
  "\"#vothL579\"": "\"Sławków\"",
  "\"#vothL580\"": "\"Pionki\"",
  "\"#vothL581\"": "\"Wolbrom\"",
  "\"#vothL599\"": "\"Bobrek\"",
  "\"#vothL600\"": "\"Mikolów\"",
  "\"#vothL602\"": "\"Sieradz\"",
  "\"#vothL603\"": "\"Krynica-Zdrój\"",
  "\"#vothL605\"": "\"Sanok\"",
  "\"#vothL606\"": "\"Grybów\"",
  "\"#vothL613\"": "\"Delyatyn\"",
  "\"#vothL595\"": "\"Lisbon\"",
  "\"#vothL110\"": "\"Sighetu Marmaţiei\"",
  "\"#vothL111\"": "\"Maramures Province\"",
  "\"#vothL112\"": "\"Oradea\"",
  "\"#vothL234\"": "\"Edineţ\"",
  "\"#vothL277\"": "\"Bucharest\"",
  "\"#vothL279\"": "\"Cluj-Napoca\"",
  "\"#vothL399\"": "\"Rădăuţi\"",
  "\"#vothL562\"": "\"Constanţa\"",
  "\"#vothL113\"": "\"Saratov\"",
  "\"#vothL156\"": "\"Nivenskoye\"",
  "\"#vothL294\"": "\"Volgograd\"",
  "\"#vothL361\"": "\"Moskva\"",
  "\"#vothL364\"": "\"Koenigsberg\"",
  "\"#vothL367\"": "\"Rostov\"",
  "\"#vothL368\"": "\"Makhachkala\"",
  "\"#vothL407\"": "\"Buguruslan\"",
  "\"#vothL409\"": "\"Novosibirsk\"",
  "\"#vothL441\"": "\"Smolensk\"",
  "\"#vothL453\"": "\"Sankt-Peterburg\"",
  "\"#vothL547\"": "\"Samara\"",
  "\"#vothL558\"": "\"Kirov\"",
  "\"#vothL584\"": "\"Kaliningrad\"",
  "\"#vothL607\"": "\"Buzuluk\"",
  "\"#vothL608\"": "\"Totskoye\"",
  "\"#vothL611\"": "\"Sukhobezvodnoye\"",
  "\"#vothL612\"": "\"Nizhniy Novgorod\"",
  "\"#vothL551\"": "\"Belgrade \"",
  "\"#vothL114\"": "\"Kurima\"",
  "\"#vothL115\"": "\"Bratislava\"",
  "\"#vothL345\"": "\"Kosice\"",
  "\"#vothL448\"": "\"Banská Bystrica\"",
  "\"#vothL428\"": "\"Johannesburg\"",
  "\"#vothL167\"": "\"Castelló d Empúries\"",
  "\"#vothL282\"": "\"Barcelona\"",
  "\"#vothL423\"": "\"Madrid\"",
  "\"#vothL454\"": "\"Bilbao\"",
  "\"#vothL555\"": "\"Córdoba\"",
  "\"#vothL570\"": "\"San Cugat del Vallés\"",
  "\"#vothL116\"": "\"Zurich\"",
  "\"#vothL117\"": "\"Genève\"",
  "\"#vothL200\"": "\"Montreux\"",
  "\"#vothL278\"": "\"Basel\"",
  "\"#vothL289\"": "\"Engelberg\"",
  "\"#vothL290\"": "\"Luzern\"",
  "\"#vothL420\"": "\"Wädenswil\"",
  "\"#vothL506\"": "\"Speicher\"",
  "\"#vothL507\"": "\"Sankt Gallen\"",
  "\"#vothL565\"": "\"Appenzell\"",
  "\"#vothL615\"": "\"Buchs\"",
  "\"#vothL616\"": "\"Gattikon\"",
  "\"#vothL617\"": "\"Lugano\"",
  "\"#vothL618\"": "\"Morcote\"",
  "\"#vothL609\"": "\"Ghŭsar\"",
  "\"#vothL371\"": "\"İstanbul\"",
  "\"#vothL369\"": "\"Türkmenbaşy\"",
  "\"#vothL587\"": "\"Mary\"",
  "\"#vothL120\"": "\"Zaporizhia\"",
  "\"#vothL121\"": "\"Brody\"",
  "\"#vothL122\"": "\"Dnipro\"",
  "\"#vothL123\"": "\"Lviv\"",
  "\"#vothL136\"": "\"Chernivtsi\"",
  "\"#vothL137\"": "\"Rivne\"",
  "\"#vothL147\"": "\"Bus’k\"",
  "\"#vothL240\"": "\"Kyiv\"",
  "\"#vothL311\"": "\"Odessa\"",
  "\"#vothL338\"": "\"Kharkov\"",
  "\"#vothL370\"": "\"Poltava\"",
  "\"#vothL378\"": "\"Zolochiv\"",
  "\"#vothL431\"": "\"Bohuslav\"",
  "\"#vothL533\"": "\"Dniprovs'ke\"",
  "\"#vothL548\"": "\"Kamianets-Podilskyi\"",
  "\"#vothL568\"": "\"Kremenets\"",
  "\"#vothL569\"": "\"Dubno\"",
  "\"#vothL586\"": "\"Volochysk\"",
  "\"#vothL589\"": "\"Pidvolochysk\"",
  "\"#vothL590\"": "\"Rava-Rus’ka\"",
  "\"#vothL591\"": "\"Cherkasy\"",
  "\"#vothL593\"": "\"Barysh\"",
  "\"#vothL604\"": "\"Drohobych\"",
  "\"#vothL269\"": "\"Gibraltar\"",
  "\"#vothL293\"": "\"London\"",
  "\"#vothL537\"": "\"Newcastle upon Tyne\"",
  "\"#vothL255\"": "\"Hartford\"",
  "\"#vothL256\"": "\"Chicago\"",
  "\"#vothL257\"": "\"New York\"",
  "\"#vothL306\"": "\"Sacramento\"",
  "\"#vothL307\"": "\"Detroit\"",
  "\"#vothL314\"": "\"Brooklyn\"",
  "\"#vothL330\"": "\"Washington\"",
  "\"#vothL332\"": "\"Boston\"",
  "\"#vothL377\"": "\"San Francisco\"",
  "\"#vothL411\"": "\"Miami\"",
  "\"#vothL412\"": "\"Cleveland\"",
  "\"#vothL422\"": "\"Los Angeles\"",
  "\"#vothL429\"": "\"Milwaukee\"",
  "\"#vothL470\"": "\"Atlanta\"",
  "\"#vothL490\"": "\"Erie\"",
  "\"#vothL491\"": "\"Gary\"",
  "\"#vothL492\"": "\"Durango\"",
  "\"#vothL493\"": "\"Newark\"",
  "\"#vothL598\"": "\"Philadelphia\"",
  "\"#vothL408\"": "\"Bukhara\"",
  "\"#vothL610\"": "\"Tashkent\"",
  "\"#vothL619\"": "\"Sławięcice \"",
  "\"#vothC4\"": "\"Auschwitz concentration camp\"",
  "\"#vothC6\"": "\"Bendsburg concentration camp \"",
  "\"#vothC7\"": "\"Belzec concentration camp\"",
  "\"#vothC8\"": "\"Bergen-Belsen concentration camp\"",
  "\"#vothC11\"": "\"Birkenheim\"",
  "\"#vothC15\"": "\"Buchenwald concentration camp\"",
  "\"#vothC13\"": "\"Börgermoor concentration camp\"",
  "\"#vothC24\"": "\"Częstochowa concentration camp\"",
  "\"#vothC25\"": "\"Dachau concentration camp\"",
  "\"#vothC83\"": "\"Mittelbau-Dora concentration camp\"",
  "\"#vothC27\"": "\"Drancy concentration camp\"",
  "\"#vothC29\"": "\"Flossenbürg concentration camp\"",
  "\"#vothC152\"": "\"Fort de Romainville concentration camp\"",
  "\"#vothC36\"": "\"Gogolin concentration camp\"",
  "\"#vothC162\"": "\"Gross Masselwitz concentration camp\"",
  "\"#vothC39\"": "\"Gross-Rosen concentration camp\"",
  "\"#vothC40\"": "\"Gurs concentration camp\"",
  "\"#vothC41\"": "\"Haidari concentration camp\"",
  "\"#vothC140\"": "\"Herzogenburg concentration camp\"",
  "\"#vothC43\"": "\"Janinagrube concentration camp\"",
  "\"#vothC44\"": "\"Janowska concentration camp\"",
  "\"#vothC161\"": "\"Karviná concentration camp\"",
  "\"#vothC157\"": "\"Kiełbasin concentration camp\"",
  "\"#vothC163\"": "\"Klettendorf concentration camp\"",
  "\"#vothC47\"": "\"Płaszów concentration camp\"",
  "\"#vothC61\"": "\"Le Vernet concentration camp\"",
  "\"#vothC59\"": "\"Les Avants\"",
  "\"#vothC60\"": "\"Les Milles concentration camp\"",
  "\"#vothC62\"": "\"Limoges\"",
  "\"#vothC69\"": "\"Majdanek concentration camp\"",
  "\"#vothC72\"": "\"Mauthausen concentration camp\"",
  "\"#vothC114\"": "\"Struthof concentration camp\"",
  "\"#vothC170\"": "\"Neustadt \"",
  "\"#vothC153\"": "\"Nováky concentration camp\"",
  "\"#vothC82\"": "\"Noé concentration camp\"",
  "\"#vothC126\"": "\"Esterwegen concentration camp\"",
  "\"#vothC88\"": "\"Pithiviers concentration camp\"",
  "\"#vothC90\"": "\"Fort VII concentration camp\"",
  "\"#vothC91\"": "\"Pravieniškės concentration camp\"",
  "\"#vothC94\"": "\"Pustków concentration camp\"",
  "\"#vothC95\"": "\"Ravensbrück concentration camp\"",
  "\"#vothC138\"": "\"Riesenburg \"",
  "\"#vothC96\"": "\"Rivesaltes concentration camp\"",
  "\"#vothC22\"": "\"Royallieu concentration camp\"",
  "\"#vothC97\"": "\"Roznow concentration camp\"",
  "\"#vothC98\"": "\"Reichshof concentration camp\"",
  "\"#vothC99\"": "\"Sachsenhausen concentration camp\"",
  "\"#vothC160\"": "\"Sakrau concentration camp\"",
  "\"#vothC154\"": "\"Septfonds concentration camp\"",
  "\"#vothC139\"": "\"Schaulen concentration camp\"",
  "\"#vothC102\"": "\"Skarżysko-Kamienna concentration camp\"",
  "\"#vothC104\"": "\"Sobibór concentration camp\"",
  "\"#vothC132\"": "\"Starachowice concentration camp\"",
  "\"#vothC107\"": "\"Stutthof concentration camp\"",
  "\"#vothC108\"": "\"Szebnie concentration camp\"",
  "\"#vothC112\"": "\"Treblinka concentration camp\"",
  "\"#vothC115\"": "\"Vyhne concentration camp\"",
  "\"#vothC119\"": "\"Weidenberg\"",
  "\"#vothC120\"": "\"Wejherowo\"",
  "\"#vothC148\"": "\"Wischau\"",
  "\"#vothC10\"": "\"Birkenau concentration camp\"",
  "\"#vothC12\"": "\"Blechhammer concentration camp\"",
  "\"#vothC169\"": "\"Bobrek concentration camp\"",
  "\"#vothC151\"": "\"Budy concentration camp\"",
  "\"#vothC31\"": "\"Fürstengrube concentration camp\"",
  "\"#vothC35\"": "\"Gleiwitz\"",
  "\"#vothC45\"": "\"Jawischowitz concentration camp\"",
  "\"#vothC18\"": "\"Monowitz concentration camp\"",
  "\"#vothC2\"": "\"Aschersleben concentration camp\"",
  "\"#vothC145\"": "\"Eisen- und Hüttenwerke, Bochum concentration camp\"",
  "\"#vothC23\"": "\"Crawinkel concentration camp\"",
  "\"#vothC58\"": "\"Leipzig-Thekla concentration camp\"",
  "\"#vothC64\"": "\"Lippstadt II concentration camp\"",
  "\"#vothC68\"": "\"Magdeburg Brabag concentration camp\"",
  "\"#vothC84\"": "\"Ohrdruf concentration camp\"",
  "\"#vothC87\"": "\"Oschatz stadium\"",
  "\"#vothC109\"": "\"Taucha concentration camp\"",
  "\"#vothC3\"": "\"Augsburg Messerschmitt concentration camp\"",
  "\"#vothC159\"": "\"Pelcery \"",
  "\"#vothC118\"": "\"Warta\"",
  "\"#vothC19\"": "\"Burgau concentration camp\"",
  "\"#vothC133\"": "\"Landsberg concentration camp\"",
  "\"#vothC78\"": "\"Mühldorf concentration camp\"",
  "\"#vothC142\"": "\"Stephanskirchen (BMW) concentration camp\"",
  "\"#vothC128\"": "\"Türkheim concentration camp\"",
  "\"#vothC20\"": "\"Chemnitz concentration camp\"",
  "\"#vothC74\"": "\"Meissen-Neuhirschstein concentration camp\"",
  "\"#vothC110\"": "\"Theresienstadt concentration camp\"",
  "\"#vothC9\"": "\"Biesnitzer Grund concentration camp\"",
  "\"#vothC123\"": "\"Bolkenhain concentration camp\"",
  "\"#vothC30\"": "\"Laskowitz-Meleschwitz concentration camp\"",
  "\"#vothC33\"": "\"Gabersdorf concentration camp\"",
  "\"#vothC57\"": "\"Gebhardsdorf concentration camp\"",
  "\"#vothC37\"": "\"Gräben concentration camp\"",
  "\"#vothC146\"": "\"Wolfsberg concentration camp\"",
  "\"#vothC130\"": "\"Görlitz concentration camp\"",
  "\"#vothC42\"": "\"Hirschberg concentration camp\"",
  "\"#vothC49\"": "\"Kamenz concentration camp\"",
  "\"#vothC164\"": "\"Landeshut concentration camp\"",
  "\"#vothC71\"": "\"Markstädt concentration camp\"",
  "\"#vothC116\"": "\"Waldheim concentration camp\"",
  "\"#vothC147\"": "\"Wüstegiersdorf concentration camp\"",
  "\"#vothC17\"": "\"Budzyń concentration camp\"",
  "\"#vothC144\"": "\"Krasnik concentration camp\"",
  "\"#vothC89\"": "\"Płaszów concentration camp\"",
  "\"#vothC111\"": "\"Trawniki concentration camp\"",
  "\"#vothC63\"": "\"Linz\"",
  "\"#vothC28\"": "\"Ellrich concentration camp\"",
  "\"#vothC14\"": "\"Schillstraße concentration camp \"",
  "\"#vothC80\"": "\"Bremen-Neuenland concentration camp\"",
  "\"#vothC122\"": "\"Wilhelmshaven concentration camp\"",
  "\"#vothC66\"": "\"Wöbbelin concentration camp\"",
  "\"#vothC76\"": "\"Mielec concentration camp\"",
  "\"#vothC121\"": "\"Wieliczka concentration camp\"",
  "\"#vothC92\"": "\"Przemysl concentration camp\"",
  "\"#vothC5\"": "\"Barth concentration camp\"",
  "\"#vothC70\"": "\"Malchow concentration camp\"",
  "\"#vothC81\"": "\"Neustadt-Glewe concentration camp\"",
  "\"#vothC127\"": "\"Rechlin concentration camp\"",
  "\"#vothC125\"": "\"Neuengamme concentration camp\"",
  "\"#vothC86\"": "\"Oranienburg concentration camp\"",
  "\"#vothC21\"": "\"Colmar concentration camp\"",
  "\"#vothC136\"": "\"Geislingen an der Steige concentration camp\"",
  "\"#vothC26\"": "\"Burggraben concentration camp\"",
  "\"#vothC134\"": "\"Gotenhafen concentration camp\"",
  "\"#vothC16\"": "\"Buczacz Ghetto\"",
  "\"#vothC129\"": "\"Budapest Ghetto\"",
  "\"#vothC150\"": "\"Będzin Ghetto\"",
  "\"#vothC38\"": "\"Grodno Ghetto\"",
  "\"#vothC155\"": "\"Hatvan Ghetto\"",
  "\"#vothC50\"": "\"Kovno Ghetto\"",
  "\"#vothC52\"": "\"Kielce Ghetto \"",
  "\"#vothC53\"": "\"Kisvárda Ghetto \"",
  "\"#vothC55\"": "\"Kraków Ghetto\"",
  "\"#vothC56\"": "\"Kutno Ghetto\"",
  "\"#vothC67\"": "\"Lvov Ghetto \"",
  "\"#vothC156\"": "\"Miskolc Ghetto\"",
  "\"#vothC75\"": "\"Międzyrzec Podlaski Ghetto\"",
  "\"#vothC79\"": "\"Munkács Ghetto\"",
  "\"#vothC135\"": "\"Mátészalka Ghetto\"",
  "\"#vothC85\"": "\"Oradea Ghetto \"",
  "\"#vothC93\"": "\"Przemyśl Ghetto\"",
  "\"#vothC143\"": "\"Radom Ghetto\"",
  "\"#vothC100\"": "\"Salonika Ghetto\"",
  "\"#vothC101\"": "\"Máramarossziget Ghetto\"",
  "\"#vothC103\"": "\"Słonim Ghetto\"",
  "\"#vothC105\"": "\"Sosnowiec Ghetto\"",
  "\"#vothC106\"": "\"Wierzbnik-Starachowice Ghetto\"",
  "\"#vothC158\"": "\"Székesfehérvár Ghetto\"",
  "\"#vothC166\"": "\"Telšiai Ghetto \"",
  "\"#vothC167\"": "\"Vilna Ghetto\"",
  "\"#vothC117\"": "\"Warsaw Ghetto\"",
  "\"#vothC65\"": "\"Łódź Ghetto\"",
  "\"#vothL14\"": "\"Jewish Committee home for adult Jewish refugees\"",
  "\"#vothL15\"": "\"ORT School\"",
  "\"#vothL16\"": "\"AJDC office\"",
  "\"#vothL17\"": "\"Grand Hotel\"",
  "\"#vothL12\"": "\"OPEJ children's home\"",
  "\"#vothL28\"": "\"Chateau de Boucicaut; OSE home for adolescents\"",
  "\"#vothL30\"": "\"Funkkaserne displaced-person's camp\"",
  "\"#vothL31\"": "\"UNRRA University of Munich\"",
  "\"#vothL32\"": "\"Lohengrinstrasse\"",
  "\"#vothL37\"": "\"Feldafing displaced persons camp\"",
  "\"#vothL118\"": "\"Community home for displaced Jewish refugees\"",
  "\"#vothL119\"": "\"ORT School\"",
  "\"#vothL968\"": "\"Austria\"",
  "\"#vothL969\"": "\"Belarus\"",
  "\"#vothL970\"": "\"Chile\"",
  "\"#vothL226\"": "\"Czechoslovakia\"",
  "\"#vothL235\"": "\"Estonia\"",
  "\"#vothL124\"": "\"France\"",
  "\"#vothL125\"": "\"Germany\"",
  "\"#vothL222\"": "\"Poland\"",
  "\"#vothL219\"": "\"Greece\"",
  "\"#vothL225\"": "\"Hungary\"",
  "\"#vothL971\"": "\"Italy\"",
  "\"#vothL972\"": "\"Lithuania\"",
  "\"#vothL973\"": "\"Romania\"",
  "\"#vothL223\"": "\"Russia\"",
  "\"#vothL974\"": "\"Slovakia\"",
  "\"#vothL975\"": "\"Switzerland\"",
  "\"#vothL229\"": "\"Ukraine\"",
  "\"#vothL233\"": "\"Latvia\"",
  "\"#vothL976\"": "\"Palestine\"",
  "\"#vothL977\"": "\"Belgium\"",
  "\"#vothL978\"": "\"Georgia\"",
  "\"#vothL979\"": "\"Spain\"",
  "\"#vothL232\"": "\"Albania\"",
  "\"#vothL980\"": "\"United States\"",
  "\"#vothL981\"": "\"United Kingdom\"",
  "\"#vothL982\"": "\"Morocco\"",
  "\"#vothL983\"": "\"Argentina\"",
  "\"#vothL984\"": "\"Algeria\"",
  "\"#vothL985\"": "\"Hungray\"",
  "\"#vothL986\"": "\"Turkmenistan\"",
  "\"#vothL987\"": "\"Turkey\"",
  "\"#vothL988\"": "\"China\"",
  "\"#vothL989\"": "\"Azerbaijan\"",
  "\"#vothL990\"": "\"Uzbekistan\"",
  "\"#vothL991\"": "\"Brazil\"",
  "\"#vothL992\"": "\"Czech Republic\"",
  "\"#vothL993\"": "\"South Africa\"",
  "\"#vothL994\"": "\"Mexico\"",
  "\"#vothL995\"": "\"Serbia\"",
  "\"#vothL996\"": "\"Egypt\"",
  "\"#vothL997\"": "\"Kazakhstan\"",
  "\"#vothL998\"": "\"Portugal\"",
  "\"#vothL999\"": "\"Tajikistan\""
}
