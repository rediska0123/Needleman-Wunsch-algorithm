# Needleman-Wunsch-algorithm
Implementation of [Needleman–Wunsch algorithm](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm).

## Initialization
Please install the packages before trying out the alrorithm. Run the following:

```shell script
pip3 install requirements.txt
```
 or manually install each package provided in `requirements.txt` file.

##Usage
For executing the algorithm provide input data in `input.txt` in the following format:

```
<score matrix, 4*4 integers>
<d, integer>
<first dna sequence (contains only A, G, C, T)>
<second dna sequence (only A, G, C, T)>
```

E.g.:

```
10 -1 -3 -4
-1 7 -5 -3
-3 -5 9 0
-4 -3 0 8
-5
GTTACAA
GACGTTT
```
Represents scoring matrix:

|   | A  | G  | C  | T  |
|---|----|----|----|----|
| A | 10 | -1 | -3 | -4 |
| G | -1 | 7  | -5 | -3 |
| C | -3 | -5 | 9  | 0  |
| T | -4 | -3 | 0  | 8  |

`d = -5`, two DNA sequences: `GTTACAA`, `GACGTTT`.

Run `needleman_wunsch.py`, which would output the highest score possible and the alignment for this score:

```shell script
>> python3 needleman_wunsch.py
Score:  1.0
GTTACAA--
G--ACGTTT
```

## Tests

For testing run

```shell script
pytest
```