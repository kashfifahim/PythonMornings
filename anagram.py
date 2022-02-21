import timeit
#  Write a function that takes two words
#  and returns True if they are anagrams

def is_anagram(word1, word2):
  w_list1 = list(word1)
  w_list1 = sorted(w_list1)
  w_list2 = list(word2)
  w_list2 = sorted(w_list2)

  if len(w_list1) != len(w_list2):
    return False
 
  for i in range(0, len(w_list1)):
    if w_list2[i] != w_list1[i]:
      return False

  return True


#  Test function
print(timeit.timeit(str(is_anagram('tachymetric', 'mccarthyite'))))
print(timeit.timeit(str(is_anagram('post', 'top'))))
print(timeit.timeit(str(is_anagram('pott', 'top'))))
print(timeit.timeit(str(is_anagram('top', 'post'))))
print(timeit.timeit(str(is_anagram('topss', 'postt'))))
