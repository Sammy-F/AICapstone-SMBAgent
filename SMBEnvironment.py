from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

from colorama import Fore

class SMBEnvironment:

    state = None
    reward = None
    done = True
    info = None

    def __init__(self):
        self.newEnvironment()

    def runRandom(self, numSteps=5000, verbose=True):
        if self.closed:
            self.newEnvironment()
        self.done = True
        for step in range(numSteps):
            self.randomStep(verbose)
        self.env.close()
        self.closed = True


    def randomStep(self, verbose=True):
        if self.done:
            self.state = self.env.reset()
        self.state, self.reward, self.done, self.info = self.env.step(self.env.action_space.sample())
        self.env.render()

        if verbose:
            print(str(self))

    def newEnvironment(self):
        env = gym_super_mario_bros.make('SuperMarioBros-v0')
        self.env = JoypadSpace(env, SIMPLE_MOVEMENT)
        self.closed = False

    def __str__(self):
        return "***State***\n{state}\n\n***Reward***\n{reward}\n\n***Info***\n{info}".format(
            state=self.state, reward=self.reward, info=self.info
        )
