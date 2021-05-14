class Solution:
    def isValid(self, s: str) -> bool:
        brackets_mirror = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        bracket_options = {
            'needed_brackets': [],
        }

        def checker(symbol):
            if symbol in brackets_mirror:
                bracket_options['needed_brackets'].append(brackets_mirror[symbol])
            else:
                if symbol != bracket_options['needed_brackets'][-1]:
                    raise Exception
                bracket_options['needed_brackets'].pop()

        try:
            list(map(checker, s))
        except:
            return False

        return False if len(bracket_options['needed_brackets']) else True


