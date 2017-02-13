def battle(soldiers):
  '''
  Args:
    soldiers: LIST - list of INTs.
    
  Out:
    STRING - "odds wins" if odd numbers are the winners,
             "even wins" if even numbers are the winners,
             "tie" if there is a tie between them.
  '''
  # Initialize counters to 0
  odds = evens = 0
  
  # Count bits, 0's for evens and 1's for odds
  for num in soldiers:
    bits = bin(num).count(str(num % 2))
    if num % 2 == 0: # if even number
      bits -= 1 # sub 1 because the bin string repr startswith extra 0b
      evens = evens + bits if num > 0 else evens - bits
    else: # if odd number
      odds = odds + bits if num > 0 else odds - bits
        
  # Check for the winner
  if odds > evens:
    return "odds win"
  elif odds < evens:
    return "evens win"
  else: 
    return "tie"
      
if __name__ == "__main__":
  test_cases = [[21, -3, 20], [7, -3, -14, 6], [17, -3, 32, -24]]
  test_answers = ["evens win", "evens win", "tie"]
  output = "{idx:<3} {expected:^10} {result:^10} {matched:^10}"
  print(output.format(idx = "No.", expected = "Expected", 
                      result = "Result", matched = "Matched"))
  for idx, (data, expected) in enumerate(zip(test_cases, test_answers), 1):
    result = battle(data)
    matched = expected == result
    print(output.format(**locals()))
        
    
    
    
    
  
