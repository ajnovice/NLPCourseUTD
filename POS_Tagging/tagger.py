import os
import io
import sys


class Tagger:

    def __init__(self):
        self.initial_tag_probability = None
        self.transition_probability = None
        self.emission_probability = None
        self.unique_tags = None
        self.tag_count = None
        self.front_tag=None
        self.tags_dict=None

    def load_corpus(self, path):
        if not os.path.isdir(path):
            sys.exit("Input path is not a directory")
        for filename in os.listdir(path):
            filename = os.path.join(path, filename)
            try:
                reader = io.open(filename)
                """
                YOUR CODE GOES HERE: Complete the rest of the method so that it outputs a list of lists as described in the question
                
                """
                lines = reader.readlines()
                token_pos = list()
                for line in lines:
                    if line:
                        line_pos = list()
                        word_poses = line.split()
                        for word_pos in word_poses:
                            word_pos_list = word_pos.split("/")
                            line_pos.append(tuple([word_pos_list[0],word_pos_list[1]]))
                        if line_pos:
                            token_pos.append(line_pos)
                return token_pos
            except IOError:
                sys.exit("Cannot read file")

    def initialize_probabilities(self, sentences):
        if type(sentences) != list:
            sys.exit("Incorrect input to method")
        """
        YOUR CODE GOES HERE: Complete the rest of the method so that it computes the probability matrices as described in the question
        """
        tags = list()
        words = list()
        sentence_count=0
        tag_count = 0
        front_tag = dict()
        tags_dict = dict()
        for sentence in sentences:
            if sentence:
                sentence_count+=1
                cnt=0
                for token_pos in sentence:
                    word,pos=token_pos
                    words.append(word)
                    tags.append(pos)
                    tag_count+=1
                    if pos not in tags_dict:
                        tags_dict[pos] = 1
                    else:
                        tags_dict[pos] += 1

                    if cnt==0:
                        if pos not in front_tag:
                            front_tag[pos]=1
                        else:
                            front_tag[pos]+=1
                        cnt+=1
        self.tag_count=tag_count
        self.tags_dict=tags_dict
        couple_tags_count=0
        couple_tags = dict()
        for sentence in sentences:
            if sentence:
                for index in range(len(sentence)-1):
                    couple_tags_count+=1
                    first_token_pos = sentence[index]
                    second_token_pos = sentence[index+1]
                    couple_pos = first_token_pos[1]+":"+second_token_pos[1]
                    if couple_pos not in couple_tags:
                        couple_tags[couple_pos]=1
                    else:
                        couple_tags[couple_pos]+=1
                couple_tags_count+=1

        couple_word_tag_count=0
        couple_word_tag = dict()
        for sentence in sentences:
            if sentence:
                for token_pos in sentence:
                    couple_word_tag_count+=1
                    word,pos = token_pos
                    # couple_word_pos = word+":"+pos
                    if pos not in couple_word_tag:
                        couple_word_tag[pos]=[word]
                    else:
                        couple_word_tag[pos].append(word)

        initial_tag_probability = dict()
        unique_tags = tuple(set(tags))
        self.unique_tags=unique_tags
        for tag in unique_tags:
            if tag not in front_tag:
                initial_tag_probability[tag]=1/(sentence_count+tag_count)
            else:
                initial_tag_probability[tag]=(front_tag.get(tag)+1)/(sentence_count+tag_count)
        self.initial_tag_probability=initial_tag_probability

        transition_probability = dict()
        for first_tag in unique_tags:
            for second_tag in unique_tags:
                couple_pos=first_tag+":"+second_tag
                if couple_pos not in couple_tags:
                    transition_probability[couple_pos]=1/(tags_dict.get(first_tag)+tag_count)
                else:
                    transition_probability[couple_pos] = (1+couple_tags.get(couple_pos) )/ (tags_dict.get(first_tag)+tag_count)
        self.transition_probability=transition_probability

        emission_probability = dict()
        unique_words = list(set(words))
        for tag in unique_tags:
            for word in unique_words:
                pos_couple = tag + ":" + word
                if tag not in couple_word_tag:
                    emission_probability[pos_couple]=1/(tag_count+tags_dict.get(tag))
                else:
                    emission_probability[pos_couple] = (1 +couple_word_tag.get(tag).count(word))/ (tag_count+tags_dict.get(tag))

        self.emission_probability=emission_probability


    def viterbi_decode(self, sentence):
        if type(sentence) != str:
            sys.exit("Incorrect input to method")
        """
        YOUR CODE GOES HERE: Complete the rest of the method so that it computes the most likely sequence of tags as described in the question
        """

        sentence_list = sentence.split(" ")
        result = list()
        mostProbable = 0.0
        mostProbableTag=None
        for unique_tag in self.unique_tags:
            pos_word = unique_tag+":"+sentence_list[0]
            if pos_word in self.emission_probability:
                em=self.emission_probability.get(pos_word)
            else:
                em = 1/(self.tags_dict.get(unique_tag)+self.tag_count)
            localProbable = em*self.initial_tag_probability[unique_tag]
            if localProbable>=mostProbable:
                mostProbable=localProbable
                mostProbableTag=unique_tag
        result.append(mostProbableTag)

        for index in range(1,len(sentence_list)):
            mostProbable = 0.0
            mostProbableTag = None
            for unique_tag in self.unique_tags:
                pos_word = unique_tag + ":" + sentence_list[index]
                if pos_word in self.emission_probability:
                    ep = self.emission_probability.get(pos_word)
                else:
                    ep = 1 / (self.tags_dict.get(unique_tag) + self.tag_count)

                tag_tag = result[-1]+":"+unique_tag
                if tag_tag in self.transition_probability:
                    tp = self.transition_probability.get(tag_tag)
                else:
                    tp = 1/(self.tag_count+self.tags_dict.get(result[-1]))
                localProbable = ep * tp
                if localProbable >= mostProbable:
                    mostProbable = localProbable
                    mostProbableTag = unique_tag
            result.append(mostProbableTag)
        return result


if __name__ == "__main__":
    corpus_path = sys.argv[1]
    sentence = sys.argv[2]
    tagger = Tagger()
    token_pos=tagger.load_corpus(corpus_path)
    tagger.initialize_probabilities(token_pos)
    sequence_of_tags = tagger.viterbi_decode(sentence)
    print(sequence_of_tags)