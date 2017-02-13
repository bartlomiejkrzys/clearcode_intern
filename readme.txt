# Uwaga.
# Kody pisane w wersji Pythona 3.5, kompatybilne z 2.7+

# Zadanie 1 - opis podej�cia.
Szczerze m�wi�c, na samym pocz�tku problemem by� dob�r odpowiedniego sposobu.
Najpier uzna�em, �e najlepiej by�oby stosowa� operacje bitowe (&), by za ich pomoc� iterowa�
po kolejnych bitach liczby N i sprawdza�, czy s� one 1 lub 0 (w zale�no�ci od tego, czy liczba
jest parzysta, czy nie), ale wraz z tym pomys�em pojawi� si� problem dot. wielko�ci liczby (z ilu bit�w si� sk�ada).
Ustawienie na sztywno jakiej� konkretnej, np 32 te� wyda�o si� bardzo nierozs�dne. Uzna�em wtedy, 
�e zastosuj� funkcj� math.log i po prostu w ten spos�b ustal� g�rny limit. Dopiero po jakich� pi�ciu
minutach my�lenia nad tym problemem (by�o ju� p�no, wraca�em z uczelni) przypomnia�em sobie 
o wbudowanej funkcji bin(), kt�ra do�� prosto przekszta�ci dowoln� liczb� na posta� binarn�. 
W po��czeniu z metod� string�w .count() pozwoli wyci�gn�� liczb� 0 lub 1, to te� wykorzysta�em to
w ostatecznym rozwi�zaniu. 

# Zadanie 2 - opis podej�cia.
W zasadzie od razu wiedzia�em, �e jest to zadanie zwi�zane z dynamicznym programowaniem.
Wiedzia�em, �e mo�na do niego podej�� na dwa sposoby (jak do wszystkiego) i tak te� w tym przypadku
podszed�em. Osobi�cie najpierw my�l� nad rozwi�zaniem problemu metod� brute-force, a napisanie
samego kodu rekurencyjnego nie zaj�o mi wiele czasu. Rozpisywa�em te� dzia�anie kod�w na kartce,
sprawdza�em mo�liwo�ci podej�cia - co (nie)stety cz�sto zdarza mi si� robi� - i w ten spos�b powoli doszed�em
do rozwi�zania dynamicznego. Ju� kiedy� przerabia�em podobny problem (znalezienie czworoboku o najwi�kszym
polu, spo�r�d kilku po��czonych ze sob�, prezentowanych w�a�nie na macierzy). Po obliczeniu koszt�w doj�cia ca�ego
pierwszego rz�du i kolumny (dla przypadku, gdzie poruszaliby�my si� innymi �cie�kami, nale�a�oby obliczy� inne pola)
wystarczy znale�� "minimum lokalne" - jak to nazwa�em - a nast�pnie si�gn�� po informacje pod odpowiednim indeksem.
Na pocz�tku oblicza�em minimum lokalne dla ca�ej listy (limit rz�d�w i kolumn ustawiony na len(L)), ale doszed�em do 
wniosku, �e lepiej oblicza� tylko tyle, ile jest potrzebne (limit ograniczony do rz�du i kolumny kt�r� chcemy sprawdzi�),
Zastanawia�em si� te� nad implementacj�, kt�ra pozwoli�aby zmniejszy� koszt pami�ci, kt�ra teraz jest O(n^2), bo tworz�
drug� list�, list� koszt�w takiego samego rozmiaru co ta wej�ciowa, ale uzna�em, �e mog�oby to za nadto skomplikowa� spraw�.
Nie jestem te� dumny ze sposobu w kt�ry wydobywam informacj� z pliku, ale musz� przyzna�, �e wyda� mi si� on do�� prosty. 
Zakodowa�em r�wnie� obs�ug� wyj�tku wywo�ania skryptu bez podania argumentu, chocia� nie zakodowa�em obs�ugi b��du dla
wypadku w kt�rym kto� poda z�� nazw� �cie�ki/pliku, poniewa� ta wbudowana (FileNotFound) wyda�a mi si� ca�kiem sensowna. 

W pliku dwie wersje rozwi�zania. 