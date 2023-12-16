--ZAD1
SELECT STANOWISKO
,AVG(PENSJA) SREDNIE
,MIN(PENSJA) MINIMALNE
,MAX(PENSJA) MAKSYMALNE
FROM PRACOWNIK
GROUP BY STANOWISKO

--ZAD2
SELECT MIN(PENSJA) MINIMALNA, MAX(PENSJA) MAKSYYMALNA FROM PRACOWNIK;

--ZAD3
SELECT STANOWISKO, COUNT(1) ILE
FROM PRACOWNIK
WHERE STANOWISKO = 'ANALITYK'
GROUP BY STANOWISKO
--ZAD4

SELECT D.NAZWA, COUNT(1) ILE
FROM DEPARTAMENT D
LEFT JOIN PRACOWNIK P
    ON D.NR_DEPARTAMENTU = P.NR_DEPARTAMENTU
GROUP BY D.NAZWA
ORDER BY D.NAZWA, ILE DESC;

--ZAD5

SELECT D.NAZWA, NVL(AVG(PENSJA),0) AS "SREDNIA PENSJA"
FROM DEPARTAMENT D
LEFT JOIN PRACOWNIK P
    ON D.NR_DEPARTAMENTU = P.NR_DEPARTAMENTU
GROUP BY D.NAZWA
ORDER BY "SREDNIA PENSJA" DESC;

--ZAD6

SELECT D.NAZWA,COUNT(*)
FROM DEPARTAMENT D
LEFT JOIN PRACOWNIK P
    ON D.NR_DEPARTAMENTU = P.NR_DEPARTAMENTU
GROUP BY D.NAZWA
HAVING COUNT(*) > 3;

--ZAD7
SELECT D.NAZWA,COUNT(*) ILE
FROM DEPARTAMENT D
LEFT JOIN PRACOWNIK P
    ON D.NR_DEPARTAMENTU = P.NR_DEPARTAMENTU
WHERE UPPER(D.LOKALIZACJA) IN ('WARSZAWA','BIALYSTOK')
GROUP BY D.NAZWA
HAVING COUNT(*) > 3;

--ZAD8

SELECT D.NAZWA,P.STANOWISKO, COUNT(ID_PRACOWNIKA) ILE
FROM DEPARTAMENT D
LEFT JOIN PRACOWNIK P
    ON D.NR_DEPARTAMENTU = P.NR_DEPARTAMENTU
GROUP BY D.NAZWA,P.STANOWISKO

--ZAD9

SELECT A.ID_PRACOWNIKA, COUNT(B.ID_PRACOWNIKA) ILE
FROM PRACOWNIK A
LEFT JOIN PRACOWNIK B
    ON A.ID_PRACOWNIKA = B.ID_KIEROWNIKA
GROUP BY A.ID_PRACOWNIKA;

SELECT ID_PRACOWNIKA, ID_KIEROWNIKA, LEVEL, CONNECT_BY_ISCYCLE, SYS_CONNECT_BY_PATH(ID_PRACOWNIKA, '/')
FROM PRACOWNIK
START WITH ID_PRACOWNIKA = 10
CONNECT BY NOCYCLE PRIOR ID_PRACOWNIKA = ID_KIEROWNIKA;


--ZAD10
SELECT A.NAZWISKO, B.STANOWISKO, AVG(B.PENSJA) SREDNIA
FROM PRACOWNIK A
JOIN PRACOWNIK B
    ON A.ID_PRACOWNIKA = B.ID_KIEROWNIKA
GROUP BY A.NAZWISKO, B.STANOWISKO
ORDER BY A.NAZWISKO

SELECT D.NAZWA,MIN(P.PENSJA) MINIMALNA, MAX(PENSJA) MAKSYMALNA
FROM DEPARTAMENT D
LEFT JOIN PRACOWNIK P
    ON D.NR_DEPARTAMENTU = P.NR_DEPARTAMENTU
WHERE P.PENSJA > 3000
GROUP BY D.NAZWA
HAVING COUNT(*) > 2;