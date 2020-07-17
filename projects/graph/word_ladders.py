from util import Queue

#build graph
# could filter our word list by lenght
#remember

# for every letter in word, swap out a letter in the alphabet
# if the result is in our words list, its a neighbor

# BFS

word_list = set()
for word in words:
    word_list.add(word.lower())

def get_neighbors(start_word):
    neighbors = []
    #for word_letter in word:
    for letter_index in range(len(start_word)):
        for letter in string.ascii_lowercase:
            word_list = list(start_word)
            word_list[letter_index] = letter

            word = "".join(word_list)


            if word in word_list:
                neighbors.append(word)
    return neighbors


def word_ladders(start_word, end_word):
    q = Queue()

    visited = set()

    q.enqueue([start_word])

    while q.size > 0:

        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path

        if current_word not in visited:
            visited.add(current_word)

            neighbors = get_neighbors(current_word)

            for neighbor in neighbors:
                new_path = current_path + [neighbor]
                q.enqueue(new_path)
