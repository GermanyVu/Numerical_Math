
class Integration:
    def __init__(self, initial_limit, final_limit,number_slices = None,
                                                        accepted_error = None):
        self.initial_limit = initial_limit
        self.final_limit = final_limit
        self.number_slices = number_slices if number_slices is not None else 10
        self.error = accepted_error if accepted_error is not None else .0001
        self.h = abs(initial_limit - final_limit)/self.number_slices

    def __repr__(self):
        return str(self.__class__.__name__) + '({0},{1},{2},{3})' \
               .format(self.number_slices, self.initial_limit,self.final_limit \
               ,self.error)
    def double_it(self):
        self.number_slices = 2 *self.number_slices
        self.h = self.h/2
