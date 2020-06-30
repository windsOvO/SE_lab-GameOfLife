import profile
import GameOfLife


def profileTest():
    a = 100
    b = 100
    world = GameOfLife.MapStorage(a, b)
    controller = GameOfLife.LifeCycleController(0.2)
    controller.run_cycle_gui(world)


if __name__ == "__main__":
    profile.run("profileTest()")
