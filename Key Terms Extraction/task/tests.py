from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from test.news import news_text

answer = {'Brain Disconnects During Sleep:': ['the', 'of', ',', '.', 'that'],
          'New Portuguese skull may be an early relative of Neandertals:': ["of", "the", ",", "in", "a"],
          'Living by the coast could improve mental health:': ['the', 'to', ',', '.', 'health'],
          'Did you knowingly commit a crime? Brain scans could tell:': ['the', ',', '.', 'of', 'a'],
          'Computer learns to detect skin cancer more accurately than doctors:': [",", "the", "of", ".", "in"],
          'US economic growth stronger than expected despite weak demand:': ["the", ",", "in", "of", "to"],
          'Microsoft becomes third listed US firm to be valued at $1tn:': ["the", ".", "to", ",", "microsoft"],
          "Apple's Siri is a better rapper than you:": [",", ".", "'s", "the", "and"],
          'Netflix viewers like comedy for breakfast and drama at lunch:': [",", "the", "of", ".", "a"],
          'Loneliness May Make Quitting Smoking Even Tougher:': [",", "to", ".", "the", "that"]}


class KTETest(StageTest):
    def generate(self):
        with open('news.xml', 'w') as file:
            file.write(news_text)
        return [TestCase()]

    def check(self, reply, attach):
        lines = reply.split('\n')
        while ("" in lines):
            lines.remove("")
        headers = lines[::2]
        text = lines[1::2]
        news_text = []
        for row in text:
            row = row.split(' ')
            while ("" in row):
                row.remove("")
            news_text.append(row)
        news = {}
        if len(news_text) != len(headers):
            return CheckResult.wrong(feedback="The number of headers should be equal "
                                              "to the number of lines with keywords.\n"
                                              "Please check the output of your program.")

        for i in range(len(headers)):
            news[headers[i]] = news_text[i]
        wrong_news = []
        wrong_head = []
        ans = list(answer.items())
        new = list(news.items())
        for i in range(len(ans)):
            if len(answer) != len(news):
                return CheckResult.wrong(
                    feedback="Something is wrong with output. Probably, you have forgotten to print some news? Try again")

            if ans[i][1] != new[i][1]:
                wrong_news.append(new[i][0])
            if ans[i][0] != new[i][0]:
                wrong_head.append(new[i][0])
        if len(answer) != len(news):
            return CheckResult.wrong(
                feedback="Something is wrong with output. Probably, you have forgotten to print some news? Try again")
        if len(wrong_head) != 0:
            return CheckResult.wrong(
                feedback='Incorrect headers are found in your output. \n'
                         'The following headers are incorrect:\n'
                         '{0}'.format('\n'.join(wrong_head)))
        if len(wrong_news) != 0:
            return CheckResult.wrong("Keywords are found incorrectly in {0} of {1} news texts.\n"
                                     "Keywords are found incorrectly in the following texts:\n\n"
                                     "{2}".format(len(wrong_news), len(news), '\n'.join(wrong_news)))

        return CheckResult.correct()


if __name__ == '__main__':
    KTETest().run_tests()
