# Zadanie 1

## 1.

Najlepsi kandydaci:

Klucz: 230, zgodność: 1.0 'Wkh#Qljkw#Ihuu|\r\rWkh#qljkw#
Klucz: 233, zgodność: 1.0 'The Night Ferry\n\nThe night 
Klucz: 228, zgodność: 0.9947534102833159 "Ymj%Snlmy%Kjww~\x0f\x0fYmj%sn
Klucz: 229, zgodność: 0.9947534102833159 'Xli$Rmklx$Jivv}\x0e\x0eXli$rm
Klucz: 231, zgodność: 0.9947534102833159 'Vjg"Pkijv"Hgtt{\x0c\x0cVjg"pk

## 2.

Sensowny tekst otrzymujemy dla klucza 233. 
Pełny tekst:
'The Night Ferry\n\nThe night ferry left the harbour at eleven, as it had done every evening for as long as anyone in the town could remember. Marta stood at the rail on the upper deck and watched the lights of the quay shrink into a thin yellow line. Below her, the engines settled into their slow, patient rhythm, and the smell of diesel mixed with salt and wet rope.\n\nShe had taken this crossing twice a year since she was a child: once in early spring, when the sea was grey and restless, and once at the end of summer, when it was so calm that the ferry seemed to slide across a sheet of dark glass. Tonight it was neither. A light wind came from the west, and small waves slapped against the hull with a sound like distant applause.\n\nIn the lounge, a group of students had taken over two tables. They were playing cards and arguing about the rules, which seemed to change every few minutes. An old man in a green coat sat alone by the window, writing in a notebook with a short pencil. Every so often he stopped, looked out at the black water, and then went back to writing, as if the sea were dictating something to him one sentence at a time.\n\nMarta bought a cup of tea from the small counter at the back. The woman serving it had a badge with her name, Ilse, and the tired smile of someone who had answered the same questions thousands of times. "Calm night," Marta said. "For now," Ilse answered, and pointed at a screen above the counter. It showed a simple map: the coastline, a dotted line for the route, and a tiny arrow for the ferry, already a quarter of the way across.\n\nBack on deck, the wind had grown a little stronger. The lighthouse on the northern cape blinked twice, paused, and blinked twice again. Marta counted the seconds between the flashes without thinking about it. Her grandfather had taught her that every lighthouse along this coast had its own pattern, so that a sailor who knew the patterns could tell exactly where he was, even on a night without stars. It was, he used to say, a kind of secret language that everyone was allowed to learn.\n\nAround one o\'clock the island appeared: first a faint glow, then a cluster of lights, and finally the dark outline of the hills behind the port. The engines changed their tone. Crew members in orange jackets walked along the deck, checking ropes and calling to each other in short, practiced phrases. The students packed their cards away. The old man closed his notebook, put the pencil behind his ear, and stood up slowly, holding the back of his chair.\n\nWhen the ramp finally came down, Marta was one of the last to leave. She paused at the top, looked back at the empty deck, and listened for a moment to the quiet ticking of the cooling engines. Then she picked up her bag and walked down into the island night, where the air smelled of pine trees and the only sound was the sea.\n'


## 3.
Przesunięcie wynosi 233

Sprawdziłam wszystkie 256 możliwych przesunięć <0,255> i obliczyłam dla każdego z nich udział bajtów odpowiadających drukowalnym znakom ASCII, tabulatorom i końcom wiersza. Następnie z 5 kandydatów o najwyższym wskaźniku ręcznie wybrałam rozwiązanie, dla którego otrzymny tekst jest sensowny. 
Obliczenie udziału znaków drukowalnych i wybranie najbardziej prawdopodobnych kandydatów pozwoliło uniknąć konieczności analizy wszystkich tekstów dla możliwych przesunięć.

Sama entropia histogramu wartości 0-255 nie rozstrzygnie, które przesunięcie jest poprawne, ponieważ przy przesunięciu modulo 256 entropia się nie zmienia - zmieniają się jedynie wartości bajtów, natomiast ich liczebność(histogram) pozostają takie same.


# Zadanie 2
## 1.
Zaszyfrowany plik znajduje się w pliku vigenere.bin

Rezultaty sprawdzeń zgodności:
True
Empty:
True
0 i 255:
True

## 2.

Klucz SZYFR:
95ac9a9393
95ac9a9393
95ac9a9393

Klucz KOD:
8da1859890
869d90918c
91968c9c85

