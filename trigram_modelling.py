import glob
import math
import os


class ngram_model():

    def __init__(self):
        self.texts = glob.glob("gutenberg/*")
        self.test_texts = glob.glob("test_data/*")

    def preprocess(self):
        output = ""
        for file in self.texts:
            with open(os.path.join(os.getcwd(), file), 'r', encoding="utf-8-sig", errors='ignore') as suffix:
                sentence = suffix.read().split('\n')
                for line in sentence:
                    output += " " + line
        return output

    def ngrams(self, text, n):
        Ngrams = []
        for i in range(len(text)): Ngrams.append(text[i: i + n])
        return Ngrams

    def UNK_treated_ngram_frequency(self, ngram_list):
        frequency = {}
        for ngram in ngram_list:
            if ngram in frequency:
                frequency[ngram] += 1
            else:
                frequency[ngram] = 1

        sup = 0
        result = {}

        for k, v in frequency.items():
            if v >= 5:
                result[k] = v
            else:
                sup += v
        result["UNK"] = sup
        # print(result)
        return result

    def perplexity(self, total_log_prob, N):
        perp = math.exp(-1 * total_log_prob / N)
        return perp

    def ngram_model_laplace_k(self, trigram, k):
        laplace_one_probs = []
        bigram = self.UNK_treated_ngram_frequency(self.ngrams(self.preprocess(), 2))
        vocabulary = len(self.UNK_treated_ngram_frequency(self.ngrams(self.preprocess(), 3)))
        for trigram_value, trigram_count in trigram.items():
            try:
                prob = (trigram_count + k) / (bigram[trigram_value[:-1]] + (k * vocabulary))
                sum_prob = ++prob
            except KeyError:
                prob = (trigram_count + k) / (bigram["UNK"] + (k * vocabulary))
                sum_prob = ++math.log(prob)
            laplace_one_probs.append([trigram_value, prob])
        prep = self.perplexity(sum_prob, len(trigram_value))
        print(prep)
        return laplace_one_probs

    def open_file(self, file):
        output = ""
        # with open(os.path.join(os.getcwd(), "test_data/",file), 'r', encoding="utf-8-sig", errors='ignore') as suffix:
        with open(os.path.join(os.getcwd(), file), 'r', encoding="utf-8-sig", errors='ignore') as suffix:
            sentence = suffix.read().split('\n')
            for line in sentence:
                output += " " + line
        return output

    def test(self):
        # filenames = random.sample(os.listdir('test_data'), 100)
        # for file in self.test_texts:
            # print(file)
        output ="When it comes to the decision itself, according to the Treaty there is no method other than the Intergovernmental Conference. It is important that we remember this, just as Mrs BerÃšs said just now. I understand that Parliament is very interested, as I am, in the important discussion on how we will reach a decision - the debate we will have before the decision, how we will prepare for the debate, and the role which might be played by the convention method. These issues were addressed by the initial speakers. The discussion in Parliament shows that we must have a broad debate on these matters, but I think it is too early today to reach a definite position as there are both advantages and disadvantages. The advantages are clear - an open debate and broad participation - but here too questions can be raised. Who is to be involved - Member States, candidate countries and organisations, and if so, which? We cannot reach a final position on this today. Some have also put forward the disadvantages. With very many participants, the process can become unwieldy. Furthermore, the decision-making process itself can be unclear, as the convention submits proposals and the Intergovernmental Conference has to reach decisions. Even if one advocates a convention, one must also discuss dealing with its disadvantages. We should therefore discuss this properly and in detail. The Council has not said yes but nor has the Council objected, and we have definitely not said that we are afraid of a convention. We have said that we must now be able to discuss both the factual issues surrounding the future of Europe and the methods - including the question of a convention. Just as Mr Brok and others said, the European Parliament is naturally involved in this entire debate. You played a part in initiating the debate on the future. You played a part in the launch and you are also among those participating in the website. I do not know exactly where Mr Elles has been looking, but I can guarantee that Parliament is represented. Furthermore, there are lots of contributions, so if Parliament was not represented there today, it can only be an oversight. This debate is a further example of Parliament' s being involved, but we would also like to see the view of Parliament as a whole on the debate on the future, and we will get that in May. Therefore, I think it is important that this also be included as part of the on-going discussion. Let me now comment on some other issues. Mr Cox wondered why I said that the Treaties should be simplified without changing the content. I reply that I was quoting the Nice Decision. To Mr BarÃ³n Crespo I would like to say that it is clear that we must go out into the real world. I myself have taken the debate to many Swedish schools. I presume that you others too have also visited schools. I think it is important that, here too, Parliament is really involved in the debate on content. What schoolchildren and the general public will ask us will naturally be questions which are very much wider in scope than those we have discussed here today. I would also like to say to Mr BarÃ³n Crespo that of course Parliament was invited to take part in launching the future of Europe right from the start. To Mrs Frassoni I would like to say that when it comes to the question on civil society, there must unfortunately have been some problem with the translation, for the Swedish Presidency has exhibited a very great interest in civil society. In my introductory speech, I cited examples of major conferences we are organising in Sweden and in other countries. Ahead of the summit in Gothenburg we are organising three broad forums arranged by civil society. We are also working on town twinning to a great extent and are doing a great deal of work at many schools and universities. I personally have several school classes as reference groups, which I can recommend, by the way. Mr Bonde brought up the subject of the website and said that only Prime Minister Persson and other high-up figures are allowed to write on it. I recommend that he go and look at it as there are already many contributions there. Among other things in my introductory speech, I quoted contributions from Denmark and the UK - opinions of ordinary citizens in both countries. This is naturally an important debate for the future. I expect we will return to the discussion of the methods and the convention and how we can best broaden the debate. But it is also important that we have a broad debate on the factual issues, i.e. on how Europe really will be able to address globalisation and on how Europe can become a strong force on employment, environmental issues and the matters we will be discussing later today. So when it comes to the future of Europe, let us discuss both methods and substance. Mr President, ladies and gentlemen, with thanks to each and every one of you, I would like at this stage to comment briefly on a few specific questions put by a number of you. As for the rest, I can only confirm on behalf of President Prodi, and on my own personal behalf, that the Commission will continue to work intelligently and in close cooperation with the European Parliament during this rather sensitive period of the debate on the future of Europe, as Mrs BerÃšs said. And that is what counts. Mrs Lindh has just said a few words about the website, which several of you have mentioned, most notably James Elles and Mrs MalmstrÃ¶m. This site is going through a running-in phase so please show a little understanding. It was opened barely a week ago. I think all your comments will help us to turn it into a real website for the people. Furthermore, our idea is to share the management of this site amongst several institutions, including the European Parliament, but I admit that we must push it forwards and perhaps also understand its role better, as it must be used as a platform for the national debates which will soon be organised in each Member State. That is my first reply, but this site must be improved and the Commission will make a contribution to make this happen. Mr Seguro asked a question of the President of the Commission and the Commissioner. Yes, Mr Seguro, we are going to continue to meet with the governments in each of the capitals not only of the Member States but, as Mr Prodi has done, as each of us does, the capitals of the candidate countries too. This is the role of the President, which he carries out not only with regard to the debate on the future of Europe, but on many other subjects as well. I would add that we will also continue to meet with national parliaments, which has not been normal practice for the Commission up till now. In the context of the debates in the run-up to Nice, I personally was concerned to meet with national parliaments and, quite frankly, I do not regret it at all. Mr Leinen mentioned, as did Mr Dupuis, the concern we expressed through our President that 2004 will be an extremely busy year. It is the year in which we will table the new post-Berlin agenda. It is the year in which many accession negotiations will be concluded, if this has not already happened. It is the year of the renewal of the European Parliament and it is also the final year of this Commission. So the sooner we can move, at the start of 2004 and perhaps, Mr Leinen, why not in Rome at the end of 2003, the better it will be for everybody, for us and for you, and so necessarily for the European debate itself. The answer to that, however, is also in the hands of the Heads of State and Government. I would like to thank each and every one of you, especially the group chairpersons who expressed their desires and their agreement with the ideas or the guidelines of the Commission. We will continue to work together. Please allow me to say a final personal word of thanks to Mr Desama at this moving time when he is about to leave this House to take up more local responsibilities in Verviers. I am sure he will not forget the profession of European faith he has carried out here when he assumes his role of Lord Mayor in the weeks to come. Mr President, on a point of order I should like to put on record a matter I raised at the Conference of Presidents."
        # print(output)
        return self.ngram_model_laplace_k(self.UNK_treated_ngram_frequency(self.ngrams(output, 3)), 5)

p = ngram_model()
print(p.test())
