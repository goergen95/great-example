class foo:
    """Parent class.

    A parent class with a single parameter.

    Parameters
    ----------
    foo
        An integer. Defaults to 1.
    """
    def __init__(self, foo: int = 1) -> None:
        self.foo = foo

    def a(self, bar: int = 1) -> int:
        """Returns foo + bar.

        Adds foo and bar together.

        Parameters
        ----------
        bar
            An integer to be added to foo. Defaults to 1.
        """
        return self.foo + bar


class bar(foo):
    """Child class.

    A child class adding another parameter.

    Parameters
    ----------
    bar
        A string. Defaults to 'bar'.
    kwargs
        Keyword arguments of parent class `foo`.
    """
    def __init__(self, bar: str = "bar", **kwargs) -> None:
        super().__init__(**kwargs)
        self.bar = bar

    def b(self, foo: str = "foo") -> str:
        """Returns bar + foo.

        Parameters
        ----------
        foo
            A string to be added to bar. Defaults to 'foo'.
        """
        return self.bar + foo