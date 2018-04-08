from callgraphdecorator import CallGraphDecorator


@CallGraphDecorator(True)
def test1():
    print("Hello Word.")


if __name__ == '__main__':
    test1()
