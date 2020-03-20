# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret = []
        cur_length_of_words = 0
        pos = 0
        for index, word in enumerate(words):
            if cur_length_of_words + len(word) + index - pos <= maxWidth:
                cur_length_of_words += len(word)
            else:
                text = ""
                spaces = maxWidth - cur_length_of_words
                base, last = divmod(spaces, max(index - pos-1, 1))
                for i in range(pos, index-1):
                    text += words[i] + " "*base + (" " if last > 0 else "")
                    last -= 1
                text += words[index-1]
                ret.append(text+" "*(maxWidth-len(text)))
                pos = index
                cur_length_of_words = len(word)
        text = " ".join(words[pos:])
        text += " "*(maxWidth-len(text))
        ret.append(text)
        return ret


def main():
    s = Solution()
    print(s.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."]
    ,maxWidth = 16))
    print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))


if __name__ == "__main__":
    main()
