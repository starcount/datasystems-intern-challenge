def with_skip_not_implemented(func):
    def func_wrapper(self):
        try:
            func(self)
        except NotImplementedError:
            self.skipTest("Not implemented yet") 
    return func_wrapper

