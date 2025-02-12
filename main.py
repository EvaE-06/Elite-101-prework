def count_vowels(s):
    vowels = "aeiouAEIOU"
     starting_count = 0
  
    for char in s:
        if char in vowels:
            starting_count += 1
