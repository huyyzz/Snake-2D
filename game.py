import random
##board = 20x20

class SnakeGame:
    def __init__(self):
        try:
            with open("Diemcao.txt", "r") as f:
                self.highscore = int(f.read())
        except:
            self.highscore = 0

        self.reset()

    def reset(self):
        ## khoiwr tạo 3 ví trị của rắn
        self.snake = [
            [10, 10],
            [9, 10],
            [8, 10]
        ]

        # self.snake = [
        #    [random.randint(5, 10), random.randint(5, 10)]
        # ]
        
        ## hướng ban đầu ->
        self.direction = "RIGHT"
        self.next_direction = "RIGHT"
        self.game_over = False
        self.paused = True

        ## +1 đồ ăn free
        self.food = self.random_food()

        self.score = 0

    def random_food(self):
        while True:
            p = [
                random.randint(0, 19),
                random.randint(0, 19)
            ]
            if p not in self.snake:
                return p

    def change_direction(self, d):
        if self.game_over:  
            return

        opposite = {
            "UP":"DOWN",
            "DOWN":"UP",
            "LEFT":"RIGHT",
            "RIGHT":"LEFT"
        }

        if d != opposite[self.direction]:
            self.next_direction = d

    def update(self):
        if self.game_over:
            return

        self.direction = self.next_direction

        x, y = self.snake[0]
        if self.direction=="UP":
            y -= 1
        elif self.direction=="DOWN":
            y += 1
        elif self.direction=="LEFT":
            x -= 1
        elif self.direction=="RIGHT":
            x += 1
        head = [x, y]

        ## di qua tuong
        ## chắc đổi qua kiểu đi qua tường -> nhảy qua bên kia 14/7/2026 
        if x < 0 or y < 0 or x >= 20 or y >= 20:
            # self.game_over = True
            # return
            x = (x + 20) % 20
            y = (y + 20) % 20
            head = [x, y]
        
        # if head in self.snake:
        #     self.game_over = True

        ## cắn nhầm vào đít
        if head in self.snake:
            if self.score > self.highscore:
                self.highscore = self.score

            with open("Diemcao.txt", "w") as f:
                f.write(str(self.highscore))


            self.game_over = True 
            return
        
        self.snake.insert(0, head)
        if head==self.food:
            self.score += 1
            self.food=self.random_food()
        else:
            self.snake.pop()
            # pass ##check nếu di  chuyển + k ăn thì mất cái đuôi sau cùng
    def state(self):
        return {
            "snake": self.snake,
            "food": self.food,
            "score": self.score,
            "highscore": self.highscore,
            "game_over": self.game_over,
            "paused": self.paused
        }
    def restart():
        self.reset()