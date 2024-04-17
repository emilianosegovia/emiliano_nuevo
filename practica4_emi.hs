----------------------------------------------------------
--ejercicio 1
fibonacci :: Integer -> Integer 
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci (n-2)
-----------------------------------------------------------
--ejercicio 2
parteEntera :: Float -> Integer
parteEntera n | n < 1 && n > 0 = 0 
              | n >(-1) && n<0 = 0
              | n > 1 = parteEntera (n-1) + 1   
              | otherwise = parteEntera(n + 1) - 1
-----------------------------------------------------------
--ejercicio 3
esDivisible :: Integer->Integer-> Bool 
esDivisible n m | n == m = True
                | n > m = esDivisible n (m+m)
                | otherwise = False  
-----------------------------------------------------------
--ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = 1
              | otherwise = (2*n - 1) + sumaImpares (n-1)
-----------------------------------------------------------
--ejercicio 5
medioFact :: Integer -> Integer
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n * medioFact (n-2)
-----------------------------------------------------------
--ejercicio 6
sumaDigitos :: Integer -> Integer
sumaDigitos n | n <= 9 = n
              | otherwise = mod n 10 + sumaDigitos (div n 10)
-----------------------------------------------------------
--ejercicio 7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n <= 9 = True
                      | mod n 10 /= mod (div n 10) 10 = False
                      | otherwise = todosDigitosIguales (div n 10) 
------------------------------------------------------------
--ejercicio 8
cantidadDeDigitos :: Integer -> Integer
cantidadDeDigitos n | n <= 9 = 1 
                    | otherwise = 1 + cantidadDeDigitos(div n 10)
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n m = mod (div n (10^((cantidadDeDigitos n)-m))) 10
-------------------------------------------------------------
--ejercicio 9
capicua :: Integer -> Bool
capicua n | n <= 9 = True
          | div n (10^((cantidadDeDigitos n)-1)) == mod n 10 = capicua (div (mod n (10^((cantidadDeDigitos n)-1))) 10)
          | otherwise = False 
-------------------------------------------------------------
--ejercicio 10
sumatoria1 :: Integer -> Integer
sumatoria1 n | n == 0 = 1
             | otherwise = 2^n + sumatoria1 (n-1)
-------------------------------------------------------------
--ejercicio 10_b
sumatoria2 :: Integer -> Integer -> Integer
sumatoria2 n m | n == 1 = m 
               | otherwise = m^n + sumatoria2 (n-1) m
--------------------------------------------------------------
--ejercicio 10_c
sumatoria3 :: Integer -> Float -> Float
sumatoria3 n q | n == 1 = q^2 + q 
               | otherwise = q ^ (2*n) + q ^ (2*n - 1)  + sumatoria3 (n-1) q
---------------------------------------------------------------
--ejercicio 10_d
--preguntar
---------------------------------------------------------------
--ejercicio 11 
eAprox :: Integer -> Float
eAprox n | n== 0 = 1
         | otherwise = 1/(fromIntegral(factorial n)) + eAprox(n-1)

factorial :: Integer -> Integer
factorial n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n * factorial(n-1)
----------------------------------------------------------------
--ejercicio 12 
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n | n == 1 = 1
               | otherwise = 2 + 1/ (raizDe2Aprox(n-1) + 1) - 1
----------------------------------------------------------------
--ejercicio 13
sumatoriaAux :: Integer -> Integer
sumatoriaAux n | n == 1 = 1
               | otherwise = n + sumatoriaAux(n-1)

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble n m  | n == 1 = m 
                    | m == 1 = sumatoriaAux n
                    | otherwise  = n ^ m + sumatoriaDoble n (m - 1) + (sumatoriaDoble (n-1) m) - sumatoriaDoble (n-1) (m-1)

sumatoriaDoble1 :: Integer -> Integer -> Integer
sumatoriaDoble1 n m | n == 1 = (sumatoria2 n m)
                    | otherwise = (sumatoria2 n m) + (sumatoriaDoble1 (n-1) m)
----------------------------------------------------------------
--ejercicio 14
--sumaPotencias :: Integer -> Integer -> Integer -> Integer
--sumaPotencias q n m | 
--                    | otherwise = q ^ (n+m) + sumaPotencias q sumatoria2(q n) (m-1)
--sumaPotenciasAux :: Integer -> Integer -> Integer
--sumaPotenciasAux n m | n 
-----------------------------------------------------------------
--ejercicio 16
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde 2 n
menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde m n | mod n m == 0 = m
                      | otherwise = menorDivisorDesde (m+1) n
------------------------------------------------------------------

