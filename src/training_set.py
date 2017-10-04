class TrainingSet(object):
    def __init__(self):
        self.n = 2
        self.m = 4

        self.data_set = dict((i, dict((j, 0) for j in range(0, 10))) for i in range(0, 10))

        self.data_set[0][0] = 1
        self.data_set[0][1] = 2104/2000
        self.data_set[0][2] = 5/30
        self.data_set[0][3] = 1
        self.data_set[0][4] = 45

        self.data_set[1][0] = 1
        self.data_set[1][1] = 1416/2000
        self.data_set[1][2] = 3/30
        self.data_set[1][3] = 2
        self.data_set[1][4] = 40

        self.data_set[2][0] = 1
        self.data_set[2][1] = 1534/2000
        self.data_set[2][2] = 30/30
        self.data_set[2][3] = 2
        self.data_set[2][4] = 30

        self.data_set[3][0] = 1
        self.data_set[3][1] = 852/2000
        self.data_set[3][2] = 2/30
        self.data_set[3][3] = 1
        self.data_set[3][4] = 36

        self.labels = [460, 232, 315, 178]
