import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_size()

    # Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        flag=False
        scoreboard.game_over()

    for segment in snake.seg:
        if snake.head.distance(segment) < 10 and segment != snake.head:
            flag=False
            scoreboard.game_over()

screen.exitonclick()