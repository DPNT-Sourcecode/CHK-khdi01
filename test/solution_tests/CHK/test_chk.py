from solutions.CHK import checkout_solution


class TestCHK():
    def test_chk(self):
        assert checkout.compute("A1B2C3D4") == 200

test = TestCHK()

test.test_chk()