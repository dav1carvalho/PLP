statistics :: String -> (String, Int)
statistics input = ([head input, '.', last input], length input)
