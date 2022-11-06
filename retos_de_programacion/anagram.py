import sys

def is_anagram(word1, word2):
	
	word1_list = list(word1.lower())
	word2_list = list(word2.lower())
	if word1_list == word2_list:
		print( "They are the same words" )
	
	elif sorted(word1_list) == sorted(word2_list):
		
		print("They are anagrams")
	else:
		 print("They aren't anagrams")


if __name__ == "__main__":
	
	if len(sys.argv) == 3:
		is_anagram(sys.argv[1], sys.argv[2])
	else:
		print("El programa trabaja con 2 argumentos")
		sys.exit(1)