## 3.
Klucz SZYFR ma długość 5 - podobnie jak BRAMA powtarzające się trzykrotnie w szyfrowanym ciągu. W szyfrze Vigenere dla każdego znaku do jego bajtowej wartości dodajemy key[i % len(key)]. Dzięki temu każde wystąpienie słowa BRAMA jest szyfrowane tymi samymi kluczami, przez co otrzymujemy trzykrotnie wartość szesnastkową 95ac9a9393. 
Klucz KOD ma długość 3 bajtó, więc tutaj ta regularność już nie występuje i kolejne wystąpienia słowa BRAMA zaczynają się na różnych pozycjach względem klucza.


# Zadanie 3

## 1.
Zaimplementowałam RC4 i przetestowałam dla klucza "abc" i bajtów 3, 165, 18, 0, 255 => decrypted == data zwraca True, zatem dwukrotne zastosowanie funkcji z tym samym kluczem odtwarza wejście

## 2.
Klucz: tat, entropia: 4.391044
Klucz: neg, entropia: 7.430376
Klucz: mcn, entropia: 7.451232
Klucz: oxo, entropia: 7.453574
Klucz: tnx, entropia: 7.459153
Wybrany klucz: tat
Liczba prób: 17576

## 3. 
Odszyfrowany tekst:
The Clockmaker's Apprentice

On his first day in the workshop, Tomas was not allowed to touch a single clock. The old clockmaker, a quiet woman named Helena Varga, handed him a broom, a soft brush, and a small wooden box with compartments, and told him to clean the bench and sort the screws by size. "If you cannot find the right screw," she said, "you will never find the right fault."

The workshop occupied a narrow room above a bakery, so that in the early morning the smell of warm bread rose through the floorboards and mixed with the smell of oil and brass. Along the walls hung dozens of clocks, each showing a slightly different time. At first Tomas thought this was carelessness. Later he understood that every clock was there for a reason: some were waiting for parts, some were being tested, and some had simply been forgotten by their owners.

For two weeks he sorted screws, cleaned tools, and watched. He learned that a clock is not one machine but a conversation between several. The spring stores the energy, the gear train passes it on, the escapement releases it in small, equal portions, and the pendulum or balance wheel decides how long each portion should last. If one part speaks too quickly or too slowly, the whole conversation falls apart.

In the third week Helena gave him a cheap kitchen clock that had stopped. "Tell me why," she said, and went downstairs to buy bread. Tomas opened the case, laid out the parts on a white cloth, and examined each one under the magnifying lamp. The spring was fine. The gears turned freely. It took him almost an hour to notice a hair, a single long hair, wound around the axle of the escape wheel. He removed it with tweezers, put everything back together, and the clock began to tick.

When Helena returned, she listened to the clock for a while without saying anything. Then she nodded. "Most faults are small," she said. "The difficult part is believing that they are small, and looking carefully anyway."

Over the following months Tomas repaired alarm clocks, wall clocks, and a heavy brass carriage clock that had travelled across three countries in a suitcase. He began to recognize the sound of a healthy movement and the slightly uneven beat of one that needed attention. He also learned to keep a notebook, writing down every step of every repair, because a week later he would no longer remember which wheel had come out first.

One winter evening a customer brought in a clock that had belonged to his grandfather. It was not valuable, he explained, but it had stood in the same hallway for sixty years, and the house felt wrong without its sound. Tomas worked on it for three evenings. When he finally returned it, the man stood in the doorway of the workshop for a long time, just listening, and then thanked him in a voice that was not quite steady.

That night Tomas understood what Helena had meant on his first day. The work was not really about clocks. It was about patience, about small things, and about the people who waited for them to start ticking again.


## 4.
Wybrany klucz: tat

Kandydaci:
Klucz: tat, entropia: 4.391044
Klucz: neg, entropia: 7.430376
Klucz: mcn, entropia: 7.451232
Klucz: oxo, entropia: 7.453574
Klucz: tnx, entropia: 7.459153

Liczba prób: 17576
Czas przeszukiwania: 4.0127664000010554 s

Entropia kryptogramu: 7.927094
Entropia odszyfrowania: 4.325867

Ponowne szyfrowanie może odtworzyć kryptogram również dla błędnego klucza, ponieważ RC4 wykorzystuje operację XOR, która zastosowana dwukrotnie z tym samym kluczem przywraca dane wejściowe. 
Ranking entropii może zawieść, gdy np. tekst ma nietypowy rozkład bajtów lub jest krótki - wtedy nie musi on mieć najniższej entropii spośród kandydatów