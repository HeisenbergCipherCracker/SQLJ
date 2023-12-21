class Memelist(list):
    """
    >>> my_list = Memelist([1, 2, 3, 4, 5])

    # Use the get_list_as_generator_obj method
    >>> gen_obj = my_list.get_list_as_generator_obj(my_list)
    >>> for item in gen_obj:
        >>> print(item)

    # Use the get_list_as_generator_exp method
    >>> gen_exp = my_list.get_list_as_generator_exp(my_list)
    >>> for item in gen_exp:
        >>> print(item)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_list_as_generator_obj(self,ls:list):
        for i in ls:
            yield i
    
    def get_list_as_generator_exp(self,ls:list):
        gen_expr = (x for x in ls)
        return gen_expr
    
    def __getitem__(self, key):
        return self.get_list_as_generator_obj(super().__getitem__(key))
    
