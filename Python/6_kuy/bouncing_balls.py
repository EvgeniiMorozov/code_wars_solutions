# https://www.codewars.com/kata/5544c7a5cb454edb3c000047


def bouncing_ball(h: float, bounce: float, window: float):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        rebound_height = h * bounce
        counter = 1
        while rebound_height > window:
            if rebound_height < window:
                counter += 1
            rebound_height *= bounce
            counter += 2

        return counter

    return -1


if __name__ == "__main__":
    print(bouncing_ball(2, 0.5, 1))
    print(bouncing_ball(3, 0.66, 1.5))
    print(bouncing_ball(30, 0.66, 1.5))
    print(bouncing_ball(30, 0.75, 1.5))
