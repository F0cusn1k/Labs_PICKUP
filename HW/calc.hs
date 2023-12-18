-- Пользовательский тип данных ошбики(либо слишком мало чисел, либо произошло деление на ноль)
data Error = StackTooShort Int Int | DividingByZero deriving Show 

-- Функция показа ошбики, выводит на экран ошибку с пояснением
showErr (StackTooShort a b) = "Stack has " ++ show a ++ " elements. " ++ show b ++ " needed"
showErr (DividingByZero) = "You divided by zero!"

-- Пользовательский тип данных токен, в который производится ввод и который может быть целым числом, либо действием между числами
data Token = Number Int | Plus | Minus | Div | Mul deriving Show

-- Функция для извлечения значения из типа Maybe
numm (Just x) = x

-- data Either a b = Left a | Right b

-- Функция, принимающая список чисел, которая возвращает список со сложенными первыми двумя числами(в случае нехватки чисел возвращает ошибку)
add [] = Left (StackTooShort 0 2)
add (x:[]) = Left (StackTooShort 1 2)
add (x1:x2:xs) = Right ((x1+x2):xs)

-- Вычитание. Аналогично add
sub [] = Left (StackTooShort 0 2)
sub (x:[]) = Left (StackTooShort 1 2)
sub (x1:x2:xs) = Right ((x1-x2):xs)
--sub (x1:x2:xs) = Right ((x2 - x1):xs)

-- Целочисленное деление. Аналогично add
div' [] = Left (StackTooShort 0 2)
div' (x:[]) = Left (StackTooShort 1 2)
div' (x1:x2:xs) = if x2/=0 then Right ((div x1 x2):xs) else Left DividingByZero
--div' (x1:x2:xs) = if x2/=0 then Right ((div x2 x1):xs) else Left DividingByZero

-- Деление. Аналогично add
divide [] = Left (StackTooShort 0 2)
divide (x:[]) = Left (StackTooShort 1 2)
divide (x1:x2:xs) = if x2/=0 then Right ((x1/x2):xs) else Left DividingByZero

-- Умножение. Аналогично add
mul [] = Left (StackTooShort 0 2)
mul (x:[]) = Left (StackTooShort 1 2)
mul (x1:x2:xs) = Right ((x1*x2):xs)

-- Функция преобразования токена и списка целых чисел в список чисел
-- Если внутри токена оператор, то он выполняется
-- Если внутри токена число, то оно присоединяется к списку
operation :: Token -> [Int] -> Either Error [Int]
operation Plus a = add a
operation Minus a = sub a
operation Div a = div' a
operation Mul a = mul a
operation (Number a) b = Right (a:b)

-- Функция преобразования строки в число
parseInt :: String -> Maybe Int
parseInt str = h (reads str) -- reads разбивает строку на пары
  where
    -- h :: [(Int, String)] -> Maybe Int
	h [(a, b)] = if b=="" then Just a else Nothing
	h _ = Nothing

-- Функция, разбивающая входную строку на слова и преобразующая их в токен
convert a = convert' (words a)
  where
	convert' [] = []
	convert' (x:xs) = (if (x=="+") then Plus else if (x=="-") then Minus else if (x=="/") then Div else if (x=="*") then Mul else Number (numm (parseInt x))) : (convert' xs)

-- Функция, которая принимает стек целых чисел и список токенов, а затем выполняет операции, представленные токенами, на значениях стека
calc :: [Int] -> [Token] -> Either Error [Int]
calc stack [] = Right stack
calc stack (op:ops) = do
	stack <- operation op stack
	calc stack ops

-- Функция вывода результата
ret:: Either Error [Int] -> String
ret (Left a) = showErr a
ret (Right (x:xs)) = show x


--pr1:: [Token] -> [Int]
--pr1 ((Number x) : xs) = x : pr1 xs
--pr1 (x) = []

-- Функция, которая принимает список токенов и возвращает новый список токенов, содержащий только цифровые токены (числа)
pr1:: [Token] -> [Token]
pr1 ((Number x) : xs) = (Number x) : (pr1 xs)
pr1 (x) = []

-- Функция, которая принимает список токенов и возвращает список токенов, содержащий только операции
pr2:: [Token] -> [Token]
pr2 (Plus:xs) = Plus : pr2 xs
pr2 (Minus:xs) = Minus : pr2 xs
pr2 (Div:xs) = Div : pr2 xs
pr2 (Mul:xs) = Mul : pr2 xs
pr2 (x:xs) = pr2 xs
pr2 [] = []

-- Функция, переворачивающая список
reverseList [] = []
reverseList (x:xs) = reverseList xs ++ [x]


--runProgram a = (ret (calc [] (convert a)))


-- Запуск программы (преобразуем все слова в токены, разбиваем токены на числа и операции раздельно, а затем переворачиваем список, чтобы операции оказались сверху)
runProgram a = (ret (calc [] ( (reverseList (pr1 (convert a))) ++ ( pr2 (convert a) ) )))

-- Ввод данных
interact' :: (String -> String) -> IO ()
interact' f = do
	a <- getLine
	putStrLn (f a)
	interact' f
	
-- Запуск
main = interact' runProgram








	
	
	