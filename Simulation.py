from SMBEnvironment import SMBEnvironment

""" Run default simulation. """
if __name__ == "__main__":
    env = SMBEnvironment()
    env.runRandom(numSteps=5)
    env.runRandom(numSteps=5000, verbose=False)