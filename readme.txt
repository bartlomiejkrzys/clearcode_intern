# Uwaga.
# Kody pisane w wersji Pythona 3.5, kompatybilne z 2.7+

# Zadanie 1 - opis podejœcia.
Szczerze mówi¹c, na samym pocz¹tku problemem by³ dobór odpowiedniego sposobu.
Najpier uzna³em, ¿e najlepiej by³oby stosowaæ operacje bitowe (&), by za ich pomoc¹ iterowaæ
po kolejnych bitach liczby N i sprawdzaæ, czy s¹ one 1 lub 0 (w zale¿noœci od tego, czy liczba
jest parzysta, czy nie), ale wraz z tym pomys³em pojawi³ siê problem dot. wielkoœci liczby (z ilu bitów siê sk³ada).
Ustawienie na sztywno jakiejœ konkretnej, np 32 te¿ wyda³o siê bardzo nierozs¹dne. Uzna³em wtedy, 
¿e zastosujê funkcjê math.log i po prostu w ten sposób ustalê górny limit. Dopiero po jakichœ piêciu
minutach myœlenia nad tym problemem (by³o ju¿ póŸno, wraca³em z uczelni) przypomnia³em sobie 
o wbudowanej funkcji bin(), która doœæ prosto przekszta³ci dowoln¹ liczbê na postaæ binarn¹. 
W po³¹czeniu z metod¹ stringów .count() pozwoli wyci¹gn¹æ liczbê 0 lub 1, to te¿ wykorzysta³em to
w ostatecznym rozwi¹zaniu. 

# Zadanie 2 - opis podejœcia.
W zasadzie od razu wiedzia³em, ¿e jest to zadanie zwi¹zane z dynamicznym programowaniem.
Wiedzia³em, ¿e mo¿na do niego podejœæ na dwa sposoby (jak do wszystkiego) i tak te¿ w tym przypadku
podszed³em. Osobiœcie najpierw myœlê nad rozwi¹zaniem problemu metod¹ brute-force, a napisanie
samego kodu rekurencyjnego nie zajê³o mi wiele czasu. Rozpisywa³em te¿ dzia³anie kodów na kartce,
sprawdza³em mo¿liwoœci podejœcia - co (nie)stety czêsto zdarza mi siê robiæ - i w ten sposób powoli doszed³em
do rozwi¹zania dynamicznego. Ju¿ kiedyœ przerabia³em podobny problem (znalezienie czworoboku o najwiêkszym
polu, spoœród kilku po³¹czonych ze sob¹, prezentowanych w³aœnie na macierzy). Po obliczeniu kosztów dojœcia ca³ego
pierwszego rzêdu i kolumny (dla przypadku, gdzie poruszalibyœmy siê innymi œcie¿kami, nale¿a³oby obliczyæ inne pola)
wystarczy znaleŸæ "minimum lokalne" - jak to nazwa³em - a nastêpnie siêgn¹æ po informacje pod odpowiednim indeksem.
Na pocz¹tku oblicza³em minimum lokalne dla ca³ej listy (limit rzêdów i kolumn ustawiony na len(L)), ale doszed³em do 
wniosku, ¿e lepiej obliczaæ tylko tyle, ile jest potrzebne (limit ograniczony do rzêdu i kolumny któr¹ chcemy sprawdziæ),
Zastanawia³em siê te¿ nad implementacj¹, która pozwoli³aby zmniejszyæ koszt pamiêci, która teraz jest O(n^2), bo tworzê
drug¹ listê, listê kosztów takiego samego rozmiaru co ta wejœciowa, ale uzna³em, ¿e mog³oby to za nadto skomplikowaæ sprawê.
Nie jestem te¿ dumny ze sposobu w który wydobywam informacjê z pliku, ale muszê przyznaæ, ¿e wyda³ mi siê on doœæ prosty. 
Zakodowa³em równie¿ obs³ugê wyj¹tku wywo³ania skryptu bez podania argumentu, chocia¿ nie zakodowa³em obs³ugi b³êdu dla
wypadku w którym ktoœ poda z³¹ nazwê œcie¿ki/pliku, poniewa¿ ta wbudowana (FileNotFound) wyda³a mi siê ca³kiem sensowna. 

W pliku dwie wersje rozwi¹zania. 