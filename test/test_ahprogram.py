from testbase import TestBase
from corepro.program import Program

class TestAhProgram(TestBase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self):
        p = Program.getItem(TestBase.prepaidConn, TestBase.loggingObject)
        self.assertTrue(p.name == 'CoreProPrepaidTester')