from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("THE SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        for seg in snake.turtles:
            if food.distance(seg) < 10:
                food.refresh()
        snake.extend()
        score.scores()

    if (snake.head.xcor() > 300) or (snake.head.xcor() < -300) or (snake.head.ycor() > 300) or\
            (snake.head.ycor() < -300):
        is_game_on = False
        score.high_score()
        score.game_over()

    for seg in snake.turtles[1:]:
        if snake.head.distance(seg) < 10:
            is_game_on = False
            score.high_score()
            score.game_over()

screen.exitonclick()
