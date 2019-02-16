from random import choices
from string import ascii_letters, digits


DEFAULT_CANDIDATES = ascii_letters + digits


def random_str(length, candidates=DEFAULT_CANDIDATES):
    return ''.join(choices(candidates, k=length))


class FilterModule(object):
    ''' Query filter '''

    # test with
    #   ansible -m debug -a 'msg="{{ 8 | random_password }}"' server

    def filters(self):
        return {
            'random_password': random_str,
        }
