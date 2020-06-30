import GameOfLife
import unittest


class GameOfLifeTestCase(unittest.TestCase):
    def setUp(self):
        self.mapStorage = GameOfLife.MapStorage(200, 200)
        self.lifeChanger = GameOfLife.LifeChanger()
        self.lifeCycleController = GameOfLife.LifeCycleController(0.2)

    def tearDown(self):
        print("Unit test complete!")

    def testMapStorage(self):
        assert self.mapStorage.getSize() == (200, 200), 'incorrect map size'
        life = self.mapStorage.getLife(100, 100)
        assert life == 0 or life == 1, 'incorrect life condition'

    # 周围生命太多——死亡
    def testLifeChanger1(self):
        self.mapStorage.map[49][49] = self.mapStorage.map[49][50] = self.mapStorage.map[49][51] = 1
        self.mapStorage.map[50][49] = self.mapStorage.map[50][51] = 1
        self.mapStorage.map[51][49] = self.mapStorage.map[51][50] = self.mapStorage.map[51][51] = 0
        assert self.lifeChanger.life_change(self.mapStorage, 50, 50) == 0, 'incorrect life change1'

    # 周围生命太少——死亡
    def testLifeChanger2(self):
        self.mapStorage.map[49][49] = self.mapStorage.map[49][50] = self.mapStorage.map[49][51] = 0
        self.mapStorage.map[50][49] = self.mapStorage.map[50][51] = 0
        self.mapStorage.map[51][49] = self.mapStorage.map[51][50] = self.mapStorage.map[51][51] = 0
        assert self.lifeChanger.life_change(self.mapStorage, 50, 50) == 0, 'incorrect life change2'

    # 周围生命==3——存活
    def testLifeChanger3(self):
        self.mapStorage.map[49][49] = self.mapStorage.map[49][50] = self.mapStorage.map[49][51] = 1
        self.mapStorage.map[50][49] = self.mapStorage.map[50][51] = 0
        self.mapStorage.map[51][49] = self.mapStorage.map[51][50] = self.mapStorage.map[51][51] = 0
        assert self.lifeChanger.life_change(self.mapStorage, 50, 50) == 1, 'incorrect life change3'

    # 周围生命==2——不变
    def testLifeChanger4(self):
        self.mapStorage.map[49][49] = self.mapStorage.map[49][50] = self.mapStorage.map[49][51] = 0
        self.mapStorage.map[50][49] = self.mapStorage.map[50][51] = 1
        self.mapStorage.map[51][49] = self.mapStorage.map[51][50] = self.mapStorage.map[51][51] = 0
        assert self.lifeChanger.life_change(self.mapStorage, 50, 50) == self.mapStorage.map[50][50], 'incorrect life ' \
                                                                                                     'change4 '

    def testLifeCycleController(self):
        assert self.lifeCycleController.getCycleTime() == 0.2, 'incorrect cycle time'
        self.mapStorage.map[49][49] = self.mapStorage.map[49][50] = self.mapStorage.map[49][51] = 1
        self.mapStorage.map[50][49] = self.mapStorage.map[50][51] = 1
        self.mapStorage.map[51][49] = self.mapStorage.map[51][50] = self.mapStorage.map[51][51] = 0
        self.lifeCycleController.cycle(self.mapStorage)
        assert self.mapStorage.map[50][50] == 0, 'incorrect cycle'


def suite():
    suite = unittest.TestSuite()
    suite.addTest(GameOfLifeTestCase('testMapStorage'))
    suite.addTest(GameOfLifeTestCase('testLifeChanger1'))
    suite.addTest(GameOfLifeTestCase('testLifeChanger2'))
    suite.addTest(GameOfLifeTestCase('testLifeChanger3'))
    suite.addTest(GameOfLifeTestCase('testLifeChanger4'))
    suite.addTest(GameOfLifeTestCase('testLifeCycleController'))
    return suite


if __name__ == "__main__":
    unittest.main()


# assertEqual(a,b,msg="None")  判断a,b是否相等，不相等时，抛出msg；
# assertTure(x,msg="None") 判断x表达式是否为真，表达式为假时，抛出msg；
# assertIn(a,b,msg="None") 判断a是否在b里面，a不在b里面时，抛出msg；
# assertIsNone(x,msg="None") 判断x是否为空，x不为空时，抛出msg。