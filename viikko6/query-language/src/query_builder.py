from matchers import *


class QueryBuilder:
    def __init__(self, query_object=All()):
        self._query_object = query_object

    def playsIn(self, team):
        return QueryBuilder(And(self._query_object, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query_object, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query_object, HasFewerThan(value, attr)))

    def build(self):
        return self._query_object
