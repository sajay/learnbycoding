#Write a script poetry.py that will generate a poem based on randomly chosen words and
#a pre-determined structure. When you are done, you will be able to generate poetic
#masterpieces such as the following in mere milliseconds:
#A furry horse
#A furry horse curdles within the fragrant mango extravagantly, the horse slurps
#the mango meows beneath a balding extrovert
#All of the poems will have this same general structure, inspired by Clifford Pickover:
#{A/An} {adjective1} {noun1}
#{A/An} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}
#{adverb1}, the {noun1} {verb2}
#the {noun2} {verb3} {preposition2} a {adjective3} {noun3}
#Your script should include a function makePoem() that returns a multi-line string representing a complete poem. 
#The main section of the code should simply print makePoem() to display a single poem. In order to get there, use the following steps as a
#guide:
#1. First, you'll need a vocabulary from which to create the poem. Create several lists,
#each containing words pertaining to one part of speech (more or less); i.e., create
#separate lists for nouns, verbs, adjectives, adverbs, and prepositions. You will need
#to include at least three different nouns, three verbs, three adjectives, two
#prepositions and one adverb. You can use the sample word lists below, but feel free
#to add your own:
#Nouns: "fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert","gorilla"
#Verbs: "kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"
#Adjectives: "furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"
#Prepositions: "against", "after", "into", "beneath", "upon", "for", "in", "like", "over","within"
#Adverbs: "curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"
#2. Choose random words from the appropriate list using the random.choice() function,
#storing each choice in a new string. Select three nouns, three verbs, three
#adjectives, one adverb, and two prepositions. Make sure that none of the words are
#repeated. (Hint: Use a while loop to repeat the selection process until you get a new word.)
#3. Plug the words you selected into the structure above to create a poem string by using the format() string method
#4. Bonus: Make sure that the "A" in the title and the first line is adjusted to become an 
#"An" automatically if the first adjective begins with a vowel.

TODO: